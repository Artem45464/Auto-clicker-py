from pynput.mouse import Button, Controller
import time
import threading
import keyboard

# Define global variables
mouse_controller = Controller()
running_event = False  # Track whether auto-clicking is currently running
click_thread = None  # This will hold the click thread

# Function for auto-clicking logic, ensuring 20 CPS
def auto_click(target_cps=20):
    interval = 1 / target_cps  # Calculate target interval (0.05 seconds)
    while running_event:  # Continue clicking while it's set to True
        start_time = time.perf_counter()  # Track time before click
        mouse_controller.click(Button.left, 1)  # Perform the click
        end_time = time.perf_counter()  # Track time after click
        click_duration = end_time - start_time  # Calculate click duration
        remaining_time = interval - click_duration  # Calculate time remaining for the target interval
        # Sleep the remaining time to keep interval as close to 0.05 as possible
        if remaining_time > 0:
            time.sleep(remaining_time)

# Start clicking
def start_click(target_cps=20):
    global running_event, click_thread
    if not running_event:  # If not already running, start clicking
        running_event = True
        print(f"Auto-clicker started with {target_cps} clicks per second.")
        click_thread = threading.Thread(target=auto_click, args=(target_cps,), daemon=True)
        click_thread.start()  # Start the auto-clicking in a separate thread

# Stop clicking
def stop_click():
    global running_event
    if running_event:  # If the clicker is running, stop it
        running_event = False
        print("Auto-clicker stopped.")
        if click_thread:
            click_thread.join()  # Wait for the clicking thread to finish

# Main function for user control
def main():
    print("Press 'k' to start/stop auto-clicking.")
    print("Press 'q' to exit the program.")
    
    key_state_k = False  # To track whether 'k' has been pressed
    try:
        while True:
            # Check for 'k' key press to toggle clicking
            if keyboard.is_pressed('k'):  # Press 'k' to toggle start/stop clicking
                if not key_state_k:  # This ensures toggling works only once per press
                    if running_event:
                        stop_click()  # If running, stop the clicking
                    else:
                        start_click()  # If not running, start the clicking
                    key_state_k = True  # Mark that 'k' was pressed
                time.sleep(0.2)  # Small delay to ensure no multiple detections

            # Reset state when 'k' is released
            if not keyboard.is_pressed('k'):
                key_state_k = False

            # Exit the program when 'q' is pressed
            if keyboard.is_pressed('q'):  # Press 'q' to exit the program
                stop_click()  # Stop the auto-clicking before exiting
                print("Exiting program.")
                break  # Break out of the loop and terminate the program

            time.sleep(0.1)  # Small delay to prevent CPU overload

    except KeyboardInterrupt:
        stop_click()
        print("Program interrupted by user.")

# Run the program
if __name__ == "__main__":
    main()
