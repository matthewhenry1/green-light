import pyautogui
import random
from threading import Timer
import os

# Close Slack
def close():
    os.system("osascript -e 'quit app \"/Applications/Slack.app\"'")
    stop = 1

# Timer
t = Timer(4500.0, close)
t.start()

# Move Mouse
while 1 < 2:
    x = random.randint(600, 800)
    y = random.randint(600, 800)
    pyautogui.moveTo(x,y,duration=1)
