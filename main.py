import time
import pyautogui
import threading
import keyboard
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Attempt to load the CLICK_INTERVAL variable from .env and print to debug
click_interval = os.getenv('CLICK_INTERVAL')
if click_interval:
    print(f"Loaded interval from .env: {click_interval}")
else:
    print("No interval found in .env. Using default.")

# Get the click interval from the .env file, or use a default if not set
interval = float(click_interval) if click_interval else 0.5  # Defaults to 0.5 if not found
print(f"Click Interval: {interval} seconds.")

# Function to perform the auto-clicking
def clicker(interval, stop_event):
    print(f"Auto-clicker started! Clicking every {interval} seconds. Press 'q' to stop.")
    while not stop_event.is_set():
        pyautogui.click()  # Click at the current mouse position
        time.sleep(interval)

# Function to listen for the 'q' key to stop the script
def listen_for_stop(stop_event):
    keyboard.wait('q')  # Waits until the 'q' key is pressed
    stop_event.set()

# Main part of the script
if __name__ == "__main__":
    try:
        # Create an event to stop the thread
        stop_event = threading.Event()

        # Start listening for stop key in a separate thread
        stop_thread = threading.Thread(target=listen_for_stop, args=(stop_event,))
        stop_thread.start()

        # Start the auto-clicker in a separate thread
        clicker_thread = threading.Thread(target=clicker, args=(interval, stop_event))
        clicker_thread.start()

        # Wait for the clicker to finish or be stopped
        clicker_thread.join()
        stop_thread.join()

        print("Auto-clicker stopped.")
    except KeyboardInterrupt:
        print("\nScript terminated manually.")
