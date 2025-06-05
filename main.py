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
    start_time = time.perf_counter()
    click_count = 0
    
    while auto_clicking.is_set():
        current_time = time.perf_counter()
        # Reset timing if we've fallen too far behind
        if current_time - start_time > interval * click_count + interval * 5:
            start_time = current_time
            click_count = 0
            
        mouse.click(Button.left, 1)
        click_count += 1
        next_time = start_time + (click_count * interval)
        sleep_time = max(0, next_time - time.perf_counter())
        time.sleep(sleep_time)

def toggle_auto_clicking():
    """Toggle auto-clicking state."""
    # Use threading.Lock to prevent race conditions
    with print_lock:
        if auto_clicking.is_set():
            stop_auto_clicking()
        else:
            start_auto_clicking()

def start_auto_clicking():
    """Start auto-clicking in a separate thread if not already running."""
    # No need for the if check since we're using a lock in toggle_auto_clicking
    auto_clicking.set()
    thread = threading.Thread(target=auto_click, daemon=True)
    thread.start()
    print("Auto-clicker started.", flush=True)

def stop_auto_clicking():
    """Stop auto-clicking."""
    auto_clicking.clear()
    print("Auto-clicker stopped.", flush=True)

def main():
    """Monitor keypresses."""
    with print_lock:
        print("Press 'k' to start/stop the auto-clicker.")
        print("Press 'q' to exit the program.")
    
    # Register hotkey
    keyboard.on_press_key("k", lambda e: toggle_auto_clicking())
    
    try:
        keyboard.wait('q')  # Wait for 'q' to be pressed to exit
    finally:
        with print_lock:
            stop_auto_clicking()
            # Clean up keyboard hooks
            keyboard.unhook_all()
            print("Exiting program.", flush=True)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        with print_lock:
            stop_auto_clicking()
            keyboard.unhook_all()
            print("\nProgram interrupted. Exiting...")
