from lol_api import call_lol_api
from chat_actions import chat
import re


def a_main():
    info = call_lol_api('current_game', 3790466)
    try:
        position_in_game = -1
        for x, d in enumerate(info['participants']):
            if d['summonerId'] == 3790466:
                position_in_game = x
        if position_in_game == -1:
            raise TypeError
        champ = call_lol_api('champ_by_id', info['participants'][position_in_game]['championId'])['key']
        try:
            re.match('[aeiou]', champ, re.I).start()
            chat('Wow, is that an {} main?'.format(champ))
        except AttributeError:
            chat('Wow, is that a {} main?'.format(champ))
    except TypeError:
        chat('Meeseeks is not in a game...')
