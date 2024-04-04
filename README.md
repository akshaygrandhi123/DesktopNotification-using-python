# Break Reminder

This is a simple Python script that sends a desktop notification to remind you to take a break and play some games or relax your mind. The notification appears every hour (3600 seconds).

## Prerequisites

Before running the script, you'll need to have Python installed on your system. You can download the latest version of Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Additionally, you'll need to install the `plyer` library, which is used for generating desktop notifications.

## Installation

1. Open your terminal or command prompt.

2. Install the `plyer` library using pip (Python's package installer):

```
pip install plyer
```

If you encounter any issues during the installation process, make sure you have the latest version of pip installed. You can upgrade pip by running:

```
python -m pip install --upgrade pip
```

## Usage

1. Save the script to a file with a `.py` extension, e.g., `break_reminder.py`.

2. Open the script file and modify the `app_icon` parameter to the path of your desired icon file (optional).

```python
app_icon = "path/to/your/icon.ico"
```

3. Run the script from the terminal or command prompt:

```
python break_reminder.py
```

The script will run indefinitely, displaying a notification every hour to remind you to take a break.

## Customization

You can customize the notification by modifying the following parameters in the `notification.notify()` function:

- `title`: The title of the notification.
- `message`: The message body of the notification.
- `app_icon`: The path to the icon file that will be displayed with the notification.
- `timeout`: The duration (in seconds) for which the notification will be displayed.

## Note

- Make sure to replace `"C:/Users/MY PC/OneDrive/Documents/Codes/Python/try.ico"` with the actual path to your desired icon file.
- The script will continue to run until you manually stop it (e.g., by closing the terminal or command prompt window).

## License

This project is licensed under the [MIT License](LICENSE).
```
