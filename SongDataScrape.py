from pandas import DataFrame, read_csv
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
import pandas as pd
import sys
import matplotlib
import requests
import re
from seperator import*

#this function scrapes the web for the top 100 songs on a given day in history
def getChartsForDate(Month, Day, Year):
    
    #Gaining access to the billboards hot 100 for the specified date
    webpage = requests.get("https://www.billboard.com/charts/hot-100"+ "/" + Year + "-" + Month + "-" + Day)
    #turning the contents of the page into a soup
    soup = BeautifulSoup(webpage.content, "html.parser")
    #scraping top song and artist off the charts
    topSong = soup.select('.chart-number-one__title')
    topArtist = soup.select('.chart-number-one__artist')

    #scraping 2-100 ranked songs off the charts
    songs_list = soup.select('.chart-list-item__title-text')
    artists_list = soup.select('.chart-list-item__artist')

    #intializing lists for the final song list and artist list
    final_song_list = []
    final_artists_list = []
    
    #adding song and artist to lists after removing tags for top song
    final_song_list.append(topSong[0].text.strip())
    final_artists_list.append(topArtist[0].text.strip())

    #adding songs 2-100 to list after removing tags
    for x in songs_list:
        final_song_list.append(x.text.strip())
    #adding artist to list after removing tags
    for y in artists_list:
        final_artists_list.append(y.text.strip())

    #creating data frame for songs and artist in top 100
    Top100Songs = pd.DataFrame({'Songs': final_song_list, 'Artist': final_artists_list})
    Top100Songs.to_csv('Top100Songs' + Month + Day + Year + ".csv")

    #return data frame of top 100 songs
    return Top100Songs

#this function scrapes the web for the lyrics to a song and creates a txt output of the song
def getSongLyricsToTXT (song, artist):

    #changing variables to append to weblink
    songSearch = song.replace(" ", "-")
    artistSearch = artist.replace(" ", "-")
    
    #gaining access to lyrics page
    lyricPage = requests.get('https://genius.com/'+ artistSearch + '-' + songSearch +"-"+'lyrics')

    #creating soup of page contents
    songSoup = BeautifulSoup(lyricPage.content, 'html.parser')
    #scraping lyrics and removing all tags
    lyrics = songSoup.select('.lyrics')
    lyrics[0] = lyrics[0].text.strip()

    #creating txt file and writing song lyrics to txt file

    lyricsFile = open(('.\lyrics\\'+artistSearch+"," +songSearch+'.txt').replace(" ",",").replace("-",","), 'w')
    lyricsFile.write(lyrics[0])
    lyricsFile.close()







