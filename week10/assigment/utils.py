from bottle import template
import json

JSON_FOLDER = './data'
AVAILABE_SHOWS = ["7", "66", "73", "82", "112", "143",
                  "175", "216", "1371", "1871", "2993", "305"]


def getVersion():
    return "0.0.1"


def getJsonFromFile(showName):
    try:
        return template("{folder}/{filename}.json".format(folder=JSON_FOLDER, filename=showName))
    except:
        return "{}"


def getData():
    data = []
    for filename in AVAILABE_SHOWS:
        data.append(json.loads(getJsonFromFile(filename)))

    return data


def getDataById(showId):
    return json.loads(getJsonFromFile(str(showId)))


def getEpisodeById(showId, episodeId):
    fEpisode = '{}'
    episodes = json.loads(getJsonFromFile(str(showId)))[
        '_embedded']['episodes']

    for episode in episodes:
        if episode['id'] == int(episodeId):
            fEpisode = episode

    return fEpisode


def search(value):
    data = getData()
    result = []

    for show in data:
        for episode in show['_embedded']['episodes']:
            if str(episode['summary']).find(value) > -1:
                resElement = {'showid': show['id'], 'episodeid': episode['id'], 'text': '{}: {}'.format(
                    show['name'], episode['name'])}

                result.append(resElement)

    return result
