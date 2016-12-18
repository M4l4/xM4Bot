from chat_actions import timeout
from multiprocessing import Process
from time import sleep
from functions import global_vars as gv


def spank(user):
    if user in gv.spanking:
        gv.spanking.pop(user).terminate()
    else:
        gv.spanking[user] = Process(target=hit, args=(user,))
        gv.spanking[user].start()


def hit(user):
    while True:
        timeout(user, 5)
        sleep(10)
