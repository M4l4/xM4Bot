import requests
import datetime
import dateutil.parser
from chat_actions import chat


def uptime():
    headers = {'Client-ID': '63cvsgl9w0qifcraewi42gdz2kylqs'}
    r = requests.get('https://api.twitch.tv/kraken/streams/pandahusky1', headers=headers)
    try:
        a = dateutil.parser.parse(r.json()['stream']['created_at'])
    except TypeError:
        chat("Stream is not live.")
    else:
        b = dateutil.parser.parse(datetime.datetime.utcnow().isoformat()+"Z")
        c = str(b-a).split(":")
        c[2] = c[2][:2]
        chat('Uptime: {0[0]} hours {0[1]} minutes {0[2]} seconds'.format(c))
