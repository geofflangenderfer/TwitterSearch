#!yusr/bin/env python3
import json
from Tweet import Tweet
import auth.credentials
import requests

class TwitterSearch():

    def __init__(self, author_string):
        self.headers = {"Authorization": f"Bearer {auth.credentials.bearer_token}"}
        self.author = author_string
        self.next_token = ""
        self.url = self.get_query_url() 
        self.tweets = []#self.get_tweets()
        self.get_tweets()

    def get_tweets(self):
    
        response_json = self.get_twitter_response_json(self.url)
        self.extract_tweets(response_json)
        while(self.has_next_page(response_json)):
            self.next_token = response_json['meta']['next_token']
            #url = self.url + f"&next_token={next_token}"
            url = self.get_query_url()
            response_json = self.get_twitter_response_json(url)
            self.extract_tweets(response_json)

    def extract_tweets(self, response_json):
        
        for obj in response_json["data"]:
            self.tweets.append(Tweet(
                obj["id"],
                obj["text"],
                self.author,
                obj["created_at"],
                json.dumps(obj["public_metrics"]),
                obj["public_metrics"]["like_count"],
            ))

    def has_next_page(self, response_json):
        if "next_token" in response_json["meta"]:
            return True
        return False


    def get_query_url(self):
        base = "https://api.twitter.com/2/tweets/search/recent"
        query = f"?query=from:{self.author}"
        max_results = "&max_results=100"
        tweet_fields = "&tweet.fields=created_at,public_metrics"
        next_token = f"&next_token={self.next_token}" if len(self.next_token) > 0 else ""
        url = base + query + max_results + tweet_fields + next_token


        return url

    def get_twitter_response_json(self, url):
        response = requests.get(url, headers=self.headers)


        if response.status_code != 200:
            raise Exception(response.status_code, response.text)

        return response.json()
    

if __name__ == '__main__':
    test = TwitterSearch('dvassallo')
    for tweet in test.tweets:
        print(tweet)
