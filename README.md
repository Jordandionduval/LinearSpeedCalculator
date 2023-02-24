# LinearSpeedCalculator
A maya script used to quickly calculate movement speed in units/time.

![image](https://user-images.githubusercontent.com/84198946/221055881-48206247-b9de-4d96-acd1-46dd3e0a4e14.png)

###### Table of content
- [Overview](https://github.com/Jordandionduval/LinearSpeedCalculator#overview "Overview")
- [Installation](https://github.com/Jordandionduval/LinearSpeedCalculator#installation "Installation")
- [Known Issues](https://github.com/Jordandionduval/LinearSpeedCalculator#known-issues "Known Issues")

<!-- This is a comment -->
<!--###### Other Pages
- [Patch Notes](../LinearSpeedCalculator/blob/main/PATCHNOTES.md "Go to Patch Notes page")-->

## Overview

This tool was made to help my animator colleagues sync up walk/run cycles with in-game character movement speed. This can be useful to avoid feet sliding on the ground. The logic for this was initially made in about a day, but I later added UI and tweaked the logic to work with vector data another day.

The tool requires the user to select a controller with its translate attributes animated and specify a start and end frame.
The distance is calculated from the translate vectors at the specified keys. The duration is determined using the provided keys, divide by framerate (fps).
Distance is then divided by duration, which gives us the speed in units per seconds.

---

## Installation
1. Copy the "jdd_LinearSpeedCalculator.py" to your Maya scripts directory:
>MyDocuments\Maya\scripts\

2. Then, within maya, use the following text as a python script to run the tool:
```
import jdd_LinearSpeedCalculator as scpt
scpt.UI()
```
3. *(Optional)* Alternatively, the text can be saved in the custom shelf using maya's script editor. This makes the script a small button in your current shelf so it can easily be accessed later.

---

## Known Issues
- Nothing so far!
