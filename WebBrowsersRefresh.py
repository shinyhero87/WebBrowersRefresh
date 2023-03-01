import webbrowser
import time
import winsound
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

# Update the timer label


def update_timer_label():
    global time_left
    time_left -= 1
    if time_left >= 0:
        timer_label.config(text="Refresh in: " +
                           time.strftime('%M:%S', time.gmtime(time_left)))
        timer_label.after(1000, update_timer_label)
    else:
        timer_label.config(text="Refreshing...")
        refresh()

# Refresh the web page


def refresh():
    webbrowser.open(url, new=0, autoraise=True)
    play_sound()
    global time_left
    time_left = refresh_interval
    timer_label.after(0, update_timer_label)


# Check if the appropriate drivers are installed
driver_installed = True  # Assume the driver is installed
# Add your code here to check if the driver is installed
# Set driver_installed to False if the driver is not installed

# If the driver is not installed, display a prompt to install the driver
if not driver_installed:
    install_driver = tk.messagebox.askyesno("Driver not installed",
                                            "The appropriate drivers are not installed. Would you like to install them?")
    if install_driver:
        # Add your code here to install the driver
        pass
    else:
        exit()

# Create the Tkinter GUI
root = tk.Tk()
root.title("Web Page Refresh")

# Create the timer label
time_left = refresh_interval
timer_label = tk.Label(root, text="Refresh in: " +
                       time.strftime('%M:%S', time.gmtime(time_left)))
timer_label.pack()

# Create the refresh button
refresh_button = tk.Button(root, text="Refresh", command=refresh)
refresh_button.pack()

# Start the GUI main loop
root.mainloop()
