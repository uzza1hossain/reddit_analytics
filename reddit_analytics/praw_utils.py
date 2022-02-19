import datetime
import os
from pathlib import Path

import environ
import praw

from reddit_analytics import models

env = environ.Env()
BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

reddit = praw.Reddit(
    client_id=env("client_id"),
    client_secret=env("client_secret"),
    password=env("password"),
    user_agent=env("user_agent"),
    username=env("username"),
)

subreddit = reddit.subreddit("django")
last_hour = datetime.datetime.now() - datetime.timedelta(hours=3)


def submissions():
    submission_authors = []
    for submission in subreddit.new():
        utc_time = datetime.datetime.fromtimestamp(submission.created)
        if utc_time >= last_hour:
            submission_authors.append(submission.author.name)

    for author in list(set(submission_authors)):
        quantity = submission_authors.count(author)
        submission = models.Submission.objects.create(author=author, count=quantity)
        submission.save()


def comments():
    comment_authors = []
    for comment in subreddit.comments():
        utc_time = datetime.datetime.fromtimestamp(comment.created)
        if utc_time >= last_hour:
            comment_authors.append(comment.author.name)

    for author in list(set(comment_authors)):
        quantity = comment_authors.count(author)
        comment = models.Comment.objects.create(author=author, count=quantity)
        comment.save()
