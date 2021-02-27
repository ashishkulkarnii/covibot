# covibot
A Reddit bot which gives COVID-19 stats of a specific region to Redditors based on their post title. 

A SpaceJam 2021 project.

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
