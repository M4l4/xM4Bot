from config import CHAN, TESTING
from connect import s as socket


def chat(msg):
    """
    Send a chat message to the server.
    Keyword arguments:
    msg  -- the message to be sent
    """
    socket.send("PRIVMSG {} :{}\r\n".format(CHAN, msg).encode("utf-8"))
    if TESTING:
        socket.send("PRIVMSG {} :{}\r\n".format(CHAN, '/clear').encode("utf-8"))


def ban(user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    user -- the user to be banned
    """
    chat(".ban {}".format(user))


def unban(user):
    """
    Ban a user from the current channel.
    Keyword arguments:
    user -- the user to be banned
    """
    chat(".unban {}".format(user))


def timeout(user, secs=600):
    """
    Time out a user for a set period of time.
    Keyword arguments:
    user -- the user to be timed out
    secs -- the length of the timeout in seconds (default 600)
    """
    chat(".timeout {} {}".format(user, secs))
