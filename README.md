# covibot
A Reddit bot which gives COVID-19 stats of a specific region to Redditors based on their post title. 

A SpaceJam 2021 project. Won 2nd place, Freshers' Track.

To get it up and running, add the PRAW library to Python (3.6+), using ```pip install praw```.

Navigate to the Python folder, enter Lib folder, site-packages, and then open praw.ini

Here, add a bot, like shown below:

Make sure you've registered a Reddit script application before this step, 'cause that's where you'll get the client ID and client secret.

```
[bot1]
client_id=
client_secret=
password=
username=
user_agent=
```

Here, user agent can be any name.

Once you've got this in place, you're ready to go!

Note: covibot is designed to run in r/SpaceJam2021, a subreddit I created for testing covibot. By changing the line ```subreddit = r.subreddit("SpaceJam2021")```, the bot can be deployed pretty much anywhere.


For reference, check out our subreddit: https://www.reddit.com/r/SpaceJam2021/

For a quick demo, check out my YouTube video: https://www.youtube.com/watch?v=AqTPwbqeNeU

PPT: https://docs.google.com/presentation/d/15PUDgeP8JoicsmX3rf_dg8xgRDyMsBSlQQbA5nvFyoU/edit?usp=sharing

Our submission on Devfolio: https://devfolio.co/submissions/covibot-cf95
