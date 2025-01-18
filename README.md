# Auto clicker 

Steps:
1 Deactivate the current environment:
 ```bash
deactivate
   ```

2 Delete the existing .venv folder
 ```bash
rm -rf .venv
 ```
3 Create a new virtual environment:
 ```bash
python3 -m venv .venv
 ```
4 Activate the new environment:
 ```bash
source .venv/bin/activate
 ```

Install Required Packages: Now, you'll need to install the packages that are required for your script (pyautogui, keyboard, python-dotenv):
 ```bash
pip install pyautogui keyboard python-dotenv
 ```
Run Your Script: Once everything is set up, try running the script again:
 ```bash
python3 auto_clicker.py
 ```

Install Dependencies:
Make sure you have the necessary packages installed:
 ```bash
pip install pyautogui keyboard python-dotenv
```
