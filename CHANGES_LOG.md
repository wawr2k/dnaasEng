## Notice!

This is a free script released based on a free open-source project.

This script is for programming learning purposes only. Please do not use it for illegal profit!

You can find the open-source information for this script here: https://github.com/arnold2957/dnaas

If you purchased this script from someone else or obtained it through other paid means, please report "illegal reselling" to the platform.

Thank you for your support!


**New Version!**
==v1.0.34==
Fixed: Fishing will no longer exit now.
Added: Added test version of Labyrinth. Limited to 6-constellation Madame and Blue Pulse, currently only tested on Level 70 Rogue.
Optimized: Changed server connection failure popup to built-in text.

==Announcement: dnaas Project Entering "Cooldown" Mode==
Hello everyone, thank you for your support of this project. Due to limited personal energy and the fact that long-term optimization is not the original intention of this project, I hereby notify:

After the "Labyrinth" quest is completed, this project will enter "cooldown" mode.

What does this mean?

I will no longer develop any new features that are not for my personal needs (such as "auto-switching between Cipher farming and Level 30 Fire", etc.).

Future updates will only be based on optimizing the experience on my personal device.

At the same time, adjustments to issue strategy:

For compatibility issues that only appear on specific devices (such as "a certain mode always gets stuck"), if I cannot reproduce them on my end, I will no longer provide optimization or debugging support.

For basic issues that are clearly documented (such as "ADB won't connect"), related comments will be directly ignored, with no reply.

Of course, PRs are welcome:

If you have optimization solutions for specific devices or want to implement new features, PRs are very welcome, and I will still review the code.

Thank you for your continued support, but my personal energy is really limited, and excessive pressure is hard to bear. I hope for your understanding and continued support of dnaas!

**Update History**
==v1.0.33==
Fixed: Now always clicks blank areas when fishing.
Added: The script can now automatically check for new versions and download them by accessing GitHub.

==v1.0.32==
Added: Added the fourth room of Red Pearl domain. Although testing shows it can be completed in under 300 seconds on average, a separate test version was created for safety.
Optimized: Changed Cipher-Expulsion to reset (instead of random movement at start).
Optimized: Leisurely fishing now recognizes new encyclopedia entries, and frequently clicks blank positions to skip all possible popups.

==v1.0.31==
Fixed: Fixed issue where fishing would interrupt due to "Fish Caught" prompt.

==v1.0.30==
Fixed: Fixed issue where leisurely fishing would only catch the first fish.
Optimized: Experience domains now check if left side reaches 100% or top-right corner "Go to Evacuation Point".
Optimized: Fixed issue where ranged attacks after releasing Q skill might cause continuation problems.

==v1.0.29==
Added: Added Wedge of the Abyss (Not Nautical Handbook!) quest, can farm Level 40, 60, 100 Wedge of the Abyss mixed pools.
Added: Added leisurely fishing. Since I currently don't have leisurely, feedback on this quest is welcome!
Fixed: Fixed issue where restarting when exiting a domain would incorrectly deduct one count of completed domains.
Optimized: Optimized Red Bean domain camera adjustments and count statistics.
Optimized: Level 30 Fire now looks straight at the floor to optimize game performance. (Supposedly useful.)
Optimized: Increased wait time after Q skill release to prevent shooting sometimes being ineffective.

==v1.0.28==
Optimized: Optimized Level 60 Condensed Pearl domain.
Fixed: Fixed occasional inability to evacuate.
Note: Version 1026 incorrectly outputs debug information, please delete that data()

