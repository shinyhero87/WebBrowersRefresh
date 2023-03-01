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

# Function to update the timer label


def update_timer_label():
    while timer_running:
        timer_label.config(text="Refresh in: " +
                           time.strftime("%M:%S", time.gmtime(time_left)))
        time.sleep(1)
        if time_left <= 0:
            break
        else:
            time_left -= 1
    timer_label.config(text="Refresh in: --:--")


# Main loop that refreshes the page and plays the sound
while True:
    # Open the web page
    webbrowser.open(url, new=0, autoraise=True)

    # Start the timer thread
    timer_running = True
    time_left = refresh_interval
    timer_thread = threading.Thread(target=update_timer_label)
    timer_thread.start()

    # Wait for the refresh interval
    time.sleep(refresh_interval)
    timer_running = False

    # Refresh the page
    webbrowser.refresh()

    # Play the sound to indicate that the page has been refreshed
    play_sound()

# Create the timer window
timer_window = tk.Tk()
timer_window.title("Page Refresh Timer")

# Create the timer label
timer_label = tk.Label(
    timer_window, text="Refresh in: --:--", font=("Arial", 16))
timer_label.pack()

# Start the main loop of the timer window
timer_window.mainloop()
