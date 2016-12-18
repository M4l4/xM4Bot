import requests
from chat_actions import ban, unban
from time import sleep
import json


def btk():
    r = requests.get('https://tmi.twitch.tv/group/user/pandahusky1/chatters')
    r_binary = r.content
    r_json = json.loads(r_binary.decode())
    users = r_json['chatters']['viewers']
    banned = []
    for u in users:
        if not u == "franniechann":
            ban(u)
            banned.append(u)
    sleep(15)
    for u in banned:
        if not u == "franniechann":
            unban(u)

if __name__ == "__main__":
    btk()
