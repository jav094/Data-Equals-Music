# Data == Music
A prediction model that can predict how highly rated music will be based on audio characteristics and track information from Spotify.

### The problem & my hypothesis
Music can be infinitely varied, and yet people are often able to agree on what is "good". Can we predict a track's popularity based on its characteristics?

### My hypothesis
I think we can. A few features spring to mind: "danceability", being in a major key, and probably certain key lyrics ("love", "c'mon").

### The data:
[Spotify Charts](https://spotifycharts.com) is a cool little project launched by Spotify in 2013, showcasing the most listened to and most viral tracks on Spotify each week. I grabbed the convenient .csv of popular tracks which contains the track name, artist name, top 200 ranking, and a URL to the track on spotify's web client.

I then used [Spotify Charts](https://github.com/plamere/spotipy/blob/master/docs/index.rst), a convenient Python wrapper for the Spotify web API, to get the audio characteristics. The wrapper's audio_features method takes a song ID, which I extracted from the URL in the csv file.

The hardest part remains: putting everything neatly in a DataFrame together such that we can make predictions off it!

### Pre-processing
This data is pristine! No cleaning or modification was needed, it went into a DataFrame as-is.

### Exploration and visualization
Not much exploration yet. First need a complete DataFrame!

### Features
From [Spotify's web API documentation](https://developer.spotify.com/web-api/track-endpoints), I gathered enough background to form a laundry list of features:
* acousticness - A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* analysis_url - An HTTP URL to access the full audio analysis of this track. An access token is required to access this data.
* danceability - Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* duration_ms - The duration of the track in milliseconds.
* energy - Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks * feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.
* id - The Spotify ID for the track.
* instrumentalness - Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* key - The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on.
* liveness - Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* loudness - The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typical range between -60 and 0 db.
* mode - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* speechiness - Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* tempo - The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* time_signature - An estimated overall time signature of a track. The time signature (meter) is a notational convention to specify how many beats are in each bar (or measure).
* track_href - A link to the Web API endpoint providing full details of the track.
* type - The object type: "audio_features"
* uri - The Spotify URI for the track.
* valence - A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).

### Modeling process
1. Get everything into a dataframe, abstracting features into dummy variables when necessary.
2. Use Linear Regression model fit to the data
3. Use cross-validation to gauge accuracy
4. Accuracy improvement
5. (optional) dimensionality reduction

### Challenges & successes
The first challenge is the one I'm on now: getting the data into a usable format!

### Extensions / business applications
Spotify themselves could use this, or a music publisher could use it to help make a business case for putting one of their artists on Spotify. If, for example, their music were very similar to a known quantity, they might be likely to rank similarly once well-exposed to the public.

### Key learnings & conclusions
None yet - please hold