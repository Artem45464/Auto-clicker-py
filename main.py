import time
import threading
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Listener, KeyCode
import sys

class AutoClicker:
    """Thread-safe auto-clicker with precise timing control."""
    
    def __init__(self, cps=20):
        self.mouse = MouseController()
        self.target_cps = cps
        self.interval = 1.0 / cps
        
        self._clicking = threading.Event()
        self._stop_flag = threading.Event()
        self._click_thread = None
        self._click_lock = threading.Lock()
        self._print_lock = threading.Lock()
        self._running_lock = threading.Lock()
        self._is_running = False
        self._cleanup_done = False
        
        self.keyboard_listener = None
        
    def _auto_click(self):
        """Continuously clicks at target CPS until stopped, with accurate timing."""
        perf = time.perf_counter
        next_click_time = perf() + self.interval
        
        while self._clicking.is_set() and not self._stop_flag.is_set():
            current_time = perf()
            sleep_time = next_click_time - current_time
            
            if sleep_time > 0:
                # Only cap very small sleep times to prevent busy-waiting
                # For normal operations, sleep the full duration
                actual_sleep = max(sleep_time, 0.0001) if sleep_time < 0.001 else sleep_time
                
                # Check stop flag periodically during long sleeps
                if actual_sleep > 0.01:
                    chunks = int(actual_sleep / 0.01)
                    remainder = actual_sleep % 0.01
                    for _ in range(chunks):
                        if not self._clicking.is_set() or self._stop_flag.is_set():
                            return
                        time.sleep(0.01)
                    if remainder > 0:
                        time.sleep(remainder)
                else:
                    time.sleep(actual_sleep)
                continue
            
            # Perform click
            try:
                self.mouse.click(Button.left, 1)
            except Exception as e:
                self._safe_print(f"Click error: {e}")
                break
                
            next_click_time += self.interval
            
            # Resync if we've fallen too far behind
            if current_time - next_click_time > self.interval * 5:
                next_click_time = current_time + self.interval
    
    def _safe_print(self, message):
        """Thread-safe printing."""
        with self._print_lock:
            print(message, flush=True)
    
    def start(self):
        """Start auto-clicking in a separate thread if not already running."""
        with self._click_lock:
            if self._clicking.is_set():
                return False
            
            # Clean up any previous thread
            if self._click_thread is not None and self._click_thread.is_alive():
                self._clicking.clear()
                self._click_thread.join(timeout=max(2.0, self.interval * 3))
            
            self._clicking.set()
            self._click_thread = threading.Thread(
                target=self._auto_click, 
                daemon=True, 
                name="ClickerThread"
            )
            self._safe_print("Auto-clicker started.")
            self._click_thread.start()
            return True
    
    def stop(self):
        """Stop auto-clicking."""
        with self._click_lock:
            if not self._clicking.is_set():
                return False
            
            self._clicking.clear()
            self._safe_print("Auto-clicker stopped.")
            return True
    
    def toggle(self):
        """Toggle auto-clicking state."""
        if self._clicking.is_set():
            self.stop()
        else:
            self.start()
    
    def is_running(self):
        """Check if auto-clicker is currently running."""
        return self._clicking.is_set()
    
    def set_cps(self, cps):
        """Change the clicks per second rate."""
        if cps <= 0 or cps > 1000:
            self._safe_print(f"Invalid CPS: {cps}. Must be between 1-1000.")
            return False
        
        # Use the lock to prevent race conditions
        with self._click_lock:
            was_running = self._clicking.is_set()
            
            if was_running:
                self._clicking.clear()
                # Wait for thread to finish
                if self._click_thread is not None and self._click_thread.is_alive():
                    self._click_thread.join(timeout=max(2.0, self.interval * 3))
            
            # Update CPS
            self.target_cps = cps
            self.interval = 1.0 / cps
            self._safe_print(f"CPS set to {cps}")
            
            # Restart if it was running
            if was_running:
                self._clicking.set()
                self._click_thread = threading.Thread(
                    target=self._auto_click,
                    daemon=True,
                    name="ClickerThread"
                )
                self._click_thread.start()
        
        return True
    
    def _on_press(self, key):
        """Handle key press events."""
        try:
            char = key.char
        except AttributeError:
            return True
        
        if char == 'k':
            self.toggle()
        elif char == 'q':
            return False  # Stop listener
        elif char == '+' or char == '=':
            new_cps = min(self.target_cps + 5, 1000)
            self.set_cps(new_cps)
        elif char == '-' or char == '_':
            new_cps = max(self.target_cps - 5, 1)
            self.set_cps(new_cps)
        
        return True
    
    def run(self):
        """Start the keyboard listener and run the program."""
        # Prevent multiple simultaneous runs
        with self._running_lock:
            if self._is_running:
                self._safe_print("Program is already running!")
                return
            self._is_running = True
        
        self._safe_print("=" * 50)
        self._safe_print("Auto-Clicker Control Panel")
        self._safe_print("=" * 50)
        self._safe_print(f"Current CPS: {self.target_cps}")
        self._safe_print("")
        self._safe_print("Controls:")
        self._safe_print("  'k'     - Start/Stop auto-clicking")
        self._safe_print("  '+'/'=' - Increase CPS by 5")
        self._safe_print("  '-'/'_' - Decrease CPS by 5")
        self._safe_print("  'q'     - Exit program")
        self._safe_print("=" * 50)
        
        try:
            self.keyboard_listener = Listener(on_press=self._on_press)
            self.keyboard_listener.start()
            self.keyboard_listener.join()
        except KeyboardInterrupt:
            self._safe_print("\nInterrupted by user.")
        except Exception as e:
            self._safe_print(f"\nError: {e}")
            raise
        finally:
            self.cleanup()
            with self._running_lock:
                self._is_running = False
    
    def cleanup(self):
        """Clean up all resources."""
        with self._click_lock:
            # Prevent double cleanup - now thread-safe
            if self._cleanup_done:
                return
            self._cleanup_done = True
            self._stop_flag.set()  # Signal all threads to stop
            
            # Stop clicking
            if self._clicking.is_set():
                self._clicking.clear()
            
            if self._click_thread is not None and self._click_thread.is_alive():
                # Use dynamic timeout based on CPS
                timeout = max(3.0, self.interval * 5)
                self._click_thread.join(timeout=timeout)
        
        # Stop keyboard listener (outside lock to avoid potential deadlock)
        if self.keyboard_listener:
            try:
                self.keyboard_listener.stop()
            except Exception:
                pass
        
        self._safe_print("Program exited cleanly.")


def main():
    """Entry point for the auto-clicker application."""
    clicker = AutoClicker(cps=20)
    
    try:
        clicker.run()
    except Exception as e:
        print(f"\nFatal error: {e}", file=sys.stderr)
        clicker.cleanup()
        sys.exit(1)


if __name__ == "__main__":
    main()
