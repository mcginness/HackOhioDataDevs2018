from pandas import DataFrame, read_csv
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import requests
import re
from seperator import *


def getChartsForDate(Month, Day, Year):
    
    webpage = requests.get("https://www.billboard.com/charts/hot-100"+ "/" + Year + "-" + Month + "-" + Day)

    soup = BeautifulSoup(webpage.content, "html.parser")

    topSong = soup.select('.chart-number-one__title')
    topArtist = soup.select('.chart-number-one__artist')
    songs_list = soup.select('.chart-list-item__title-text')
    artists_list = soup.select('.chart-list-item__artist')

    final_song_list = []
    final_artists_list = []

    final_song_list.append(topSong[0].text.strip())
    final_artists_list.append(topArtist[0].text.strip())

    for x in songs_list:
        final_song_list.append(x.text.strip())

    for y in artists_list:
        final_artists_list.append(y.text.strip())

    Top100Songs = pd.DataFrame({'Songs': final_song_list, 'Artist': final_artists_list})
    Top100Songs.to_csv('Top100Songs' + Month + Day + Year + ".csv")

    return Top100Songs


def getSongLyricsToTXT (song, artist):
    song = song.replace(" ", "-")
    artist = artist.replace(" ", "-")
    
    lyricPage = requests.get('https://genius.com/'+ artist + '-' + song +"-"+'lyrics')

    songSoup = BeautifulSoup(lyricPage.content, 'html.parser')
    lyrics = songSoup.select('.lyrics')
    lyrics[0] = lyrics[0].text.strip()

    lyricsFile = open(song+'-lyrics.txt', 'w')
    lyricsFile.write(lyrics[0])
    lyricsFile.close()

getSongLyricsToTXT("Sicko Mode", "Travis Scott")
pullWords("Sicko-Mode-lyrics")
    
    
getChartsForDate("10", "26", "2018")






