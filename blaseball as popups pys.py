from sseclient import SSEClient
import json
import time
while True:
    try:
        stream = SSEClient('https://api.sibr.dev/replay/v1/replay?from=2020-08-30T01:00:08.17Z')
        for message in stream:
            # At seemingly fixed intervals, the stream sends an empty message
            if not str(message):
                continue
            data = json.loads(str(message))
            # Sometimes the stream just sends fights
            if 'games' not in data['value']:
                continue
            # If those checks passed, this should work
            games = json.loads(str(message))['value']['games']['schedule']
            for game in games:
                feed = game['lastUpdate']
                print(feed\n)
    except Exception as error:
        print(error)
        # Wait five minutes if the stream breaks
        time.sleep(300)
