# Auto Clicker
A lightweight Python utility that automates mouse clicking at 20 clicks per second. Perfect for testing, automation tasks, or games that require rapid clicking.

## Features
- Precise timing mechanism for accurate 20 CPS (clicks per second)
- Thread-safe implementation for smooth operation
- Simple keyboard controls
- Low resource usage

## Controls
The controls are as follows:
- Press "k" to start auto-clicking
- Press "k" again to stop auto-clicking
- Press "q" to exit the program

## Installation

### Create the .venv Folder
To set up the virtual environment, run the following in your terminal:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py-main
python3 -m venv .venv
```

### Activate Your Virtual Environment
Before installing any packages, make sure your virtual environment is activated:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py-main
source .venv/bin/activate
```
If the terminal prompt shows (.venv) at the beginning, it means the virtual environment is active.

### Install Required Packages
Install the necessary dependencies:
```bash
pip3 install pynput
```

## Usage

### Run Script
To run the Python script:
```bash
python3 main.py
```
No administrator permissions are required.

### Verify pynput Version
Check the currently installed version of the pynput library:
```bash
pip3 show pynput
```
If you need to update to the latest version of pynput, use the following command:
```bash
pip3 install --upgrade pynput
```

## Code Overview
The auto-clicker utilizes threading to handle continuous clicking without blocking the main program:
- Uses threading.Event() for clean thread control
- Implements a lock mechanism for thread-safe console output
- Uses a schedule-based timing mechanism for precisely 20 clicks per second
- Uses pynput for both mouse control and keyboard input

## Requirements
- Python 3.6+
- pynput library

## Troubleshooting
If you encounter issues:
- On macOS, ensure you've given Terminal/application accessibility permissions in System Preferences > Security & Privacy > Privacy > Accessibility
- On Windows, no special permissions are required
- On Linux, you may need to adjust input device permissions
