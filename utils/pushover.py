import requests 
import logging
from utils.utils import pushovertoken, Pushoverkey

def send_pushover(title, message, priority=0):
    try:
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data={
                "token": pushovertoken,
                "user": Pushoverkey,
                "title": title,
                "message": message,
                "priority": priority
            }
        )
    except Exception as e:
        print("Pushover error:", e)