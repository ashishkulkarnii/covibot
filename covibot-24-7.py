from time import sleep
import random 
import praw
import re
import os
import json
from six.moves.urllib.request import urlopen


r = praw.Reddit('bot1')


def getDictFromURL(url):
    DEFAULT_ENCODING = 'utf-8'
    urlResponse = urlopen(url)
    if hasattr(urlResponse.headers, 'get_content_charset'):
        encoding = urlResponse.headers.get_content_charset(DEFAULT_ENCODING)
    else:
        encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
    result = json.loads(urlResponse.read().decode(encoding))
    return result


def abbreviationSearch(x):
    if 'US' in x:
        return 'united states'
    x = x.lower()
    if 'usa' in x:
        return 'united states'
    if 'uk' in x:
        return 'united kingdom'
    if 'saudi' in x:
        return 'saudi arabia'
    if 'andhra' in x:
        return 'andhra pradesh'
    return x

#account for abbreviations of common countries / regions, and returning lowercase string regardless of the presence of abbreviated name


def coviComment(x):
    x = abbreviationSearch(x)
    #x = x.split()
    for i in state_stats:
        r = i['region'].lower()
        if r in x:
            return [i["region"], str(i["totalInfected"])]
    for i in world_covid_stats:
        c = i["country"].lower()
        if c in x:
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


def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    if iteration == total: 
        print()

def barOfProgress(number_of_seconds):
    items = list(range(0, number_of_seconds * 10))
    l = len(items)
    printProgressBar(0, l, prefix = 'Next Iteration:', suffix = '', length = 50)
    for i, item in enumerate(items):
        sleep(0.1)
        printProgressBar(i + 1, l, prefix = 'Next Iteration:', suffix = '', length = 50)

#progress bar between each iteration, not necessary


def clear(): 
    if os.name == 'nt': 
        _ = os.system('cls') 

#to clear console screen, not necessary


response_formats = ['{} has {} current cases, be careful!', '{} has {} infected people, stay safe!', '{} currently has {} active patients, keep your mask on!', '{} has {} COVID-19 patients presently, don\'t forget to keep sanitizer handy!']

f = open('IDs-responded-to.txt', 'a') #creating a text file, in case it does not already exist


clear()


count_iter = 1

while True: #program runs constantly. if you don't want a progress bar, you can replace 'True' with 'not sleep(60)' and remove L137, since sleep method always returns None
    
    f = open('IDs-responded-to.txt', 'r+') #opening the text file in read-and-write mode, with the handle at the top of the page
    IDs = f.readlines()
    
    url1 = 'https://api.apify.com/v2/key-value-stores/tVaYRsPHLjNdNBu7S/records/LATEST?disableRedirect=true'
    world_covid_stats = getDictFromURL(url1)

    url2 = 'https://api.apify.com/v2/key-value-stores/toDWvRj1JpTXiM8FF/records/LATEST?disableRedirect=true'
    state_stats = getDictFromURL(url2)["regionData"]

    #created a list of dictionaries of world COVID-19 stats, gets data from respective government APIs. eg: India - https://www.mohfw.gov.in/, all the datasets used are regularly updated

    subreddit = r.subreddit("SpaceJam2021")
    for submission in subreddit.new(limit=None): #limit=None indicates the bot sees all the posts in the subreddit, and .new indicates the bot sees the posts in chronological order. These valuse can be changed based on requirement.
        if str(submission.id) + '\n' not in IDs: #this is to make sure a post is replied to only once
            if re.search("going", submission.title, re.IGNORECASE) or re.search("trip", submission.title, re.IGNORECASE) or re.search("visit", submission.title, re.IGNORECASE) or re.search("visiting", submission.title, re.IGNORECASE) or re.search("in", submission.title, re.IGNORECASE) or re.search("at", submission.title, re.IGNORECASE) or re.search("go", submission.title, re.IGNORECASE) or re.search("heading", submission.title, re.IGNORECASE) or re.search("headed", submission.title, re.IGNORECASE):
                c = coviComment(submission.title)
                if c != None:
                    submission.reply(random.choice(response_formats).format(*c) + "\n\n\n\n---\n\n^(Beep boop. I am a bot.)\n^(Want to see what I'm made of? Check out: ) [^GitHub ](https://github.com/ashishkulkarnii/covibot/blob/main/covibot-24-7.py)")
                    print("Bot replying to : ", submission.title)
                    f.write(submission.id + '\n')
                c = None

    f.close()
    
    print("Iteration %d complete." % count_iter)
    
    barOfProgress(number_of_seconds = 60) #one minute between each iteration
    
    count_iter += 1
    
    clear()
    
    print("Iteration %d begins." % count_iter)
