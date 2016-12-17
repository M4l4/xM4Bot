import requests
from config import LOL_API

URLS = dict(
    summoner_by_name='api/lol/{region}/v1.4/summoner/by-name/{summonerName}',
    summoner_by_id='api/lol/{region}/v1.4/summoner/{summonerId}',
    match_list='api/lol/{region}/v2.2/matchlist/by-summoner/{summonerId}',
    match='api/lol/{region}/v2.2/match/{matchId}',
    recent_games='api/lol/{region}/v1.3/game/by-summoner/{summonerId}/recent',
    ranked_stats='api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/ranked',
    summary_stats='api/lol/{region}/v1.3/stats/by-summoner/{summonerId}/summary',
    league_data='api/lol/{region}/v2.5/league/by-summoner/{summonerId}',
    current_game='/observer-mode/rest/consumer/getSpectatorGameInfo/{region2}/{summonerId}',
    champ_by_id='/api/lol/static-data/{region}/v1.2/champion/{championId}'
)

region2 = dict(
    na='na1',
    euw='euw1',
    eune='eun1',
    br='br1',
    jp='jp1',
    kr='kr',
    lan='la1',
    las='la2',
    oce='oc1',
    pbe='pbe1',
    ru='ru',
    tr='tr1'
)

base = 'https://{region}.api.pvp.net/'


def call(function: str, an_id: int, region: str = "oce"):
    if function == 'current_game':
        url = (base + URLS[function]).format(
            region=region,
            summonerId=an_id,
            region2=region2[region])
    elif function == 'champ_by_id':
        url = (base + URLS[function]).format(
            region=region,
            championId=an_id)
    else:
        url = (base + URLS[function]).format(
            region=region,
            summonerId=an_id)
    params = {'api_key': LOL_API}
    r = requests.get(url, params=params)
    if r.status_code == 404:
        return 'Meeseeks is not in a game.'
    return r.json()
