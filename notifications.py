import os
import time
from datetime import datetime

def get_notifications():
    result = os.popen('termux-notification-list').read()
    return result

def write_notifications_to_file(file_path, notifications):
    with open(file_path, 'a') as file:
        file.write(f"--- {datetime.now()} ---\n")
        file.write(notifications + "\n\n")

file_path = "notifications.txt"

while True:
    notifications = get_notifications()
    if notifications:
        write_notifications_to_file(file_path, notifications)
    time.sleep(300)  # Пауза 5 минут
