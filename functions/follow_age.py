from twitch_api import call_twitch_api, get_display_name
from config import CHAN
import datetime
import dateutil.parser
from chat_actions import chat


def follow_age(user):
    r = call_twitch_api('https://api.twitch.tv/kraken/users/{}/follows/channels/{}'.format(user, CHAN))
    display_name = get_display_name(user)
    try:
        a = dateutil.parser.parse(r['created_at'])
        b = dateutil.parser.parse(datetime.datetime.utcnow().isoformat() + "Z")
        c = b - a
        days = divmod(c.days, 7)
        weeks = divmod(days[0], 4)
        months = divmod(weeks[0], 12)
        years = months[0]
        if years:
            chat('{} has been following for {} years {} months {} weeks {} days'.format(display_name, years, months[1],
                                                                                        weeks[1], days[1]))
        elif months[1]:
            chat('{} has been following for {} months {} weeks {} days'.format(display_name, months[1], weeks[1],
                                                                               days[1]))
        elif weeks[1]:
            chat('{} has been following for {} weeks {} days'.format(display_name, weeks[1], days[1]))
        elif days[1]:
            chat('{} has been following for {} days'.format(display_name, days[1]))
        else:
            chat('{} started following today!'.format(display_name))
    except KeyError:
        chat('{} is not following'.format(display_name))

if __name__ == "__main__":
    print(follow_age('xm4l4x'))
