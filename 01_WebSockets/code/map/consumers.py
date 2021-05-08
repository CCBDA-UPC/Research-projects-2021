import json
import time

from django.conf import settings
from channels.generic.websocket import WebsocketConsumer
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

class MyListener(StreamListener):

    def __init__(self, consumer):
        self.consumer = consumer
        self.first = True

    def on_data(self, data):
        tweet = json.loads(data)
        # Send message to connected browser
        url = "https://twitter.com/twitter/statuses/"+str(tweet['id'])
        if tweet['retweeted']:
            return True

        if not self.first:
            time.sleep(10)
        else:
            self.first = False
        self.consumer.send(text_data=json.dumps({
            'type': 'tweet',
            'url': url
        }))
        return True

    def on_error(self, status):
        self.consumer.send(text_data=json.dumps({
            'type': 'control',
            'action': 'error',
            'message': status,
        }))
        return True


class MapConsumer(WebsocketConsumer):
    twitter_stream = None
    auth = None

    def connect(self):
        self.accept()
        self.auth = OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
        self.auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)

    def disconnect(self, close_code):
        if self.twitter_stream is not None:
            self.twitter_stream.disconnect()

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        if text_data_json['type'] == 'listen':
            message = text_data_json['message']
            self.twitter_stream = Stream(auth=self.auth, listener=MyListener(self))
            # Create a new stream and filter by text
            self.twitter_stream.filter(track=[message], is_async=True)
        elif text_data_json['type'] == 'stop' and self.twitter_stream is not None:
            self.twitter_stream.disconnect()
