# Auto Clicker

A lightweight, professional-grade Python utility that automates mouse clicking with precise timing control. Perfect for testing, automation tasks, or games that require rapid clicking.

## Features
- **Adjustable CPS**: Dynamically change clicks per second (1-1000 CPS) while running
- **Precise timing**: Accurate click timing with minimal drift using `time.perf_counter()`
- **Thread-safe implementation**: Rock-solid stability with proper synchronization
- **Simple keyboard controls**: Easy-to-use hotkeys for all functions
- **Low resource usage**: Efficient CPU usage with smart sleep scheduling
- **Clean exit**: Robust resource cleanup and error handling
- **Object-oriented design**: Professional code structure for easy maintenance
- **Improved error handling**: Specific exception handling with informative error messages

## Controls
| Key | Action |
|-----|--------|
| `k` | Start/Stop auto-clicking |
| `+` or `=` | Increase CPS by 5 |
| `-` or `_` | Decrease CPS by 5 |
| `q` | Exit program |

## Installation

### 1. Navigate to the Project Folder
```bash
cd /Users/your_username/Desktop/Auto-clicker
```

### 2. Create the Virtual Environment
```bash
python3 -m venv .venv
```

### 3. Activate the Virtual Environment
On macOS/Linux:
```bash
source .venv/bin/activate
```
On Windows:
```bash
.venv\Scripts\activate
```
You should see `(.venv)` at the beginning of your terminal prompt.

### 4. Install Required Packages
```bash
pip install pynput
```

## Usage

### Run the Script
Make sure your virtual environment is activated, then run:
```bash
python3 main.py
```

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
- Default is 20 CPS
- Press `+` to increase to 25, 30, 35... up to 1000 CPS
- Press `-` to decrease to 15, 10, 5... down to 1 CPS
- Changes take effect immediately, even while clicking

### Check or Upgrade pynput
```bash
pip show pynput
pip install --upgrade pynput
```

## Code Overview
- **Class-based architecture**: `AutoClicker` class encapsulates all functionality
- **Thread synchronization**: Multiple locks prevent race conditions
- **Precise timing**: `time.perf_counter()` for high-resolution timing
- **Smart sleep scheduling**: Chunked sleeps for long intervals with periodic checks
- **Dynamic timeout**: Cleanup timeout scales with CPS for reliable shutdown
- **Specific exception handling**: Errors are caught, logged, and never silently swallowed
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
- Click errors are caught and printed without crashing the program
- Listener stop errors are caught and printed via thread-safe print
- CPS validation (1-1000 range)

## Requirements
- Python 3.6+
- pynput

## Troubleshooting

### macOS
Ensure Terminal (or your Python app) has Accessibility permissions:
1. Open **System Settings** → **Privacy & Security** → **Accessibility**
2. Add Terminal or your Python IDE to the list
3. Toggle it on

> Without this, pynput cannot control the mouse or keyboard.

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

**`ModuleNotFoundError: No module named 'pynput'`**
- Your virtual environment is not activated or pynput is not installed
- Run `source .venv/bin/activate` then `pip install pynput`

**"Click error" messages**
- Another application may be interfering with mouse control
- Try closing other automation tools or gaming software

**Keyboard input not working**
- Ensure the terminal window has focus
- On macOS, check Accessibility permissions (see above)

**"Listener stop error" messages**
- This is non-fatal — the program will still exit cleanly
- Usually caused by the listener already being stopped

**Program won't exit**
- Press `q` to exit gracefully
- If stuck, use `Ctrl+C` in the terminal
