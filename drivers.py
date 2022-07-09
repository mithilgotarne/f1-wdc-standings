import requests

def get_default_list():
    return ['max_verstappen', 'perez', 'leclerc', 'sainz', 'russell', 'hamilton', 'norris', 'bottas', 'ocon', 'alonso', 'gasly', 'kevin_magnussen', 'vettel', 'ricciardo', 'tsunoda', 'zhou', 'mick_schumacher', 'albon', 'stroll', 'latifi']


def get_wdc_standings():
    response = requests.get('https://ergast.com/api/f1/current/driverStandings.json')

    res = []

    for driver in response.json()['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']:
        res += [driver['Driver']['driverId']]

    return res
