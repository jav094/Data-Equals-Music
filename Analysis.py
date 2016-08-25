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
    # Online mode is off by default, so we use our generated .csv
    # In Online Mode, we instantiate the API and get our populated and cleaned DataFrame in real-time.
    def __init__(self):
        if ONLINE_MODE:        
            api = SpotiAPI()
            self.df = api.get_dataframe()
        else:
            file = "data/modified_spotify_top_200.csv"
            self.df = pd.read_csv(file)

    # Fit a model to the data
    def fit_model(self, df, X, y):
        raise NotImplementedError()

    # Gauge accuracy (at least at first, I plan on using cross-validation for this)
    # Repeat with different estimators to improve accuracy
    def evaluate_accuracy(self):
        raise NotImplementedError()

# Let's do most of the actual analysis down here outside of in the class, since it's less structures. 
# We'll use class methods to help us along.
a = Analysis()
df = a.df

pp.pprint(df.head(20))
# print df.columns

# Below: all grabbed from class notebook

# # define X and y
feature_cols = ['loudness', 'instrumentalness', 'valence', 'danceability']
X = df[feature_cols]
# y = titanic.Survived

# # train/test split
# from sklearn.cross_validation import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

# # train a logistic regression model
# from sklearn.linear_model import LogisticRegression
# logreg = LogisticRegression(C=1e9)
# logreg.fit(X_train, y_train)

# # make predictions for testing set
# y_pred_class = logreg.predict(X_test)

# EITHER:

# # calculate testing accuracy
# from sklearn import metrics
# print metrics.accuracy_score(y_test, y_pred_class)

# OR:

# calculate cross-validated AUC
# from sklearn.cross_validation import cross_val_score
# cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()