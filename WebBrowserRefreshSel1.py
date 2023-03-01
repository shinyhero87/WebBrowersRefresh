from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import tkinter as tk
import time
import winsound
import os
import sys
import urllib.request
import zipfile

# Set the URL you want to refresh
url = "https://www.example.com/"

# Set the refresh interval in seconds
refresh_interval = 900  # 15 minutes in seconds

# Set the font for the timer
font = ("Helvetica", 20)

# Play a beep sound to indicate that the page has been refreshed
def play_sound():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)

# Open a new window and navigate to the web page
driver = None
try:
    driver = webdriver.Chrome()
except Exception as e:
    print(f"Error: {e}")
    root = tk.Tk()
    root.title("Chrome Driver not found")
    tk.Label(root, text="Chrome driver not found. Do you want to download and install the driver?").pack()
    tk.Button(root, text="Yes", command=lambda: install_chromedriver(root)).pack(side=tk.LEFT, padx=10)
    tk.Button(root, text="No", command=root.destroy).pack(side=tk.RIGHT, padx=10)
    root.mainloop()
    sys.exit(1)

driver.execute_script("window.open('" + url + "', '_blank');")
driver.switch_to.window(driver.window_handles[-1])

# Create a new Tkinter window and label for the timer
root = tk.Tk()
timer_label = tk.Label(root, text="", font=font)
timer_label.pack()

# Update the timer label with the remaining time until the next refresh
def update_timer_label(remaining_time):
    timer_label.config(text="Next refresh in " + str(remaining_time) + " seconds")

# Install Chrome driver if selected
def install_chromedriver(root):
    try:
        os_type = sys.platform
        if os_type == 'win32':
            url = 'https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_win32.zip'
        elif os_type == 'linux':
            url = 'https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip'
        elif os_type == 'darwin':
            url = 'https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_mac64.zip'
        else:
            raise Exception("Unsupported OS")

        # Download and extract the Chrome driver
        urllib.request.urlretrieve(url, 'chromedriver.zip')
        with zipfile.ZipFile('chromedriver.zip', 'r') as zip_ref:
            zip_ref.extractall('.')

        # Add the extracted Chrome driver to the system path
        os_type = sys.platform
        if os_type == 'win32':
            os.environ["PATH"] += os.pathsep + os.getcwd() + os.pathsep + os.path.join(os.getcwd(), "chromedriver")
        else:
            os.environ["PATH"] += os.pathsep + os.path.join(os.getcwd(), "chromedriver")
        
        # Close the dialog box and restart the script
        root.destroy()
        os.execl(sys.executable
