import re
import requests

from difflib import get_close_matches
from random import choice

def getWojakList():
    r = requests.get('https://www.memeatlas.com/wojak-memes.html')
    html = r.text
    regex = re.compile(r'src\=\"images/wojaks/.*\.(?:png|jpg|gif)\"')
    cleanMyList = lambda x : x.replace('src=','').replace('"','')
    crudeList = regex.findall(html)
    return list(map(cleanMyList,crudeList))

def getWojak(wojackName):
    dashedWojakName = wojackName.lstrip().replace(" ","-")
    closeMatch = get_close_matches('images/wojaks/' + dashedWojakName , 
                                   getWojakList(), n=1)[0]
    fileName = closeMatch[14:]
    return  'http://www.memeatlas.com/' + closeMatch, fileName

def getRandomWojak():
    wojakToReturn = choice(getWojakList())
    fileName = wojakToReturn[14:]
    return  'http://www.memeatlas.com/' + wojakToReturn, fileName
