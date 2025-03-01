import time
import threading
from pynput.mouse import Button, Controller
import keyboard

mouse = Controller()
auto_clicking = threading.Event()
print_lock = threading.Lock()  # Ensure thread-safe prints

def auto_click():
    """Continuously clicks at 20 CPS until stopped, with accurate timing."""
    target_cps = 20  
    interval = 1 / target_cps  
    next_time = time.perf_counter()

    while auto_clicking.is_set():
        mouse.click(Button.left, 1)
        next_time += interval
        sleep_time = max(0, next_time - time.perf_counter())
        time.sleep(sleep_time)

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
        with print_lock:
            print("Auto-clicker started.", flush=True)

def stop_auto_clicking():
    """Stop auto-clicking."""
    auto_clicking.clear()
    with print_lock:
        print("Auto-clicker stopped.", flush=True)

def main():
    """Monitor keypresses."""
    with print_lock:
        print("Press 'k' to start/stop the auto-clicker.")
        print("Press 'q' to exit the program.")

    while True:
        keyboard.wait('k')
        toggle_auto_clicking()
        time.sleep(0.1)  # Prevent rapid toggling

        if keyboard.is_pressed('q'):  # Exit the program with 'q'
            stop_auto_clicking()
            with print_lock:
                print("Exiting program.", flush=True)
            break

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        stop_auto_clicking()
        print("\nProgram interrupted. Exiting...")
