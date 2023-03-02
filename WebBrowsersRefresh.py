import webbrowser
import time
import winsound
import threading
import tkinter as tk

# Set the URL you want to refresh
url = "https://my.wgu.edu/degree-plan"

# Set the refresh interval in seconds
refresh_interval = 60  # 1 minute in seconds

# Play a beep sound to indicate that the page has been refreshed


def play_sound():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)


# Check if appropriate drivers are installed, if not, display prompt window with options of yes or no to install these drivers
driver_installed = True  # Assume the driver is installed by default

# Try to import the appropriate driver
try:
    import chromedriver_autoinstaller
except ImportError:
    driver_installed = False

# If the driver is not installed, display a prompt to ask the user if they want to install it
if not driver_installed:
    response = input(
        "The appropriate driver is not installed. Do you want to install it now? (y/n)")
    if response.lower() == "y":
        chromedriver_autoinstaller.install()  # Install the appropriate driver

# Open the web page
browser = webbrowser.get()
if browser:
    browser.open_new_tab(url)

# Create a timer label
root = tk.Tk()
timer_label = tk.Label(root, text="")
timer_label.pack()

# Function to update the timer label every second


def update_timer_label():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text="Refresh in: " +
                           time.strftime('%M:%S', time.gmtime(time_left)))
    else:
        # Refresh the page
        browser.reload()
        # Play the sound to indicate that the page has been refreshed
        play_sound()
        # Reset the timer
        time_left = refresh_interval
    # Schedule the function to run again after 1 second
    timer_label.after(1000, update_timer_label)


# Start the timer
time_left = refresh_interval
update_timer_label()

# Run the main event loop
root.mainloop()
