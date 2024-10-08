#!/usr/bin/env python
"""
Utility to move Mouse
"""

import time
import argparse
import sys
import pyautogui
from datetime import datetime

banner = r"""\
 ______          ______                            ______             
(_____ \        |  ___ \                          (____  \       _    
 _____) )   _   | | _ | | ___  _   _  ___  ____    ____)  ) ___ | |_  
|  ____/ | | |  | || || |/ _ \| | | |/___)/ _  )  |  __  ( / _ \|  _) 
| |    | |_| |  | || || | |_| | |_| |___ ( (/ /   | |__)  ) |_| | |__ 
|_|     \__  |  |_||_||_|\___/ \____(___/ \____)  |______/ \___/ \___)
       (____/                                                         
                                          
                +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
                |P|o|w|e|r|e|d| |b|y| |B|r|o|o|t|w|a|r|e|
                +-+-+-+-+-+-+-+ +-+-+ +-+-+-+-+-+-+-+-+-+
                
    https://github.com/brootware
    https://brootware.github.io 
    """

def runMouse(time_to_stop, time_interval):
    print("If you want to stop the bot, press CTRL+C in the terminal")
    pyautogui.FAILSAFE = False
    
    if time_interval is None:
        time_interval=0.5
    else:
        time.sleep(float(time_interval))

    # Start of program
    condition_to_run = True
    while condition_to_run:
        # get current time
        current_time = time.localtime()
        # x=0
        # while(x<time_interval):
        #     time.sleep(60)
        #     x+=1
        time.sleep(float(time_interval))
        for i in range(0,10):
            pyautogui.moveTo(i*4,0)        
        pyautogui.moveTo(1,1)
        for i in range(0,3):
            pyautogui.press("shift")
        print(f"Movement made at {datetime.now().time()}")

        if current_time > time_to_stop:
            iso_time = time.strftime("%H:%M:%S", time_to_stop)
            print(f"[ + ] It's after {iso_time} now, stopping this script.")
            condition_to_run = False


def main():
    print(banner)
    parser = argparse.ArgumentParser()
    parser.add_argument("time", help="Please enter the time in HH:MM:SS format. E.g: 23:00:00")
    parser.add_argument(
        "-i",
        "--interval",
        help="Add in time interval in seconds. (E.g 30) for 30 seconds",
    )
    args = parser.parse_args()

    try:
        current_date = time.strftime("%Y %m %d")
        args.time = time.strptime(f"{current_date} {args.time}", "%Y %m %d  %H:%M:%S")
    except ValueError:
        print(f"[-] The time you entered is incorrect. Try again in HH:MM:SS format")

    args.interval = float(args.interval)

    try:
        runMouse(args.time, args.interval)
    except KeyboardInterrupt:
        print(f"[!] The bot is stopped by the user. Good bye!")
        sys.exit()


if __name__ == "__main__":
    main()
