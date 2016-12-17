import re
from time import sleep, localtime
from config import CHAT_MSG, RATE, TESTING
from connect import connected, s
from chat_actions import chat
import functions as f


def process_message(user, msg):
    if msg == "!up":
        f.uptime()
    if msg[:2] == "!a":
        f.assist(msg[3:])
    if msg in {"!Ogod", "!ogod"}:
        chat("Can't have fun in this stream FeelsBadMan")
    if msg == "!seen":
        f.a_main()


def main_loop():
    while connected:
        response = s.recv(1024).decode("utf-8")
        if response == "PING :tmi.twitch.tv\r\n":
            s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
        else:
            username = re.search(r"\w+", response).group(0)
            message = CHAT_MSG.sub("", response).rstrip()
            print("[{0[3]}:{0[4]}] {1}: {2}".format(localtime(), username, message))
            process_message(username, message)
        sleep(1 / RATE)

if __name__ == "__main__":
    main_loop()
