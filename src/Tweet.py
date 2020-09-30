#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Tweet(Base):
    # TODO: change this 
    __tablename__ = 'tweets'

    # https://developer.twitter.com/en/docs/twitter-api/data-dictionary/object-model/tweet
    id = Column(String, primary_key=True)
    text = Column(String)
    author = Column(String)
    created_at = Column(String) # ISO 8601
    public_metrics = Column(String) # json string
    like_count = Column(Integer)

    def __init__(
        self,
        id_string,
        text_string,
        author_string,
        created_at_string,
        public_metrics_string,
        like_count_string
    ):
        self.id = id_string
        self.text = text_string
        self.author = author_string
        self.created_at = created_at_string
        self.public_metrics = public_metrics_string
        self.like_count = like_count_string

    # not printing public_metrics for now. Only like_count.
    def __repr__(self):
       return f"<Tweet (id={self.id}, text={self.text}, author={self.author}," \
               + f"created_at={self.created_at}, like_count={self.like_count})>"

if __name__ == '__main__':
    test = Tweet(
        '1',
        'test tweet',
        'me',
        'today',
        '{metrics}',
        '1',
    )
    print(test)
