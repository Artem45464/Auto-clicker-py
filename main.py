from pynput.mouse import Controller, Button
import threading
import time

# Define how many clicks per second (CPS) you want
clicks_per_second = 100  # Can increase up to higher CPS

# Calculate the interval between clicks
click_speed = 1 / clicks_per_second  # Time between clicks in seconds

# Create a controller object for simulating mouse actions
mouse_controller = Controller()

# Function to perform the clicks
def clicker():
    while True:
        mouse_controller.click(Button.left)  # Simulate left click
        time.sleep(click_speed)  # Wait time between clicks to control CPS

# Start the clicking in a separate thread to run continuously
click_thread = threading.Thread(target=clicker)
click_thread.daemon = True  # Exit automatically when the program ends
click_thread.start()

print(f"Auto-clicker started at {clicks_per_second} clicks per second.")

# Keeps the program running (do your own tasks)
input("Press Enter to stop the clicking.")
