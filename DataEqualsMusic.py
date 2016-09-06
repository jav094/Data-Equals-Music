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

class SpotiAPI(object):

    def __init__(self):
        file = "data/global-spotify-top200-8-18.csv"
        self.df = pd.read_csv(file)

        # Grabs API client ID and client secret from spotify_tokens file.
        tokensfile = open("spotify_tokens", "r")
        SP_CLIENT_ID = tokensfile.readline().rstrip()
        SP_CLIENT_SECRET = tokensfile.readline().rstrip()

        # Perform client credentials flow to get an OAuth token that we need.
        client_credentials_manager = SpotifyClientCredentials(client_id=SP_CLIENT_ID, client_secret=SP_CLIENT_SECRET)
        sp_client = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        sp_client.trace = False

        # Get track id, audio features, track info, and other features into DataFrame.
        self.add_track_id_to_frame()
        self.add_audio_features_to_frame(sp_client)
        # self.add_lyrics_to_frame(sp_client)

        # Do this last, it drops unnneeded features and cleans the data if necessary.
        self.clean_frame()

    # Adds TrackID feature, sliced from URL.
    def add_track_id_to_frame(self):
        for index, row in self.df.iterrows():
            self.df.loc[index,"TrackID"] = self.get_track_id(row.URL)

    # Returns substring between "track/" and the end of the string. That's the track ID!
    def get_track_id(self, url):
        try:
            search_string = "track/"
            start = url.index(search_string)+len(search_string)
            return url[start:]
        except ValueError:
            print("There's no song ID in this URL! ", url)

    # Fetches audio features for specific tracks and adds them to the df.
    def add_audio_features_to_frame(self, sp_client):
        for index, row in self.df.iterrows():
            # Hit the Spotify API for the current track's audio features.
            # Note: we need [0] to actually get to the dictionary, otherwise this returns a list containing the dict.
            track_audio_features = sp_client.audio_features(tracks=[row.TrackID])[0]

            # Iterate through the audio features and add each as a new feature column.
            for key, value in track_audio_features.items():
                self.df.loc[index,key] = value

    # Fetches track lyrics for specific track and adds them to the df.
    def add_lyrics_to_frame(self, sp_client):
        raise NotImplementedError("Not implemented")

    # Drops unnneeded features.
    def clean_frame(self):
        cols_to_drop = ["Streams", "URL", "analysis_url", "track_href", "type", "uri", "id", "Track Name", "Artist", "TrackID"]
        self.df.drop(cols_to_drop, inplace=True, axis=1)

    # Export dataframe to a .csv (which is what we do our analysis on).
    def save_to_csv(self, file):
        self.df.to_csv(path_or_buf=file)
        print("Exported dataframe to file: %s" % (file))
    
    # Return the dataframe (for use by external classes).
    def get_dataframe(self):
        return self.df


# If this .py file is run on its own, it'll export the dataframe to a csv so we can analyze the data offline.
if __name__ == '__main__':
    api = SpotiAPI()
    api.save_to_csv("data/modified_spotify_top_200.csv")