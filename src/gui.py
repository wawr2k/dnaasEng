import tkinter as tk
from tkinter import ttk, scrolledtext, filedialog, messagebox
import os
import logging
from script import *
from auto_updater import *
from utils import *

############################################
class ConfigPanelApp(tk.Toplevel):
    def __init__(self, master_controller, version, msg_queue):
        self.URL = "https://space.bilibili.com/8843896"
        self.TITLE = f"Double Helix Auto Monster Grinder v{version} @Dede Dellyla(Bilibili)"
        self.INTRODUCTION = f"Encountered problems? Please visit:\n{self.URL}"

        RegisterQueueHandler()
        StartLogListener()

        super().__init__(master_controller)
        self.controller = master_controller
        self.msg_queue = msg_queue
        self.geometry('950x688')
        
        self.title(self.TITLE)

        self.adb_active = False

        # 关闭时退出整个程序
        self.protocol("WM_DELETE_WINDOW", self.controller.destroy)

        # --- 任务状态 ---
        self.quest_active = False

        # --- ttk Style ---
        #
        self.style = ttk.Style()
        self.style.configure("custom.TCheckbutton")
        self.style.map("Custom.TCheckbutton",
            foreground=[("disabled selected", "#8CB7DF"),("disabled", "#A0A0A0"), ("selected", "#196FBF")])
        self.style.configure("BoldFont.TCheckbutton", font=("微软雅黑", 9,"bold"))
        self.style.configure("LargeFont.TCheckbutton", font=("微软雅黑", 12,"bold"))

        # --- UI 变量 ---
        self.config = LoadConfigFromFile()
        for attr_name, var_type, var_config_name, var_default_value in CONFIG_VAR_LIST:
            if issubclass(var_type, tk.Variable):
                setattr(self, attr_name, var_type(value = self.config.get(var_config_name,var_default_value)))
            else:
                setattr(self, attr_name, var_type(self.config.get(var_config_name,var_default_value)))
          

        self.create_widgets()        

        logger.info("**********************************")
        logger.info(f"Current version: {version}")
        logger.info(self.INTRODUCTION, extra={"summary": True})
        logger.info("**********************************")
        
        if self.last_version.get() != version:
            ShowChangesLogWindow()
            self.last_version.set(version)
            self.save_config()

    def save_config(self):

        emu_path = self.emu_path_var.get()
        emu_path = emu_path.replace("HD-Adb.exe", "HD-Player.exe")
        self.emu_path_var.set(emu_path)

        for attr_name, var_type, var_config_name, _ in CONFIG_VAR_LIST:
            if issubclass(var_type, tk.Variable):
                self.config[var_config_name] = getattr(self, attr_name).get()
        
        SaveConfigToFile(self.config)

    def create_widgets(self):
        scrolled_text_formatter = logging.Formatter('%(message)s')
        self.log_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, state=tk.DISABLED, bg='#ffffff',bd=2,relief=tk.FLAT, width = 50, height = 30)
        self.log_display.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.scrolled_text_handler = ScrolledTextHandler(self.log_display)
        self.scrolled_text_handler.setLevel(logging.INFO)
        self.scrolled_text_handler.setFormatter(scrolled_text_formatter)
        logger.addHandler(self.scrolled_text_handler)

        self.summary_log_display = scrolledtext.ScrolledText(self, wrap=tk.WORD, state=tk.DISABLED, bg="#C6DBF4",bd=2, width = 50, height = 8)
        self.summary_log_display.grid(row=1, column=1, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.summary_text_handler = ScrolledTextHandler(self.summary_log_display)
        self.summary_text_handler.setLevel(logging.INFO)
        self.summary_text_handler.setFormatter(scrolled_text_formatter)
        self.summary_text_handler.addFilter(SummaryLogFilter())
        original_emit = self.summary_text_handler.emit
        def new_emit(record):
            self.summary_log_display.configure(state='normal')
            self.summary_log_display.delete(1.0, tk.END)
            self.summary_log_display.configure(state='disabled')
            original_emit(record)
        self.summary_text_handler.emit = new_emit
        logger.addHandler(self.summary_text_handler)

        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        def checkcommand():
            self.save_config()

        #设定adb
        row_counter = 0
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)  # 首行框架
        self.adb_status_label = ttk.Label(frame_row, width=20)
        self.adb_status_label.grid(row=0, column=0, sticky=tk.W)
        # 隐藏的Entry用于存储变量
        adb_entry = ttk.Entry(frame_row, textvariable=self.emu_path_var)
        adb_entry.grid_remove()
        def selectADB_PATH():
            path = filedialog.askopenfilename(
                title="Select ADB Executable File",
                filetypes=[("Executable", "*.exe"), ("All files", "*.*")]
            )
            if path:
                self.emu_path_var.set(path)
                self.save_config()
        # 浏览按钮
        self.adb_path_change_button = ttk.Button(
            frame_row,
            text="Modify",
            command=selectADB_PATH,
            width = 8,
        )
        self.adb_path_change_button.grid(row=0,column=1)
        # 初始化标签状态
        def update_adb_status(*args):
            if self.emu_path_var.get():
                self.adb_status_label.config(text="Emulator Set", foreground="green")
            else:
                self.adb_status_label.config(text="Emulator Not Set", foreground="red")
        
        self.emu_path_var.trace_add("write", lambda *args: update_adb_status())
        update_adb_status()  # 初始调用
        ttk.Label(frame_row, text="Port:").grid(row=0, column=2, sticky=tk.W, pady=5)
        vcmd_non_neg = self.register(lambda x: ((x=="")or(x.isdigit())))
        self.adb_port_entry = ttk.Entry(frame_row,
                                        textvariable=self.adb_port_var,
                                        validate="key",
                                        validatecommand=(vcmd_non_neg, '%P'),
                                        width=5)
        self.adb_port_entry.grid(row=0, column=3)
        self.button_save_adb_port = ttk.Button(
            frame_row,
            text="Save",
            command = self.save_config,
            width=5
            )
        self.button_save_adb_port.grid(row=0, column=4)

        # 分割线.
        row_counter += 1
        ttk.Separator(self.main_frame, orient='horizontal').grid(row=row_counter, column=0, columnspan=3, sticky='ew', pady=10)

        # 地下城目标
        def UpdateLvlCombo(*args):
            if self.farm_type_var.get() in DUNGEON_TARGETS.keys():
                self.farm_target_lvl_combo['value'] = list(DUNGEON_TARGETS[self.farm_type_var.get()].keys())
                if self.farm_target_lvl_combo['values'] and (self.farm_lvl_var.get() not in self.farm_target_lvl_combo['values']):
                    self.farm_lvl_var.set(self.farm_target_lvl_combo['values'][0])
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)  # 第二行框架
        ttk.Label(frame_row, text="Dungeon Target:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.farm_target_combo = ttk.Combobox(frame_row, textvariable=self.farm_type_var, values=list(DUNGEON_TARGETS.keys()), state="readonly")
        self.farm_target_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.farm_target_combo.bind("<<ComboboxSelected>>", lambda e: self.save_config())
        self.farm_type_var.trace('w', UpdateLvlCombo)

        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)  # 第二行框架
        ttk.Label(frame_row, text="Level:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.farm_target_lvl_combo = ttk.Combobox(frame_row, textvariable=self.farm_lvl_var, state="readonly", width=7)
        self.farm_target_lvl_combo.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5)
        self.farm_target_lvl_combo.bind("<<ComboboxSelected>>", lambda e: self.save_config())
        UpdateLvlCombo()
        ttk.Label(frame_row, text="Extra Parameters:").grid(row=0, column=2, sticky=tk.W, pady=5)
        self.farm_target_extra_combo = ttk.Combobox(frame_row, textvariable=self.farm_extra_var,values=DUNGEON_EXTRA, state="readonly", width=12)
        self.farm_target_extra_combo.grid(row=0, column=3, sticky=(tk.W, tk.E), pady=5)
        self.farm_target_extra_combo.bind("<<ComboboxSelected>>", lambda e: self.save_config())

        # 分割线.
        row_counter += 1
        ttk.Separator(self.main_frame, orient='horizontal').grid(row=row_counter, column=0, columnspan=3, sticky='ew', pady=10)

        # 超时设置
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)
        ttk.Label(frame_row, text="Timeout Check Per Round (seconds):").grid(row=0, column=1, sticky=tk.W, pady=5)
        self.restart_intervel_entry = ttk.Entry(frame_row,
                                             textvariable=self.restart_intervel_var,
                                             validate="key",
                                             validatecommand=(vcmd_non_neg, '%P'),
                                             width=5)
        self.restart_intervel_entry.grid(row=0, column=2)
        self.button_save_restart_intervel = ttk.Button(
            frame_row,
            text="Save",
            command = self.save_config,
            width=4
            )
        self.button_save_restart_intervel.grid(row=0, column=3)

        # 自定义轮数
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.round_custom_check = ttk.Checkbutton(
            frame_row,
            variable=self.round_custom_var,
            text="Use Custom Rounds",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.round_custom_check.grid(row=0, column=0)
        ttk.Label(frame_row, text=" | Rounds:").grid(row=0, column=1, sticky=tk.W, pady=5)
        self.round_custom_time_entry = ttk.Entry(frame_row,
                                             textvariable=self.round_custom_time_var,
                                             validate="key",
                                             validatecommand=(vcmd_non_neg, '%P'),
                                             width=5)
        self.round_custom_time_entry.grid(row=0, column=2)
        self.button_save_round_custom = ttk.Button(
            frame_row,
            text="Save",
            command = self.save_config,
            width=4
            )
        self.button_save_round_custom.grid(row=0, column=3)

        # 绿书
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.use_green_book_check = ttk.Checkbutton(
            frame_row,
            variable=self.green_book_var,
            text="Use Green Book",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.use_green_book_check.grid(row=0, column=0)

        self.use_green_book_final_check = ttk.Checkbutton(
            frame_row,
            variable=self.green_book_final_var,
            text="Only Use Green Book in Last Round",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.use_green_book_final_check.grid(row=0, column=1)



        # 分割线.
        row_counter += 1
        ttk.Separator(self.main_frame, orient='horizontal').grid(row=row_counter, column=0, columnspan=3, sticky='ew', pady=10)

        # 重置后上猪
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.cast_Q_once_check = ttk.Checkbutton(
            frame_row,
            variable=self.cast_Q_once_var,
            text="(Once Only) Release Q After Start",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.cast_Q_once_check.grid(row=0, column=0)

        # 自动放Q技能
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.cast_Q_check = ttk.Checkbutton(
            frame_row,
            variable=self.cast_q_var,
            text="Auto Cast Q Skill",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.cast_Q_check.grid(row=0, column=0)
        ttk.Label(frame_row, text=" | Interval (seconds):").grid(row=0, column=1, sticky=tk.W, pady=5)
        self.cast_Q_intervel_entry = ttk.Entry(frame_row,
                                             textvariable=self.cast_Q_intervel_var,
                                             validate="key",
                                             validatecommand=(vcmd_non_neg, '%P'),
                                             width=5)
        self.cast_Q_intervel_entry.grid(row=0, column=2)
        self.button_save_cast_Q_intervel = ttk.Button(
            frame_row,
            text="Save",
            command = self.save_config,
            width=4
            )
        self.button_save_cast_Q_intervel.grid(row=0, column=3)

        # 自动放E技能
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.cast_E_check = ttk.Checkbutton(
            frame_row,
            variable=self.cast_e_var,
            text="Auto Cast E Skill",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.cast_E_check.grid(row=0, column=0)
        ttk.Label(frame_row, text=" | Interval (seconds):").grid(row=0, column=1, sticky=tk.W, pady=5)
        self.cast_intervel_entry = ttk.Entry(frame_row,
                                             textvariable=self.cast_intervel_var,
                                             validate="key",
                                             validatecommand=(vcmd_non_neg, '%P'),
                                             width=5)
        self.cast_intervel_entry.grid(row=0, column=2)
        self.button_save_cast_intervel = ttk.Button(
            frame_row,
            text="Save",
            command = self.save_config,
            width=4
            )
        self.button_save_cast_intervel.grid(row=0, column=3)

        # E技能内部计时器
        row_counter += 1
        frame_row = ttk.Frame(self.main_frame)
        frame_row.grid(row=row_counter, column=0, sticky="ew", pady=5)

        self.cast_E_print_check = ttk.Checkbutton(
            frame_row,
            variable=self.cast_e_print_var,
            text="Print Internal Skill Release Timer",
            command=checkcommand,
            style="Custom.TCheckbutton"
            )
        self.cast_E_print_check.grid(row=0, column=0)

        # 分割线
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=4)  # Main log display takes 80% of space
        self.rowconfigure(1, weight=1)  # Summary log display takes 20% of space

        start_frame = ttk.Frame(self)
        start_frame.grid(row=1, column=0, sticky="nsew")
        start_frame.columnconfigure(0, weight=1)
        start_frame.rowconfigure(1, weight=1)

        ttk.Separator(start_frame, orient='horizontal').grid(row=0, column=0, columnspan=3, sticky="ew", padx=10)

        button_frame = ttk.Frame(start_frame)
        button_frame.grid(row=1, column=0, columnspan=3, pady=5, sticky="nsew")
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        button_frame.columnconfigure(2, weight=1)

        # Maps supported button
        self.maps_button = ttk.Button(
            button_frame,
            text="Maps Supported",
            command=self.show_maps_supported,
            width=12
        )
        self.maps_button.grid(row=0, column=0, sticky='nsew', padx=5, pady=5)

        label3 = ttk.Label(button_frame, text="",  anchor='center')
        label3.grid(row=0, column=2, sticky='nsew', padx=5, pady=5)

        s = ttk.Style()
        s.configure('start.TButton', font=('微软雅黑', 15), padding = (0,5))
        def btn_command():
            self.save_config()
            self.toggle_start_stop()
        self.start_stop_btn = ttk.Button(
            button_frame,
            text="Start Script!",
            command=btn_command,
            style='start.TButton',
        )
        self.start_stop_btn.grid(row=0, column=1, sticky='nsew', padx=5, pady= 26)


        # 分割线
        row_counter += 1
        self.update_sep = ttk.Separator(self.main_frame, orient='horizontal')
        self.update_sep.grid(row=row_counter, column=0, columnspan=3, sticky='ew', pady=10)

        #更新按钮
        row_counter += 1
        frame_row_update = tk.Frame(self.main_frame)
        frame_row_update.grid(row=row_counter, column=0, sticky=tk.W)

        self.find_update = ttk.Label(frame_row_update, text="New version found:",foreground="red")
        self.find_update.grid(row=0, column=0, sticky=tk.W)

        self.update_text = ttk.Label(frame_row_update, textvariable=self.latest_version,foreground="red")
        self.update_text.grid(row=0, column=1, sticky=tk.W)

        self.button_auto_download = ttk.Button(
            frame_row_update,
            text="Auto Download",
            width=12
            )
        self.button_auto_download.grid(row=0, column=2, sticky=tk.W, padx= 5)

        def open_url():
            url = os.path.join(self.URL, "releases")
            if sys.platform == "win32":
                os.startfile(url)
            elif sys.platform == "darwin":
                os.system(f"open {url}")
            else:
                os.system(f"xdg-open {url}")
        self.button_manual_download = ttk.Button(
            frame_row_update,
            text="Manual Download Latest Version",
            command=open_url,
            width=7
            )
        self.button_manual_download.grid(row=0, column=3, sticky=tk.W)

        self.update_sep.grid_remove()
        self.find_update.grid_remove()
        self.update_text.grid_remove()
        self.button_auto_download.grid_remove()
        self.button_manual_download.grid_remove()

    def set_controls_state(self, state):
        self.button_and_entry = [
            self.adb_path_change_button,
            self.adb_port_entry,
            self.button_save_adb_port,
            self.cast_E_check,
            self.cast_intervel_entry,
            self.button_save_cast_intervel,
            self.restart_intervel_entry,
            self.button_save_restart_intervel,
            self.use_green_book_check,
            self.use_green_book_final_check,
            self.round_custom_check,
            self.round_custom_time_entry,
            self.button_save_round_custom,
            self.cast_Q_check,
            self.cast_Q_intervel_entry,
            self.button_save_cast_Q_intervel,
            self.cast_E_print_check,
            self.farm_target_extra_combo,
            self.farm_target_combo,
            self.farm_target_lvl_combo,
            self.cast_Q_once_check,
            self.maps_button
            ]

        if state == tk.DISABLED:
            self.farm_target_combo.configure(state="disabled")
            for widget in self.button_and_entry:
                widget.configure(state="disabled")
        else:
            self.farm_target_combo.configure(state="readonly")
            for widget in self.button_and_entry:
                widget.configure(state="normal")

    def toggle_start_stop(self):
        if not self.quest_active:
            self.start_stop_btn.config(text="Stop")
            self.set_controls_state(tk.DISABLED)
            setting = FarmConfig()
            config = LoadConfigFromFile()
            for attr_name, var_type, var_config_name, var_default_value in CONFIG_VAR_LIST:
                setattr(setting, var_config_name, config[var_config_name])
            setting._FINISHINGCALLBACK = self.finishingcallback
            self.msg_queue.put(('start_quest', setting))
            self.quest_active = True
        else:
            self.msg_queue.put(('stop_quest', None))

    def show_maps_supported(self):
        """Show supported maps information in a dialog window"""
        maps_window = tk.Toplevel(self)
        maps_window.title("Supported Maps")
        maps_window.geometry("700x600")
        maps_window.resizable(True, True)

        # Create scrollable text area
        from tkinter import scrolledtext
        text_area = scrolledtext.ScrolledText(
            maps_window,
            wrap=tk.WORD,
            font=("Segoe UI", 10),
            padx=15,
            pady=15
        )
        text_area.pack(fill=tk.BOTH, expand=True)

        # Configure bold font for headers
        text_area.tag_configure("bold", font=("Segoe UI", 11, "bold"))
        text_area.tag_configure("header", font=("Segoe UI", 12, "bold"))
        text_area.tag_configure("subheader", font=("Segoe UI", 10, "bold"))
        text_area.tag_configure("note", font=("Segoe UI", 9, "italic"))

        # Insert formatted content
        text_area.insert(tk.END, "Which maps are currently supported?\n\n", "header")

        # Jiaojiao Coin section
        text_area.insert(tk.END, "🪙 Jiaojiao Coin\n", "bold")
        text_area.insert(tk.END, "• 60 Jiaojiao coins\n", "subheader")
        text_area.insert(tk.END, "• 70 Jiaojiao coins\n\n", "subheader")

        text_area.insert(tk.END, "Details:\n", "bold")
        text_area.insert(tk.END, "• 60 Jiao Jiao Coins will spawn two of the four maps, specifically the map that doesn't have water after the first reset.\n\n", "")
        text_area.insert(tk.END, "• 70 Jiaojiao Coins will spawn two of the three maps: the same map as in 65mod, and the map where the target location is directly in front after the elevator map is reset.\n\n", "")

        # Night Flight Manual section
        text_area.insert(tk.END, "📖 Night Flight Manual (Mod Version)\n", "bold")
        text_area.insert(tk.END, "• 40, 50, 55, 60, 65, 70 mod books\n\n", "subheader")

        text_area.insert(tk.END, "Details:\n", "bold")
        text_area.insert(tk.END, "• The additional parameter refers to which mod it is from top to bottom. If you don't care, it will randomly select one from 1-4.\n\n", "")

        # Character Experience section
        text_area.insert(tk.END, "⚔️ Character Experience\n", "bold")
        text_area.insert(tk.END, "• Level 50\n\n", "subheader")

        text_area.insert(tk.END, "Requirements:\n", "bold")
        text_area.insert(tk.END, "• Please make sure to equip the \"Rock Solid\" Demon Wedge.\n\n", "")

        # Breakthrough Material section
        text_area.insert(tk.END, "🔥 Breakthrough Material (Secret Letter)\n", "bold")
        text_area.insert(tk.END, "• Levels 10, 30, and 60\n\n", "subheader")

        text_area.insert(tk.END, "Details:\n", "bold")
        text_area.insert(tk.END, "• Additional parameters specify which attribute: 1-6 correspond to Water, Fire, Wind, Thunder, Light, and Darkness\n", "")
        text_area.insert(tk.END, "• No parameter corresponds to Fire\n\n", "")

        text_area.insert(tk.END, "Important Notes:\n", "bold")
        text_area.insert(tk.END, "• The 10-fire mechanic only works on the map that's on the same floor as the mechanism; it can't be used on the other map.\n", "note")
        text_area.insert(tk.END, "• The 60-fire and 30-fire versions share the same mission.\n\n", "note")

        # Weapon Breakthrough section
        text_area.insert(tk.END, "⚒️ Weapon Breakthrough\n", "bold")
        text_area.insert(tk.END, "• Levels 60 and 70\n\n", "subheader")

        text_area.insert(tk.END, "Requirements:\n", "bold")
        text_area.insert(tk.END, "• Please make sure to equip the \"Rock\" Demon Wedge.\n\n", "")

        text_area.insert(tk.END, "⚠️ Important Note:\n", "bold")
        text_area.insert(tk.END, "Due to the long duration of this task and the numerous occasional issues, please use cloud gaming whenever possible.", "note")

        text_area.configure(state='disabled')  # Make it read-only

        # Add close button
        close_button = ttk.Button(maps_window, text="Close", command=maps_window.destroy)
        close_button.pack(pady=10)

    def finishingcallback(self):
        logger.info("Stopped.")
        self.start_stop_btn.config(text="Start Script!")
        self.set_controls_state(tk.NORMAL)
        self.quest_active = False
