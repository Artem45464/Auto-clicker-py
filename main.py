import time
import threading
import keyboard
from pynput.mouse import Button, Controller

# Initialize mouse controller
mouse = Controller()
click_event = threading.Event()

def auto_click(cps=20):
    interval = 1 / cps
    while click_event.is_set():
        mouse.click(Button.left, 1)
        time.sleep(interval)

def main():
    print("Press 'k' to start/stop auto-clicker, 'q' to quit.")
    while True:
        if keyboard.is_pressed('k'):
            if click_event.is_set():
                click_event.clear()
                print("Auto-clicker stopped.")
            else:
                click_event.set()
                threading.Thread(target=auto_click, daemon=True).start()
                print("Auto-clicker started.")
            time.sleep(0.3)  # Prevents multiple triggers from one keypress

        if keyboard.is_pressed('q'):
            click_event.clear()
            print("Exiting program.")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
