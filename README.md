# Pyrus

A lighthearted desktop prank written in Python!

This script takes a snapshot of the current desktop, displays fake error screens (like fake BSODs), and ends with a funny image to surprise the user. 
It's designed to be harmless, temporary, and for consensual fun only.

## Requirements

- Python 3.x
- - `pyautogui`
- `PIL.Image` (from Pillow)
- `ImageTk` (from Pillow)
- `winsound` (standard on Windows)


## Overview
This script creates a fake Blue Screen of Death (BSOD) using:

tkinter for GUI

pyautogui to take a screenshot of the desktop

winsound to play a sound

PIL for image processing

Once started (by clicking on the full-screen window), it displays a sequence of pre-made BSOD-like images (bsod1.png to bsod8.png) as a fullscreen overlay — simulating a system crash.
To exit the programm u need to press the ( Esc ) button on your keyboard!
