#!/usr/bin/env python3
import base64
import requests
import urllib.parse
import credentials

OAUTH2_TOKEN = 'https://api.twitter.com/oauth2/token'


def get_bearer_token(consumer_key, consumer_secret):
    # enconde consumer key
    consumer_key = urllib.parse.quote(consumer_key)
    # encode consumer secret
    consumer_secret = urllib.parse.quote(consumer_secret)
    # create bearer token
    bearer_token = consumer_key + ':' + consumer_secret
    # base64 encode the token
    base64_encoded_bearer_token = base64.b64encode(bearer_token.encode('utf-8'))
    # set headers
    headers = {
        "Authorization": "Basic " + base64_encoded_bearer_token.decode('utf-8') + "",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Content-Length": "29"}

    response = requests.post(OAUTH2_TOKEN, headers=headers, data={'grant_type': 'client_credentials'})
    to_json = response.json()
    print(f"{to_json['access_token']}")


def main():
    consumer_key = credentials.api_key
    consumer_secret = credentials.api_key_secret
    get_bearer_token(consumer_key, consumer_secret)


if __name__ == "__main__":
    main()
