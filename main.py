from plyer import notification
import time


def notify_me(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "./images/icon.ico",
        timeout = 5,
    )


while True:
    notify_me("Hassan, Take a break!", "Look at something else for a while")
    time.sleep(1200)