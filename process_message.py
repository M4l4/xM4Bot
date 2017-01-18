#!/home/malachitemiller/opt/python-3.5.0/bin/python3
import re
from time import sleep, localtime
from config import CHAT_MSG, RATE, TESTING
from connect import connected, s
from chat_actions import chat
from functions.global_vars import users
import functions as f


def process_message(user, msg):
    chatted = False
    if msg == "!up":
        f.uptime()
        chatted = True
    if msg.startswith("!a "):
        f.assist(msg[3:])
        chatted = True
    if msg.endswith("and now has 0 pandapoints"):
        f.no_points()
        chatted = True
    if msg in ["!Ogod", "!ogod"]:
        chat("Can't have fun in this stream FeelsBadMan")
        chatted = True
    if msg == "!test":
        chat("http://www.ricepuritytest.com/")
        chatted = True
    if msg == "!seen":
        f.a_main()
        chatted = True
    if msg == "!sudoku":
        f.sudoku(user)
        chatted = True
    if msg == "!followage":
        f.follow_age(user)
        chatted = True
    if user in users['parents'] and msg == "!btk":
        f.btk()
        chatted = True
    if user == "cancerious_teeto" and msg.startswith("!gamble "):
        f.teeto()
        chatted = True
    if user == "xm4l4x" and msg == "!die":
        raise SystemExit
    return chatted


def main_loop():
    chat("Hi! I'm alive :D")
    try:
        while connected:
            chatted = False
            response = s.recv(1024).decode("utf-8")
            if response == "PING :tmi.twitch.tv\r\n":
                s.send("PONG :tmi.twitch.tv\r\n".encode("utf-8"))
            else:
                username = re.search(r"\w+", response).group(0)
                message = CHAT_MSG.sub("", response).rstrip()
                chatted = process_message(username, message)
            if chatted:
                sleep(1 / RATE)
        else:
            raise SystemExit
    except Exception as e:
        from chat_actions import chat
        chat("I am dieing. Please tell M4. :(")

if __name__ == "__main__":
    main_loop()
