import webbrowser
import time
import winsound

# Set the URL you want to refresh
url = "https://my.wgu.edu/degree-plan"

# Set the refresh interval in seconds
refresh_interval = 900  # 15 minutes in seconds

# Play a beep sound to indicate that the page has been refreshed
def play_sound():
    frequency = 2500  # Set the frequency of the beep sound
    duration = 1000  # Set the duration of the beep sound in milliseconds
    winsound.Beep(frequency, duration)

# Main loop that refreshes the page and plays the sound
while True:
    # Open the web page
    webbrowser.open(url, new=0, autoraise=True)
    
    # Wait for the refresh interval
    time.sleep(refresh_interval)
    
    # Refresh the page
    webbrowser.refresh()
    
    # Play the sound to indicate that the page has been refreshed
    play_sound()
