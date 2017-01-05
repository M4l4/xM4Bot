import requests
from config import TWITCH_API


def call_twitch_api(url):
    headers = {'Client-ID': TWITCH_API}
    r = requests.get(url, headers=headers)
    return r.json()


def get_display_name(user):
    r = call_twitch_api('https://api.twitch.tv/kraken/users/{}'.format(user))
    return r['display_name']

if __name__ == "__main__":
    assert get_display_name('xm4l4x') == 'xM4l4x'
