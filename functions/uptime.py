from twitch_api import call_twitch_api
import datetime
import dateutil.parser
from chat_actions import chat


def uptime():
    r = call_twitch_api('https://api.twitch.tv/kraken/streams/pandahusky1')
    try:
        a = dateutil.parser.parse(r['stream']['created_at'])
        b = dateutil.parser.parse(datetime.datetime.utcnow().isoformat()+"Z")
        c = str(b-a).split(":")
        c[2] = c[2][:2]
        chat('Uptime: {0[0]} hours {0[1]} minutes {0[2]} seconds'.format(c))
    except TypeError:
        chat("Stream is not live.")
