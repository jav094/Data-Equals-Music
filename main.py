# import ALL THE THINGS
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from textblob import TextBlob, Word
import seaborn as sea
import spotipy


# Hit the Spotify API for a specific track's audio featuers (e.g. valence, key)
# def getAudioFeatures(url):
#     return " "

# Create a DataFrame
file = "data/global-spotify-top200-8-17.csv"
sp = pd.read_csv(file)
print sp

spotify = spotipy.Spotify()

# name = "Justin Timberlake"
# results = spotify.search(q='artist:' + name, type='artist')
# print results