import pyautogui
import random
from threading import Timer
import os

# Class to determine if the
class Running(object):

    def __init__(self):
        self.active = True

    def getActive(self):
        return self.active

    def setActive(self, active):
        self.active = active

# Close Slack
def close():
    os.system("osascript -e 'quit app \"/Applications/Slack.app\"'")
    running.setActive(False)

# Execute Timer
t = Timer(3.0, close)
t.start()

# Class for get and set of active application
running = Running()

# Move Mouse
while running.getActive():
    x = random.randint(800, 1000)
    y = random.randint(800, 1000)
    pyautogui.moveTo(x,y,duration=1)
