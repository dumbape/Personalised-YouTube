import time, json, threading

def fetchData(timeInterval):
    time.sleep(timeInterval)
    fetchData(timeInterval)

def startFetchingData():
    print('Reading data.config...')
    with open('data/config.json') as f:
        config = json.load(f)

    timeInterval = int(config.get('ApiFetchInterval'))
    apiFetchThread = threading.Thread(target = fetchData, args=(timeInterval, ))
    apiFetchThread.start()