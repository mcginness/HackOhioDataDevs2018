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

getSongLyricsToTXT("Rap God", "Eminem")
printPairs(pullWords("\Rap-God-lyrics"), "\Rap God")
