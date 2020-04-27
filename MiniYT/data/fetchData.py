import time, json, threading, random, string
from datetime import datetime, timedelta
from data.models import Video
import requests

def insertVideoInDatabase(youtubeResponse):
    videos = youtubeResponse['items']
    print('FETCHED VIDEOS: ', len(videos))
    for video in videos:
        videoId = video['id']['videoId']
        title = video['snippet']['title']
        description = video['snippet']['description']
        publishedAt = video['snippet']['publishedAt']
        thumbnailURL = video['snippet']['thumbnails']['default']["url"]
        try:
            videoObject = Video(
                videoId = videoId,
                title = title,
                description = description,
                publishedAt = publishedAt,
                thumbnailURL = thumbnailURL
            )
            videoObject.save()
        except Exception as e:
            print('Could not insert video into database: ')
            print(e)


def fetchData(timeInterval, apiKey, searchQuery):

    # compute previous time to query youtube API
    publishedAfter = (datetime.now() - timedelta(seconds = timeInterval)).isoformat("T") + "Z" 
    # Z at the end is for UTC format

    params = {
        "part": "snippet",
        "eventType": "completed",
        "maxResults": 50,
        "order": "date",
        "publishedAfter": publishedAfter,
        "q": searchQuery,
        "relevanceLanguage": "en",
        "type": "video",
        "key": apiKey
    }
    
    result = requests.get('https://www.googleapis.com/youtube/v3/search', params=params)
    
    if result.status_code == 200:
        insertVideoInDatabase(json.loads(result.text))
    else:
        print('########### API RESPONSE ERROR ###########')
        print(result.json())
        print('##########################################')

    # sleep for he desired interval and fetch again
    time.sleep(timeInterval)
    fetchData(timeInterval, apiKey, searchQuery)

def startFetchingData(timeInterval, apiKey, searchQuery):
    apiFetchThread = threading.Thread(target = fetchData, args=(timeInterval, apiKey, searchQuery, ))
    apiFetchThread.start()