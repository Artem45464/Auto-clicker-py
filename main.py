import time
import threading
from pynput.mouse import Button, Controller
import keyboard

# Initialize mouse controller
mouse = Controller()
auto_clicking = False
click_timer = None

def perform_click():
    """Click once and reschedule next click."""
    global click_timer  # Ensure click_timer is treated as global
    if auto_clicking:
        mouse.click(Button.left, 1)
        click_timer = threading.Timer(0.05, perform_click)  # Adjusted for 20 CPS (0.05 seconds)
        click_timer.start()

def start_auto_clicking():
    """Start auto-clicking."""
    global auto_clicking
    if not auto_clicking:  # Start only if not running already
        auto_clicking = True
        perform_click()  # Start the first click and schedule subsequent ones
        print("Auto-clicker started.")
    else:
        print("Auto-clicker is already running.")

def stop_auto_clicking():
    """Stop auto-clicking."""
    global auto_clicking
    if auto_clicking:
        auto_clicking = False
        if click_timer:
            click_timer.cancel()  # Cancel any ongoing click timer
        print("Auto-clicker stopped.")
    else:
        print("Auto-clicker is not running.")

def main():
    """Main function to monitor keypresses."""
    print("Press 'k' to start/stop the auto-clicker.")
    print("Press 'q' to exit the program.")
    
    while True:
        if keyboard.is_pressed('k'):
            if not auto_clicking:
                start_auto_clicking()
            else:
                stop_auto_clicking()
            time.sleep(0.3)  # Slight delay to avoid repeating while key is held

        if keyboard.is_pressed('q'):
            stop_auto_clicking()
            print("Exiting program.")
            break  # Exit the loop and end the program

if __name__ == "__main__":
    main()
