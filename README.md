# DNAAS - Double Helix Auto Monster Grinder

## About

This is an English translation of the DNAAS automation script.

**Credits:** This project is based on the original Chinese version available at [https://github.com/arnold2957/dnaas](https://github.com/arnold2957/dnaas)

## Features

- 🕒 24-hour unattended operation with automatic game restarting
- 🤖 Automatic dungeon entry
- ✅ Background operation, multi-instance support, headless mode
- ↻ Automatic game restart and recovery

## Getting Started

For detailed requirements, supported maps, and complete setup instructions, please visit the original repository: [https://github.com/arnold2957/dnaas](https://github.com/arnold2957/dnaas)

## Emulator and Script Settings

Please follow these steps:

1. You can download the MuMu emulator, either MuMu12 or MuMuX. Alternatively, you can use the LDPlayer emulator.

2. Set the emulator resolution to 1600×900.

3. Enable adb debugging.

4. Turn off automatic bridging.

5. Set the emulator to maximum performance. (This can be ignored for cloud gaming.)

6. Set the in-game graphics settings to the lowest level.

7. Population density adjusted to the highest level.

8. Once inside the instance, start the script.

### What is the emulator path? / The script is throwing an error after starting.

- The "emulator path" in the top left corner of the script is:
  - MuMuX: `Netease\MuMu Player 12\nx_device\12.0\shell\MuMuNxDevice.exe`
  - Similar to MuMu12

- The port number is 5555 or 16384. If neither works, you can find the adb port number in the multi-instance manager.

If it won't start, it's definitely a problem with the emulator path; check it carefully.

## Installation

1. Clone or download this repository
2. Install requirements: `pip install -r requirements.txt`
3. Run the script: `python src/main.py`

## Usage

1. Configure your emulator path and settings
2. Select your desired dungeon/map
3. Start the script
4. The script will run automatically in the background

## License

GPL-3.0 License (same as original project)

## Disclaimer


This is an automation tool for the game "Double Helix". Use at your own risk. The original developers are not responsible for any consequences of using this software.
