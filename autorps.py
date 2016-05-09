#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, random, time

CONSUMER_KEY = '[redacted]'
CONSUMER_SECRET = '[redacted]'
ACCESS_KEY = '[redacted]'
ACCESS_SECRET = '[redacted]'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        st = status.text
        stl = (st.lower())
        print st
        print status.user.screen_name
        rock = "@autorps rock"
        paper = "@autorps paper"
        scissors = "@autorps scissors"
        a = ["ROCK", "PAPER", "SCISSORS"]
        r = random.choice(a)
        if stl == rock:
            print "YOU THREW ROCK!"
            api.update_status('@%s YOU THREW ROCK, I THROW %s (%s)' % (status.user.screen_name, r, status.created_at), in_reply_to_status_id = status.id)
        elif stl == paper:
            print "YOU THREW PAPER!"
            api.update_status('@%s YOU THREW PAPER, I THROW %s (%s)' % (status.user.screen_name, r, status.created_at), in_reply_to_status_id = status.id)
        elif stl == scissors:
            print "YOU THREW SCISSORS"
            api.update_status('@%s YOU THREW SCISSORS, I THROW %s (%s)' % (status.user.screen_name, r, status.created_at), in_reply_to_status_id = status.id)
        else:
            print "NOT A THROW"

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['@autorps'])
