# Auto Clicker

A lightweight, professional-grade Python utility that automates mouse clicking with precise timing control. Perfect for testing, automation tasks, or games that require rapid clicking.

## Features
- **Adjustable CPS**: Dynamically change clicks per second (1-1000 CPS) while running
- **Precise timing mechanism**: Accurate click timing with minimal drift
- **Thread-safe implementation**: Rock-solid stability with proper synchronization
- **Simple keyboard controls**: Easy-to-use hotkeys for all functions
- **Low resource usage**: Efficient CPU usage with smart sleep scheduling
- **Clean exit**: Robust resource cleanup and error handling
- **Object-oriented design**: Professional code structure for easy maintenance

## Controls
- Press **k** to start/stop auto-clicking
- Press **+** or **=** to increase CPS by 5
- Press **-** or **_** to decrease CPS by 5
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

You'll see a control panel with all available commands:
```
==================================================
Auto-Clicker Control Panel
==================================================
Current CPS: 20

Controls:
  'k'     - Start/Stop auto-clicking
  '+'/'=' - Increase CPS by 5
  '-'/'_' - Decrease CPS by 5
  'q'     - Exit program
==================================================
```

### Adjusting Click Speed
- Start with the default 20 CPS
- Press **+** to increase to 25, 30, 35... up to 1000 CPS
- Press **-** to decrease to 15, 10, 5... down to 1 CPS
- Changes take effect immediately, even while clicking

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
- **Class-based architecture**: `AutoClicker` class encapsulates all functionality
- **Thread synchronization**: Multiple locks prevent race conditions
- **Precise timing**: `time.perf_counter()` for high-resolution timing
- **Smart sleep scheduling**: Chunked sleeps for long intervals with periodic checks
- **Dynamic timeout**: Cleanup timeout scales with CPS for reliable shutdown
- **Exception handling**: Comprehensive error handling throughout
- **No busy-waiting**: Efficient CPU usage even at high CPS

## Technical Details

### Threading Model
- Main thread handles keyboard input
- Separate daemon thread performs clicking
- Thread-safe state management with `threading.Lock()`
- Clean shutdown with proper thread joining

### Timing Accuracy
- Uses `time.perf_counter()` for microsecond precision
- Compensates for timing drift with schedule-based clicking
- Resyncs if system falls behind by more than 5 intervals

### Safety Features
- Prevents multiple simultaneous runs
- Cleanup flag prevents double cleanup execution
- Click error handling won't crash the program
- CPS validation (1-1000 range)

## Requirements
- Python 3.6+
- pynput library

## Troubleshooting

### macOS
Ensure Terminal (or your Python app) has Accessibility permissions:
1. Open **System Settings** (or System Preferences)
2. Go to **Privacy & Security** > **Accessibility**
3. Add Terminal or your Python IDE to the list
4. Toggle it on

### Windows
No special permissions required. If you encounter issues:
- Try running the terminal as administrator
- Ensure no antivirus is blocking Python

### Linux
You may need to adjust input device permissions:
```bash
sudo usermod -a -G input $USER
```
Log out and back in for changes to take effect.

### Common Issues

**"Click error" messages**
- Another application may be interfering with mouse control
- Try closing other automation tools or gaming software

**Keyboard input not working**
- Ensure the terminal window has focus
- On some systems, you may need to run with elevated privileges

**Program won't exit**
- Press **q** to exit gracefully
- If stuck, use **Ctrl+C** in the terminal

## Notes
- Always run the script from a terminal for proper keyboard input and output
- Position your mouse cursor before starting the clicker
- Some games and applications may detect and block auto-clickers
- Use responsibly and in accordance with terms of service

## License
This project is provided as-is for educational and personal use.

## Contributing
Feel free to submit issues, fork the repository, and create pull requests for any improvements.
