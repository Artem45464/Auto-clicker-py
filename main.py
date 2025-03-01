import time
import threading
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
auto_clicking = threading.Event()

def auto_click():
    """Continuously clicks at 20 CPS until stopped, with accurate timing."""
    target_cps = 20  # Target CPS is now 20
    interval = 1 / target_cps  # Interval per click
    next_time = time.perf_counter() + interval  # Track precise timing
    
    while auto_clicking.is_set():
        next_time += interval
        sleep_time = max(0, next_time - time.perf_counter())

        if not auto_clicking.is_set():  # Ensure instant stopping
            break

        mouse.click(Button.left, 1)
        time.sleep(sleep_time)  # Maintain exact CPS

def toggle_auto_clicking():
    """Toggle auto-clicking state."""
    if auto_clicking.is_set():
        stop_auto_clicking()
    else:
        start_auto_clicking()

def start_auto_clicking():
    """Start auto-clicking in a separate thread."""
    if not auto_clicking.is_set():
        auto_clicking.set()
        threading.Thread(target=auto_click, daemon=True).start()
        print("Auto-clicker started.")

def stop_auto_clicking():
    """Stop auto-clicking."""
    auto_clicking.clear()
    print("Auto-clicker stopped.")

def main():
    """Monitor keypresses."""
    print("Press 'k' to start/stop the auto-clicker.")
    print("Press 'q' to exit the program.")
    
    while True:
        if keyboard.is_pressed('k'):  # Start/stop the auto-clicker with 'k'
            toggle_auto_clicking()
            while keyboard.is_pressed('k'):  # Wait for key release to prevent multiple toggles
                time.sleep(0.05)

        if keyboard.is_pressed('q'):  # Exit the program with 'q'
            stop_auto_clicking()
            print("Exiting program.")
            break
        
        time.sleep(0.1)  # Polling interval for key press detection

if __name__ == "__main__":
    main()
