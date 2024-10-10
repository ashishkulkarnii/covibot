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

For reference, check out our subreddit: https://www.reddit.com/r/SpaceJam2021/

For a quick demo, check out my YouTube video: https://www.youtube.com/watch?v=AqTPwbqeNeU

PPT: https://docs.google.com/presentation/d/15PUDgeP8JoicsmX3rf_dg8xgRDyMsBSlQQbA5nvFyoU/edit?usp=sharing

Our submission on Devfolio: https://devfolio.co/submissions/covibot-cf95

UPDATE: covibot-24-7.py is essentially the same bot, but now can run continuously. 
