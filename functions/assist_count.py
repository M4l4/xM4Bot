from chat_actions import chat
from functions import global_vars as gv


def assist(stat, msg):
    msg = msg.strip()
    stats = {"k": "Kills", "d": "Deaths", "a": "Assists"}
    if msg == "clear":
        gv.counts[stat] = 0
        chat(stats[stat] + " set to 0")
    elif msg == "clear all":
        for count in gv.counts:
            gv.counts[count] = 0
        chat("All stats set to 0")
    elif len(msg):
        try:
            gv.counts[stat] += int(msg)
            chat(stats[stat] + ": {}".format(gv.counts[stat]))
        except ValueError:
            chat("Usage: !{0}; !{0} x, where x is an integer; !{0} clear".format(stat))
    else:
        gv.counts[stat] += 1
        chat(stats[stat] + ": {}".format(gv.counts[stat]))
