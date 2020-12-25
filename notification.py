import time
from plyer import notification
while True:
    notification.notify(
        title = "Take a Break",
        message = "Sir Please take a Break .You are continuously working on PC for 45 minutes",
        app_icon="C:\\data D\\Shivam\\pc.ico",
        timeout = 5
        )
    
    time.sleep(60*45)
