import pandas
import praw
from praw.models import MoreComments

reddit = praw.Reddit(client_id='2CSFsNJZroWiiw',
                     client_secret='d3f9vEFoqyzxrlOFYtomn74KlR4',
                     user_agent='Machine Learning Project for Hackathon',)
sub = reddit.subreddit('RoastMe')
for submission in sub.top(limit=5):
    print("Post ID: " + submission.id)
    submission.comments.replace_more(limit=0)
    for top_level_comment in submission.comments:
       print(top_level_comment.body)