# Auto Clicker

## Controls
The controls are as follows:

- Press "k" to start auto-clicking
- Press "k" again to stop auto-clicking
- Press "q" to exit the program

## Create the .venv Folder
To set up the virtual environment, run the following in your terminal:

```bash
cd /Users/your_username/Desktop/Auto-clicker-py
python3 -m venv .venv
```
# Activate Your Virtual Environment
Before installing any packages, make sure your virtual environment is activated:
```bash
cd /Users/your_username/Desktop/Auto-clicker-py
source .venv/bin/activate
```
If the terminal prompt shows (.venv) at the beginning, it means the virtual environment is active.

# Run Script as Administrator
To run the Python script with administrator permissions on macOS, prepend sudo to your script execution:
```bash
sudo python3 main.py
```

# Verify pynput Version
Check the currently installed version of the pynput library:
```bash
pip3 show pynput
```
If you need to update to the latest version of pynput, use the following command:
```bash
pip3 install --upgrade pynput
```
