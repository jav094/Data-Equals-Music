"""
    Data == Music
    -------------
    A prediction model that can predict how highly rated 
    music will be based on audio characteristics and 
    track information from Spotify!
"""


import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import json


# Sets up pretty print (easy viewing of data hierarchies and other niceties)
pp = pprint.PrettyPrinter(depth=4)

# Adds TrackID feature, composed from URL
def add_track_id_to_frame(df):
    for track in df.values:
        df["TrackID"] = get_track_id(track[4])

# Drops unnneeded features (e.g. Streams)
def clean_frame(df):
    cols_to_drop = ["Streams", "URL"]
    df.drop(cols_to_drop,inplace=True,axis=1)    

# Returns substring between "track/" and the end of the string. That's the track ID!
def get_track_id(Url):
    try:
        search_string = "track/"
        start = Url.index(search_string)+len(search_string)
        return Url[start:]
    except ValueError:
        print("There's no song ID in this URL! ", Url)

# Fetches audio features for specific tracks and adds them to the df.
def add_audio_features_to_frame(df):
    for track in df.itertuples():
        # Get audio features for the current track
        # Note: we need [0] to actually get IN the dictionary, otherwise this returns a list containing the dict.
        track_audio_features = sp.audio_features(tracks=[track.TrackID])[0]

        # Iterate through the audio features and add each as a new feature column
        for key, value in track_audio_features.iteritems():
            df[key] = value

# Fetches track info for specific track and adds them to the df.
def add_track_info_to_frame(df):
    raise NotImplementedError("Not implemented")

# Fetches track lyrics for specific track and adds them to the df.
def add_lyrics_to_frame(df):
    raise NotImplementedError("Not implemented")

# Export dataframe to a .csv just in case the API stops liking us.
def save_to_csv(df):
    filename = "spotifyDataModified.csv"
    df.to_csv(path_or_buf=filename)
    print("Exported dataframe to file: %s" % (filename))


# From: http://stackoverflow.com/q/24392515/1958853
# Grabs API client ID and client secret from spotify_tokens
tokensfile = open("spotify_tokens", "r")
SP_CLIENT_ID = tokensfile.readline().rstrip()
SP_CLIENT_SECRET = tokensfile.readline().rstrip()

# Perform Client Credentials flow to get an OAuth token that we need. 
client_credentials_manager = SpotifyClientCredentials(client_id=SP_CLIENT_ID, client_secret=SP_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False

# Get our initial csv data into a DataFrame
df = pd.read_csv("data/global-spotify-top200-8-18.csv")

# Get track id, audio features, track info, and other features into DataFrame
add_track_id_to_frame(df)

# add_audio_features_to_frame(df)
# add_track_info_to_frame(df)
# add_lyrics_to_frame(df)
save_to_csv(df)