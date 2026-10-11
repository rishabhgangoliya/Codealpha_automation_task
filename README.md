# CodeAlpha Automation Task

A Python script that automates three small, repetitive tasks from a simple menu.

## Features
1. **Move .jpg files:** moves all .jpg images from one folder into a new folder.
2. **Extract emails:** finds all unique email addresses in a .txt file and saves them to another file.
3. **Scrape a webpage title:** downloads a webpage and saves its title to a file.

## Concepts Used
os, shutil, re (regular expressions), requests, file handling

## How to Run
1. Install the requests library: `pip install requests`
2. Run the script: `python automation.py`
3. Choose option 1, 2 or 3 and follow the prompts.

## Example Output
- Option 1: Moved: photo1.jpg ... Done! 5 file(s) moved to 'images'.
- Option 2: Done! 5 unique email(s) saved to 'emails.txt'.
- Option 3: Page title: Welcome to Python.org, saved to 'title.txt'.
