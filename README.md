# AFK-Mouse-Jiggler

# Random Mouse Mover Script

## Description

This Python script automates mouse movement and clicking using the `pyautogui` library. It randomly moves the mouse cursor across the screen and performs clicks at specific positions. The purpose of this script might be to keep the system awake or prevent it from locking, but it can also be used for testing purposes or creating automation workflows.

### Dependencies

- Python 3.x
- `pyautogui`
- `random`
- `time`

### Installation

Before using the script, make sure you have Python installed. You will also need to install the `pyautogui` library. You can do this by running:

```sh
pip install pyautogui

How It Works

    The script gets the screen size using screen.size().
    It then enters an infinite loop (while True:) to move the mouse.
    In each iteration of the loop:
        It randomly generates new x and y coordinates within the bounds of your screen.
        It moves the mouse to the new random coordinates using screen.moveTo(x1, y1).
        It clicks at a fixed position (x/2, y-30), which is generally near the middle bottom of the screen.
        It pauses for a random time interval between 0 and 60 seconds.

Parameters

    Screen Size: The script retrieves the screen size (x, y) to ensure that random positions are within the bounds.
    Mouse Movement: The random coordinates (x1, y1) for moving the mouse are generated based on the screen size.
    Mouse Click: After moving the mouse, it clicks a fixed position at the center bottom of the screen (x/2, y-30).
    Sleep Interval: The script sleeps for a random time interval (0 to 60 seconds) before repeating the process. 
    This behavior mimics human actions to avoid detection if used for automation.
