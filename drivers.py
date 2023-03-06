import requests
import datetime

def get_default_list():
    return ['max_verstappen', 'perez', 'leclerc', 'sainz', 'russell', 'hamilton', 'norris', 'bottas', 'ocon', 'alonso', 'gasly', 'kevin_magnussen', 'vettel', 'ricciardo', 'tsunoda', 'zhou', 'mick_schumacher', 'albon', 'stroll', 'latifi']


def get_wdc_standings(year):
    response = requests.get(f'https://ergast.com/api/f1/{year}/driverStandings.json')

    res = []

    for driver in response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
        res += [driver['Driver']['driverId']]

    return res
