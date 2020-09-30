#!/usr/bin/env python3
import TwitterSearch
from Tweet import Tweet, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


class SaveTweets():
    def __init__(self, tweets):
        self.connection_string= "postgresql+psycopg2://postgres:postgres@localhost:5432/project_tweets"
        self.tweets = tweets
        self.save_tweets()

    def save_tweets(self):
        session = self.start_db_session()

        for tweet in self.tweets:
            session.add(tweet)
            print(tweet)

        session.commit()

        session.close()

    def start_db_session(self):
        engine = create_engine(self.connection_string)
        # create table if it doesn't exist
        Base.metadata.create_all(engine, checkfirst=True)

        Session = sessionmaker(bind=engine)

        return Session()

if __name__ == '__main__':
    authors = ['paulg', 'r00k', 'brennandunn', 'naval', 'dvassallo', 'patio11']
#    for author in authors:
#        search = TwitterSearch.TwitterSearch(author)
#        SaveTweets(search.tweets)
    search = TwitterSearch.TwitterSearch('patio11')
    SaveTweets(search.tweets)
