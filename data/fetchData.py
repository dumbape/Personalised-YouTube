import time, json, threading, random, string
from datetime import datetime
from data.models import Video

def getRandomString(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def fetchData(timeInterval):

    # mocking the API for the moment
    video = Video(videoId=getRandomString(6), 
                    title='Hello There, this is from youtube, yay! corona',
                    description='Some Random Stuff',
                    thumbnailURL='https://www.google.com',
                    publishedAt=datetime.now()
                )

    video.save()

    # sleep for he desired interval and fetch again
    time.sleep(timeInterval)
    fetchData(timeInterval)

def startFetchingData():
    print('Reading data.config...')
    with open('data/config.json') as f:
        config = json.load(f)

    timeInterval = int(config.get('ApiFetchInterval'))
    apiFetchThread = threading.Thread(target = fetchData, args=(timeInterval, ))
    apiFetchThread.start()