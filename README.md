# Auto Clicker

A lightweight Python utility that automates mouse clicking at 20 clicks per second. Perfect for testing, automation tasks, or games that require rapid clicking.

## Features
- Precise timing mechanism for accurate 20 CPS (clicks per second)
- Thread-safe implementation for smooth operation
- Simple keyboard controls
- Low resource usage
- Clean exit and resource cleanup

## Controls
- Press **k** to start auto-clicking
- Press **k** again to stop auto-clicking
- Press **q** to exit the program

## Installation

### 1. Create the Virtual Environment
Open your terminal and run:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py-main
python3 -m venv .venv
```

### 2. Activate the Virtual Environment
On macOS/Linux:
```bash
source .venv/bin/activate
```
On Windows:
```bash
.venv\Scripts\activate
```
You should see `(.venv)` at the beginning of your terminal prompt.

### 3. Install Required Packages
```bash
pip install pynput
```

## Usage

### Run the Script
Make sure your virtual environment is activated, then run:
```bash
python3 main.py
```
No administrator permissions are required.

### Check pynput Version
To check the installed version of `pynput`:
```bash
pip show pynput
```
To upgrade to the latest version:
```bash
pip install --upgrade pynput
```

## Code Overview
- Uses `threading.Event()` for clean thread control
- Thread-safe console output with a lock
- Schedule-based timing for precise 20 clicks per second
- Uses `pynput` for both mouse control and keyboard input
- Robust cleanup and error handling

## Requirements
- Python 3.6+
- pynput library

## Troubleshooting
- **macOS:** Ensure Terminal (or your Python app) has Accessibility permissions:  
  System Settings > Privacy & Security > Accessibility
- **Windows:** No special permissions required
- **Linux:** You may need to adjust input device permissions

## Notes
- Always run the script from a terminal for proper keyboard input and output.
- If you encounter issues, try running the terminal as administrator or check your system's security settings.
