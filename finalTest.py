from pandas import DataFrame, read_csv
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import requests
import re
from seperator import *
from SongDataScrape import*
from incrementalPairMap import*

songName = "Better Now"
artist = "Post Malone"

getSongLyricsToTXT(songName, artist)
#printPairs(pullWords("Better-Now-lyrics"), "Better Now")



filePathLyrics = ('.\lyrics\\' +artist+","+songName+'.txt').replace(" ",",")
filePathCounts = ('.\counts\\' +artist+","+songName+'.txt').replace(" ",",")
#readFile = open((fileName), "r")
#content = readFile.readlines

songWords = incrementalPairMap()
songWords.createFromFile(filePathLyrics)
songWords.prettyPrint(filePathCounts)
