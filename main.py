import time
import threading
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
auto_clicking = False

def auto_click():
    """Continuously clicks at 20 CPS until stopped, adjusting dynamically."""
    global auto_clicking
    target_cps = 20  # Target CPS is now 20
    interval = 1 / target_cps  # Interval per click
    correction = 0  # Adjustment factor

    while auto_clicking:
        start_time = time.perf_counter()  # Capture time right before click
        mouse.click(Button.left, 1)
        elapsed = time.perf_counter() - start_time
        
        # Adjust for delays dynamically
        time.sleep(max(0, interval - elapsed - correction))
        
        # Recalculate correction factor
        actual_elapsed = time.perf_counter() - start_time
        correction = (actual_elapsed - interval) * 0.1  # Smooth correction

def toggle_auto_clicking():
    """Toggle auto-clicking state."""
    global auto_clicking
    if auto_clicking:
        stop_auto_clicking()
    else:
        start_auto_clicking()

def start_auto_clicking():
    """Start auto-clicking in a separate thread."""
    global auto_clicking
    if not auto_clicking:
        auto_clicking = True
        threading.Thread(target=auto_click, daemon=True).start()
        print("Auto-clicker started.")

def stop_auto_clicking():
    """Stop auto-clicking."""
    global auto_clicking
    auto_clicking = False
    print("Auto-clicker stopped.")

def exit_program():
    """Exit the program safely."""
    stop_auto_clicking()
    print("Exiting program.")
    exit(0)

def main():
    """Monitor keypresses."""
    print("Press 'k' to start/stop the auto-clicker.")
    print("Press 'q' to exit the program.")

    keyboard.add_hotkey('k', toggle_auto_clicking)
    keyboard.add_hotkey('q', exit_program)

    keyboard.wait()  # Keep the script running

if __name__ == "__main__":
    main()
