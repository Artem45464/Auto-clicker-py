import pyautogui
import time
import threading

# Define global variables
running = False  # Keeps track of the auto-clicker state
thread = None  # Thread for the clicker

# Function for auto-clicking logic
def auto_click(interval):
    while running:
        pyautogui.click()
        time.sleep(interval)

# Start clicking
def start_click(interval=0.0001):  # Reduced to 0.0001 for ultra-fast clicking
    global running, thread
    if not running:  # Prevent multiple threads
        running = True
        thread = threading.Thread(target=auto_click, args=(interval,))
        thread.start()
        print(f"Auto-clicker started with {interval} second interval.")

# Stop clicking
def stop_click():
    global running, thread
    running = False
    if thread is not None:
        thread.join()
        thread = None
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
                start_click(interval=0.0001)  # Clicking interval for ultra-fast clicks
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
        stop_click()  # Ensure it stops on exit

# Run the program
if __name__ == "__main__":
    main()
