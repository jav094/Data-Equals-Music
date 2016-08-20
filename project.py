# import necessities
import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint
import json

# set up pretty print in this proj
pp = pprint.PrettyPrinter(depth=4)


# Adds TrackID feature, composed from URL
def addTrackIdToFrame(df):
    for track in df.values:
        df["TrackID"] = getTrackID(track[4])

# Drops unnneeded features (e.g. Streams)
def cleanFrame(df):
    colsToDrop = ["Streams", "URL"]
    df.drop(colsToDrop,inplace=True,axis=1)    


# Returns substring between "track/" and the end of the string. That's the track ID!
def getTrackID(Url):
    try:
        searchString = "track/"
        start = Url.index(searchString)+len(searchString)
        return Url[start:]
    except ValueError:
        print("There's no song ID in this URL! ", Url)


# Fetches audio features for specific tracks and adds them to the df.
def addAudioFeaturesToFrame(df):
    for track in df.itertuples():
        # Get audio features for the current track
        # Note: we need [0] to actually get IN the dictionary, otherwise audio_features returns a list containing the dict.
        trackAudioFeatures = sp.audio_features(tracks=[track.TrackID])[0]

        # Iterate through the audio features and add each as a new feature column
        for key, value in trackAudioFeatures.iteritems():
            df[key] = value


def saveToCsv(df):
    df.to_csv(path_or_buf="spotifyDataModified.csv")

# From: http://stackoverflow.com/q/24392515/1958853
# Grabs API client ID and client secret from spotify_tokens
tokensfile = open("spotify_tokens", "r")
SP_CLIENT_ID = tokensfile.readline().rstrip()
SP_CLIENT_SECRET = tokensfile.readline().rstrip()

# Perform Client Credentials flow to get an OAuth token that we need. 
client_credentials_manager = SpotifyClientCredentials(client_id=SP_CLIENT_ID, client_secret=SP_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
sp.trace=False


# 1. Get csv data into a DataFrame
df = pd.read_csv("data/global-spotify-top200-8-18.csv")

# 2. Get track id, audio features, track info, and other features into df
# track IDs
addTrackIdToFrame(df)
# audio features
addAudioFeaturesToFrame(df)


saveToCsv(df)


# track info
# lyrics
# lyrics meanindful root words?



# results = sp.search(q=artist_name, limit=50)
# pp.pprint(results)


# 2. Fit a model to the data.
# 3. Gauge accuracy (at least at first, I plan on using cross-validation for this)
# 4. Repeat steps 2-3 with different estimators to improve accuracy.
# 5. Add new features, partly out of curiosity and partly to improve accuracy.
# 6. (optional) dimensionality reduction