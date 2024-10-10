# covibot
This project is a Reddit bot which gives COVID-19 stats of a specific region to Redditors based on their post title.
It was created as a submission to the PESU HackerSpace SpaceJam 2021 hackathon.
Out of ~120 teams, placed Top 5 Freshers' Track and Top 15 overall.

To get it up and running:
- add the PRAW library to Python (3.6+), using ```pip install praw```.
- navigate to the Python folder, enter Lib folder, site-packages, and then open praw.ini
- add a bot, like shown below:
    ```
    [bot1]
    client_id=
    client_secret=
    password=
    username=
    user_agent=<any name>
    ```

Note: covibot is designed to run in r/SpaceJam2021, a subreddit I created for testing covibot. 
By changing the line ```subreddit = r.subreddit("SpaceJam2021")```, the bot can be deployed pretty much anywhere.

To learn, in detail, the process I used to create covibot, read my [three part guide](https://medium.com/analytics-vidhya/a-comprehensive-guide-to-creating-a-basic-reddit-bot-part-1-15fb0e4cebcb) on Medium. 

Resources:
- The subreddit where I tested my bot: [r/SpaceJam2021](https://www.reddit.com/r/SpaceJam2021/). You will also find bots developed by people who read my Medium article on this subreddit!
- [This YouTube video](https://www.youtube.com/watch?v=AqTPwbqeNeU) is a quick demo that we sent alog with our hackathon submission.
- [This](https://docs.google.com/presentation/d/15PUDgeP8JoicsmX3rf_dg8xgRDyMsBSlQQbA5nvFyoU) is the slide deck we used during our hackathon demonstration.
- [This](https://devfolio.co/submissions/covibot-cf95) is our Devfolio submission.

Updates:
- covibot-24-7.py is essentially the same bot, but now can run continuously.
