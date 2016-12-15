from chat_actions import chat
from functions import global_vars as gv


def assist(msg):
    if msg == "clear":
        gv.count = 0
        chat("Assists set to 0")
    elif len(msg):
        try:
            gv.count += int(msg)
            chat("Assists: {}".format(gv.count))
        except ValueError:
            chat("Usage: !a; !a x, where x is an integer; !a clear")
    else:
        gv.count += 1
        chat("Assists: {}".format(gv.count))
