import webbrowser
import time
import threading
import winsound
import tkinter as tk

# Set the URL you want to refresh
url = "https://my.wgu.edu/degree-plan"

# Set the refresh interval in seconds
refresh_interval = 60  # 1 minute

# Function to play a beep sound
def play_sound():
    frequency = 2500  # Hz
    duration = 500  # ms
    winsound.Beep(frequency, duration)

# Function to refresh the webpage
def refresh_page():
    webbrowser.open(url)  # Opens in a new tab
    play_sound()

# Function to update the timer label
def update_timer_label():
    global time_left
    if time_left > 0:
        time_left -= 1
        timer_label.config(text=f"Refresh in: {time_left} sec")
        root.after(1000, update_timer_label)
    else:
        refresh_page()
        time_left = refresh_interval
        update_timer_label()  # Restart the countdown

# Open the web page initially
webbrowser.open(url)

# GUI setup
root = tk.Tk()
root.title("Auto Refresher")

timer_label = tk.Label(root, text="Refresh in: 60 sec", font=("Arial", 14))
timer_label.pack()

# Start the timer
time_left = refresh_interval
update_timer_label()

# Run the GUI loop
root.mainloop()
