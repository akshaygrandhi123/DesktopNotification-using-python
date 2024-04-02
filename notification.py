from plyer import notification
import time


if __name__ == '__main__':
    while True:
        notification.notify(
            title = " Take a Break ⏳",
            message = " Play some games chill your mind ",
            app_icon = "C:/Users/MY PC/OneDrive/Documents/Codes/Python/try.ico",
            timeout = 5)
        time.sleep(3600)
