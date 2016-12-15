import re
from time import sleep
import functions as f
from chat_actions import chat
from config import CHAT_MSG, RATE
from connect import connected, s


def process_message(user, msg):
    if msg == "!up":
        f.uptime()
    if msg[:2] == "!a":
        f.assist(msg[3:])
    if not user == "xm4bot" and msg == "Ogod. Here we go, taking all the kills then doing" \
                                       " nothing but dw \"he\'ll carry\"":
        chat(msg)


def main_loop():
    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response)[:-2]
            print(username + ": " + message)
            process_message(username, message)
        sleep(1 / RATE)

if __name__ == "__main__":
    main_loop()