==v1.0.27==
Added: Level 60 Condensed Pearl (test version). Only opens 3 hostages, and one rare map after hostages is not implemented. Requires spear equipment (not Spring Radiance Halberd), Threading Resonance, Blue +5 Swiftness and Purple +5 Charge Attack Speed.
Added: Now forces quest end when Survey is detected, to prevent using this script in multiplayer coin domains.
Added: In multiplayer games, recognizes and agrees to continue game requests.
Added: Level 30 mod. Same map as Level 65 mod (should be).
Fixed: Incorrectly outputs debug information (why can't Python use macros to control this).

==v1.0.26==
Fixed: Fixed issue where some runtime data was not reset after restart.
Fixed: Some devices cannot click top-left corner causing inability to re-enter/reset.
Added: When no skills are enabled, releases shot + reload + in-place double jump every 20 seconds to prevent being kicked from cloud gaming.
Fixed: Fixed issue where material domains would get stuck and couldn't enter.
Optimized: Now temporarily won't restart emulator.
Optimized: Because some devices' top-right corner doesn't update after completing quests, Level 50 experience domain now checks if left progress bar is 100%.

==v1.0.25==
Fixed: Fixed issue causing Level 70 weapon material domain recognition errors.
Fixed: Fixed issue where Q skill would repeatedly release instead of only once.
Optimized: Disabled Level 70 weapon material domain recognition prompts.

==v1.0.24==
Fixed: Attempted to fix issue where first movement was lost after weapon breakthrough domain reset.
Fixed: Level 50 experience domain now has third reset.
Fixed: Fixed issue where Q skill would repeatedly release instead of only once.
Added: Skip restart for NetEase Cloud Gaming, TapTap Cloud Gaming, etc.
Optimized: Changed Cipher quest name.
Fixed: Changed Level 70 Jiaojiao Coins default rounds.

==v1.0.23==
Added: Added Level 50 mod domain.
Added: Support for selecting all six elements for breakthrough material domains.
Added: Added restart support for Hong Kong/Macau/Taiwan/International servers. Currently using "com.panstudio.gplay.duetnightabyss.arpg.global", if you know the cloud gaming package name for international servers, please let me know.
Fixed: Fixed issue where "Release Q Once" would keep releasing.
Optimized: Optimized walnut opening survival, now Level 10 Fire version can be fully automatic. Semi-auto has been renamed to No Skill.
Optimized: Optimized walnut opening related quest text and restart logic. Can now stop normally.
Optimized: Reversed! Level 50 experience domain now goes from the right.
Optimized: Optimized Level 50 experience domain, now waits until 100% progress before evacuating.
Optimized: Slightly modified Level 70 breakthrough material domain logic.
Optimized: Modified Level 70 breakthrough material detection after second reset.

==v1.0.22==
Extra parameters refer to which mod domain from top to bottom. "No Concern" will randomly select one from the first four.

Please try to use adult female characters for positioning. If controlling the protagonist, be sure to turn off E skill! E skill has built-in displacement which causes deviation!

Added: Cloud gaming login "Start Game" and "I Know" detection.
Fixed: Fixed issue where mod domain selection would have deviation after Level 60.
Fixed: Fixed issue where it would get stuck and couldn't enter domain when default level and target level are the same.
Optimized: Level 70 mod changed to in-place AFK.
Optimized: Shortened forward distance after second reset in weapon breakthrough material domain.
Optimized: Weapon breakthrough material domain now includes one detection and correction.

==v1.0.21==
Added: Now supports mod selection. On restart, can re-farm mod from selected path.
Fixed: Fixed issue where it would get stuck at Commission and unselected quest.
Added: Now releases skills in weapon material domains.
Optimized: Weapon domains now try to run to the end.
Optimized: More efficient detection of which block the current reset is in.

==v1.0.20==
Fixed: Fixed issue that would cause cipher reward selection errors. Very sorry.
Fixed: Fixed issue where emulator couldn't be closed. Now when ADB connection errors occur, MuMu emulator can automatically restart.
Fixed: Fixed issue where game restart during domain exit would prevent continuation.
Fixed: Fixed front/back offset issue when opening locks in Level 70 experience domain.

==v1.0.19==
Optimized: Some devices would have recognition errors causing mistaken cipher selection, adjusted cipher selection click position to avoid false triggers.
Fixed: Fixed issue where E skill timer wasn't working.

==v1.0.18==
Added: Added screenshot size check to warn about incorrect emulator resolution.
Fixed: Cloud gaming now supports Level 70 weapon breakthrough materials. Note: test version, may have some recognition issues.
Fixed: Weapon breakthrough materials now try to walk back a distance after checking no lock is open.
Fixed: Removed random disturbance. (Should have been deleted long ago!)
Fixed: Fixed issue where custom wave count was ineffective.

==v1.0.17==
Added: Added Level 70 weapon breakthrough materials. Note: test version, may have some foot-stuck issues.
Added: Only use Green Book in the last round.
Optimized: Default E time changed to 7 seconds.
Fixed: Now restarts when exceeding attempt count.
Optimized: Modified character experience domain movement logic. Now runs a distance, waits a while, then continues running. Finally, modified facing direction at the end.
Optimized: Modified text when attempting to locate.
Optimized: Added quest name to summary.
Optimized: Optimized character experience domain text description.
Optimized: Modified quest icon click position to avoid getting stuck.
Optimized: Significantly optimized location logic to avoid various stuck issues.

==v1.0.15==
Added: Can now launch Jiaojiao Coins, Experience domains, and Material domains from desktop. When these domains encounter issues and restart, can restart normally.
Optimized: Slightly modified Expulsion start movement to avoid elevator issues.
Optimized: Expulsion and semi-auto are now separated. Semi-auto won't move at start, only AFKs in place.
Fixed: Fixed E random disturbance count error issue.
Optimized: Level 50 experience domain now resets 2 times.
Optimized: Level 65 mod and corresponding Level 70 Jiaojiao Coins maps optimized, now performs one double jump.
Optimized: Since people keep reporting E skill release issues, added internal timer printing function.

==v1.0.16--
Added: Added free statement.
Fixed: Fixed issue where cloud gaming would sometimes be killed immediately after startup.
Fixed: Fixed issue where it couldn't stop.

==v1.0.14==
Added: Expulsion and semi-auto have been merged. This quest can perform simple functions, including: Expulsion, auto-click next round, auto-release Q and E, auto-open cipher (select first), auto-select cipher reward (also first).

You can use this quest to farm all Expulsion and simpler quests. But note, this quest won't unlock or move (only has a fixed elevator descent operation).

Added: Can now automatically press Revive (cloud gaming testing pending).
Added: Can now control auto-release Q. Also automatically adds one ranged attack and reload after releasing Q.

(Regarding Q release and additional ranged attack: Sibyl's thunder orbs sometimes aren't recognized as enemies. Research shows attacking thunder orbs has a high probability of refreshing AI. But there are occasional cases where thunder orbs summon AI but it still idles. If you have a better solution, please let me know.)

Optimized: Slightly optimized Level 30 Fire domain positioning.
Optimized: Experience domains now try to jump twice when getting on the platform at the end.
Fixed: Multi-wave now won't incorrectly count the same wave repeatedly.
Optimized: Should no longer get stuck at "Abandon Challenge".
Fixed: Level 70 Jiaojiao Coins now only farms 1 round as stated.
Fixed: Level 70 Jiaojiao Coins can now farm the same map as Level 65 mod.

==v1.0.13==
Adapted lock opening for cloud gaming.
Added Level 50 experience domain and Level 30 Fire (default 10 waves).
Level 50 experience domain can only farm half the map.

==v1.0.12==
Added custom round count.
Level 70 Jiaojiao Coins default rounds changed to 2.
Panel timer now calculates time for one small round (e.g., 1 wave out of 15 waves of Level 10 Fire materials).
Modified spell interval counting method. No longer has high delay.
Now starts releasing first E skill faster.
Now checks and closes small moon card screen, and records. (Screenshot clarity insufficient, may need clearer images.)

==v1.0.10==
Slightly optimized Level 65 mod pathfinding. Should no longer get stuck.
Optimized Level 15 Fire full auto start. Won't walk too far now.
Expulsion start movement was misconfigured, can now descend elevator.
Added Level 70 Jiaojiao Coins. Can farm 2 out of 3 maps.

==v1.0.11==
Fixed issue where sometimes couldn't detect "Abandon Battle" causing script to stop.
(Also, changed version number)

==v1.0.8==
Added: Timeout check can now be customized.
Added: Can now try using Green Book.
Added: Added Level 15 Fire semi-auto.
Fixed: Expulsion now won't reset. (One second wall phase is too scary)
Optimized: Optimized Level 15 Fire full auto start logic. Won't keep walking forward, will also walk right a bit after completing mechanism.
Optimized: No longer repeatedly prompts "Already in domain".
Optimized: Counter no longer counts repeatedly.
Optimized: E skill auto-release now has random disturbance.

==v1.0.9==
Optimized: Reduced random disturbance variance.
Optimized: Expulsion added auto-walk forward at start.

==v1.0.7==
Full auto 15 waves Fire materials. Requires Skill. 260+ range Jellyfish.

==v1.0.6==
Now supports cloud gaming. If game won't open, cloud gaming is recommended.

==v1.0.5==
Fixed issue where Level 60 Jiaojiao Coins would start moving on un-farmable maps.
Added simple Level 15 Fire Endless Exploration. Currently requires manual positioning first, auto-evacuate after 15 waves.

==v1.0.4==
Added: Cloud gaming character reset detection.
Added: Custom E skill release interval.
Optimized: Use reset to reach Level 65 mod mechanism.

==v1.0.3==
Test version
Includes Level 65 Jiaojiao Coins and Level 65 mod.
Level 65 Jiaojiao Coins can only farm half the map.
May have some issues, those unwilling to try can wait for stable version.

==v1.0.2==
Fixed: Fixed issue where couldn't enter ESC interface.
Fixed: Fixed issue where sometimes would get stuck in elevator shaft.
