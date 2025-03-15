# Auto Clicker

A lightweight Python utility that automates mouse clicking at 20 clicks per second. Perfect for testing, automation tasks, or games that require rapid clicking.

## Controls

The controls are as follows:
- Press "k" to start auto-clicking
- Press "k" again to stop auto-clicking
- Press "q" to exit the program

## Installation

### Create the .venv Folder

To set up the virtual environment, run the following in your terminal:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py
python3 -m venv .venv
```

### Activate Your Virtual Environment

Before installing any packages, make sure your virtual environment is activated:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py
source .venv/bin/activate
```
If the terminal prompt shows (.venv) at the beginning, it means the virtual environment is active.

### Install Required Packages

Install the necessary dependencies:
```bash
pip3 install pynput keyboard
```

## Usage

### Run Script as Administrator

To run the Python script with administrator permissions on macOS, prepend sudo to your script execution:
```bash
sudo python3 main.py
```

For Windows, run Command Prompt as Administrator and navigate to your script directory before executing.

### Verify pynput Version

Check the currently installed version of the pynput library:
```bash
pip3 show pynput
```

If you need to update to the latest version of pynput, use the following command:
```bash
pip3 install --upgrade pynput
```

## Requirements

- Python 3.6+
- pynput library
- keyboard library

## Troubleshooting

If you encounter permission issues:
- On macOS, ensure you've given Terminal/application accessibility permissions in System Preferences > Security & Privacy > Privacy > Accessibility
- On Windows, run the script as Administrator
- On Linux, you may need to run with sudo or adjust input device permissions

## Disclaimer

This tool is intended for legitimate use cases such as testing or automation. Using auto-clickers for online games may violate terms of service.
