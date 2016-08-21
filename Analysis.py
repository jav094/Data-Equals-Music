"""
    Data == Music
    -------------
    A prediction model that can predict how highly rated 
    music will be based on audio characteristics and 
    track information from Spotify!
"""


import pandas as pd
import pprint
pp = pprint.PrettyPrinter(depth=4)

# When ONLINE_MODE is True, we'll hit the live API and work with realtime data.
# Otherwise, it'll work off the stored .csv file, which can be updated by running DataEqualsMusic.py on its own.
ONLINE_MODE = False

from DataEqualsMusic import SpotiAPI


class Analysis(object):
    # Instantiate the API and get our (fully populated and cleaned) DataFrame!
    # If API is down or something, SpotiAPI can export the DataFrame to a .csv, backups kept in /data
    def __init__(self):
        if ONLINE_MODE:        
            api = SpotiAPI()
            self.df = api.get_dataframe()
        else:
            file = "data/modified_spotify_top_200.csv"
            self.df = pd.read_csv(file)

    # Fit a model to the data
    def fit_model(self):
        raise NotImplementedError()

    # Gauge accuracy (at least at first, I plan on using cross-validation for this)
    # Repeat with different estimators to improve accuracy
    def evaluate_accuracy(self):
        raise NotImplementedError()

# Let's do most of the actual analysis down here outside of in the class, since it's less structures. 
# We'll use class methods to help us along.
a = Analysis()
df = a.df

pp df.head(1)