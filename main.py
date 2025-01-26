import time
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener
import threading

# Initialize mouse controller
mouse = Controller()
auto_clicking = False
click_timer = None

def perform_click():
    """Click once and reschedule next click"""
    if auto_clicking:
        mouse.click(Button.left, 1)
        click_timer = threading.Timer(0.05, perform_click)  # Delay adjusted for 20 CPS
        click_timer.start()

def start_auto_clicking():
    """Start auto-clicking"""
    global auto_clicking
    auto_clicking = True
    perform_click()  # Perform the first click and schedule subsequent ones

def stop_auto_clicking():
    """Stop auto-clicking"""
    global auto_clicking
    auto_clicking = False
    if click_timer:
        click_timer.cancel()  # Cancel any future clicks

def on_press(key):
    """Handles key press events"""
    try:
        if hasattr(key, 'char'):
            if key.char == 'k':  # Start/Stop auto-clicking on 'k' press
                if not auto_clicking:
                    start_auto_clicking()
                    print("Auto-clicker started.")
                else:
                    stop_auto_clicking()
                    print("Auto-clicker stopped.")

            elif key.char == 'q':  # Exit the program on 'q'
                stop_auto_clicking()
                print("Exiting program.")
                return False  # Exit listener
    except AttributeError:
        pass  # If key doesn't have 'char', skip it

def main():
    """Main function to run the listener"""
    print("Press 'k' to start/stop auto-clicker, 'q' to quit.")
    # Start the keyboard listener
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
