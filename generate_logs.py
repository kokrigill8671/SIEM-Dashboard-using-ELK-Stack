import random
import time

messages = [
    "Failed password for root from 192.168.1.10",
    "Accepted password for admin from 192.168.1.20",
    "Invalid user guest from 192.168.1.30",
    "Connection closed by 192.168.1.40",
]

while True:
    with open("../sample_logs/auth.log", "a") as f:
        f.write(random.choice(messages) + "\n")
    print("Log Generated")
    time.sleep(5)