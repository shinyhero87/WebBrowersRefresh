from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import winsound

# Set the URL you want to refresh
url = "https://www.example.com/"

# Set the refresh interval in seconds
refresh_interval = 900  # 15 minutes in seconds

# Play a beep sound to indicate that the page has been refreshed
def play_sound():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)

# Open a new window and navigate to the web page
driver = webdriver.Chrome()
driver.execute_script("window.open('" + url + "', '_blank');")
driver.switch_to.window(driver.window_handles[-1])

# Main loop that refreshes the page and displays it
while True:
    # Wait for the refresh interval
    time.sleep(refresh_interval)
    
    # Refresh the page
    driver.refresh()
    
    # Play the sound to indicate that the page has been refreshed
    play_sound()

    # Switch to the new window and display the refreshed page
    driver.switch_to.window(driver.window_handles[-1])
    driver.find_element_by_tag_name('body').send_keys(Keys.F5)
