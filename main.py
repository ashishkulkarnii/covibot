#covibot


import praw
import pdb
import re
import os
import json
from six.moves.urllib.request import urlopen


r = praw.Reddit('bot1')


DEFAULT_ENCODING = 'utf-8'

url1 = 'https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true'
urlResponse = urlopen(url1)
if hasattr(urlResponse.headers, 'get_content_charset'):
    encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
else:
    encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
world_covid_stats = json.loads(urlResponse.read().decode(encoding))

url2 = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true'
urlResponse = urlopen(url2)
if hasattr(urlResponse.headers, 'get_content_charset'):
    encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
else:
    encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
india_covid_stats = json.loads(urlResponse.read().decode(encoding))
state_stats = india_covid_stats["regionData"]

#created a list of dictionaries of world COVID-19 stats, gets data from respective government APIs. eg: India - https://www.mohfw.gov.in/
#all the datasets used are regularly updated


def coviComment(x):
	x.lower()
	x = x.split()
	for i in state_stats:
		if i["region"] in x:
			return [i["region"], str(i["totalInfected"])]
	for i in world_covid_stats:
		if i["country"] in x:
			all_time = i["infected"]
			if all_time == "NA":
				all_time = 0
			else:
				all_time = int(all_time)
			recovered = i["recovered"]
			if recovered == "NA":
				recovered = 0
			else:
				recovered = int(recovered)
			dead = i["deceased"]
			if dead == "NA":
				dead = 0
			else:
				dead = int(dead)
			current_cases = all_time - recovered - dead
			return [i["country"], str(current_cases)]
	return None

#coviComment returns the active COVID-19 cases of a mentioned country by searching through the .json dataset of countries for the country mentioned in the Reddit post title, and subtracting the number of recovered and deceased cases from the total number of cases. 

subreddit = r.subreddit("SpaceJam2021")
for submission in subreddit.new(limit=1): #limit=1 indicates the bot sees only one post at a time, and .new indicates the bot sees the posts in chronological order. These valuse can be changed based on requirement.
	if re.search("going", submission.title, re.IGNORECASE) or re.search("trip", submission.title, re.IGNORECASE) or re.search("visit", submission.title, re.IGNORECASE) or re.search("visiting", submission.title, re.IGNORECASE) or re.search("in", submission.title, re.IGNORECASE) or re.search("at", submission.title, re.IGNORECASE) or re.search("go", submission.title, re.IGNORECASE):
		c = coviComment(submission.title)
		if c != None:
			submission.reply("{} has {} current cases, be careful!".format(*c))
			print("Bot replying to : ", submission.title)
	



