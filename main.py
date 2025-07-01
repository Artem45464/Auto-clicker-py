import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener, KeyCode
import sys

mouse = MouseController()
auto_clicking = threading.Event()
print_lock = threading.Lock()  # Ensure thread-safe prints
click_thread = None
keyboard_listener = None

def auto_click():
    """Continuously clicks at exactly 20 CPS until stopped, with accurate timing."""
    target_cps = 20.0
    interval = 1 / target_cps
    next_click_time = time.time()
    while auto_clicking.is_set():
        current_time = time.time()
        if current_time >= next_click_time:
            mouse.click(Button.left, 1)
            next_click_time += interval
            if current_time > next_click_time + interval * 5:
                next_click_time = current_time + interval
        time.sleep(0.001)

def toggle_auto_clicking():
    """Toggle auto-clicking state."""
    with print_lock:
        if auto_clicking.is_set():
            stop_auto_clicking()
        else:
            start_auto_clicking()

def start_auto_clicking():
    """Start auto-clicking in a separate thread if not already running."""
    global click_thread
    if not auto_clicking.is_set():
        auto_clicking.set()
        click_thread = threading.Thread(target=auto_click, daemon=True)
        click_thread.start()
        print("Auto-clicker started.", flush=True)

def stop_auto_clicking():
    """Stop auto-clicking."""
    if auto_clicking.is_set():
        auto_clicking.clear()
        print("Auto-clicker stopped.", flush=True)

def on_press(key):
    """Handle key press events."""
    try:
        if key == KeyCode.from_char('k'):
            toggle_auto_clicking()
        elif key == KeyCode.from_char('q'):
            return False  # Stop listener
    except AttributeError:
        pass
    return True

def main():
    """Monitor keypresses using pynput instead of keyboard library."""
    global keyboard_listener
    with print_lock:
        print("Press 'k' to start/stop the auto-clicker.")
        print("Press 'q' to exit the program.")
    try:
        keyboard_listener = Listener(on_press=on_press)
        keyboard_listener.start()
        keyboard_listener.join()
    except Exception as e:
        with print_lock:
            print(f"\nError starting keyboard listener: {e}", flush=True)
        raise
    finally:
        cleanup()

def cleanup():
    with print_lock:
        stop_auto_clicking()
        if keyboard_listener and hasattr(keyboard_listener, "running") and keyboard_listener.running:
            keyboard_listener.stop()
        print("Exiting program.", flush=True)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        cleanup()
        with print_lock:
            print(f"\nError: {e}", flush=True)
        sys.exit(1)
