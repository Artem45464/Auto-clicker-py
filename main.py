from pynput.mouse import Button, Controller
import time
import threading

# Define global variables
running = False
mouse_controller = Controller()

# Function for auto-clicking logic, ensuring 20 CPS
def auto_click(target_cps=20):  # Target CPS = 20
    interval = 1 / target_cps  # Calculate target interval (0.05 seconds)
    while running:
        start_time = time.perf_counter()  # Track time before click
        mouse_controller.click(Button.left, 1)  # Perform the click
        end_time = time.perf_counter()  # Track time after click
        click_duration = end_time - start_time  # Calculate click duration
        remaining_time = interval - click_duration  # Calculate time remaining for the target interval
        # Sleep the remaining time to keep interval as close to 0.05 as possible
        if remaining_time > 0:
            time.sleep(remaining_time)

# Start clicking
def start_click(target_cps=20):  # Start at 20 CPS
    global running
    if not running:
        running = True
        print(f"Auto-clicker started with {target_cps} clicks per second.")
        threading.Thread(target=auto_click, args=(target_cps,)).start()

# Stop clicking
def stop_click():
    global running
    running = False
    print("Auto-clicker stopped.")

# Main function for user control
def main():
    print("Auto-Clicker Controls:")
    print("1. Type 'start' to begin auto-clicking.")
    print("2. Type 'stop' to stop auto-clicking.")
    print("3. Type 'quit' to exit the program.")
    
    try:
        while True:
            command = input("Enter a command: ").strip().lower()

            if command == 'start':
                start_click(target_cps=20)  # Start clicking at 20 CPS
            elif command == 'stop':
                stop_click()
            elif command == 'quit':
                print("Exiting the program.")
                stop_click()
                break
            else:
                print("Invalid command! Please type 'start', 'stop', or 'quit'.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        stop_click()

# Run the program
if __name__ == "__main__":
    main()
