
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import math
import pickle
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from time import sleep
from config import *
from os.path import exists



sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id,
                                                           client_secret= client_secret_id))


def search_song(song):
    try:
        song = sp.search(q=song, limit=5)
        return song["tracks"]["items"][0]["id"]
    except:
        return ""



def search_uri(title):
    query = title
    search = sp.search(q=query, type="track")
    uri = search["tracks"]["items"][0]["uri"]
    return uri



def search_url(title):
    query = title
    seach = sp.search(q=query, type="track")
    uri = search["tracks"]["items"][0]['spotify']['external_urls'][0] ## ------>
    return url


def get_cover(song_title):
    result = sp.search(q=song_title, limit=1)
    cover = result['tracks']['items'][0]['album']['images'][1]['url']
    return cover


#same as get image??
def search_image(title):
    query = title
    search = sp.search(q=query, type='track')
    image = search['tracks']['items'][0]['album']['images'][1]['url']
    return image

def search_image_user(title):
    query = title
    search = sp.search(q=query, type='track')
    image = search['tracks']['items'][0]['album']['images'][1]['url']
    return image


def create_df(uri):
    feats_dict = sp.audio_features(uri)
    df_audio = pd.DataFrame(feats_dict)
    df_audio = df_audio.drop(columns=['type', 'id', 'uri', 'track_href', 'analysis_url'], axis=1)
    return df_audio




def get_audio_feat(uri):
    feats_dict = sp.audio_features(uri)
    df_audio = pd.DataFrame(feats_dict)
    return df_audio




def load(filename = "filename.pickle"): 
    try: 
        with open(filename, "rb") as f: 
            return pickle.load(f) 
    except FileNotFoundError: 
        print("File not found!")



def cluster_top_100(df):
    
    hot100 = df
    scaler = load('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/scalers/scaler.pkl')
    kmeans = load("/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/models/APIs9.pickle")
    hot100_feats = hot100[['danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms', 'time_signature']]
    scaled_hot100 = pd.DataFrame(scaler.fit_transform(hot100_feats),columns =hot100_feats.columns)
    cluster_hot100 = kmeans.predict(scaled_hot100)
    hot_100_df_final = hot100
    hot_100_df_final["Cluster"] = cluster_hot100
    hot_100_df_final = hot_100_df_final.drop(columns=['type', 'id', 'uri', 'track_href', 'analysis_url'], axis=1)
    
    hot_100_df_final.to_csv('hot_100_df_final.csv')
    return hot_100_df_final





def cluster_nothot (df):
    
    if exists('nothot_df_final.csv'):
        return pd.read_csv('nothot_df_final.csv')
    not_hot = get_audio_features(df['title'].tolist())
    not_hot = df
    scaler = load('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/scalers/scaler.pkl')
    kmeans = load("/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/models/APIs9.pickle")
    nothot_feats = not_hot[['danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms', 'time_signature']]
    scaled_nothot = pd.DataFrame(scaler.fit_transform(nothot_feats),columns=nothot_feats.columns)
    cluster_nothot = kmeans.predict(scaled_nothot)
    nothot_df_final = not_hot
    nothot_df_final["Cluster"] = cluster_nothot
    nothot_df_final = nothot_df_final.drop(columns=['type', 'id', 'uri', 'track_href', 'analysis_url'], axis=1)

    
    nothot_df_final.to_csv('nothot_df_final.csv')
    return nothot_df_final





def cluster_user_song(user_song):
    
    
    song_uri = search_uri(user_song)
    song_df = create_df(song_uri)
    scaler = load('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/scalers/scaler.pkl')
    kmeans = load("/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/models/APIs9.pickle")
    user_feats = song_df[['danceability', 'energy', 'key', 'loudness', 'mode',
       'speechiness', 'acousticness', 'instrumentalness', 'liveness',
       'valence', 'tempo', 'duration_ms', 'time_signature']]
    scaled_user_song = pd.DataFrame(scaler.fit_transform(user_feats),columns=user_feats.columns)
    cluster_user_song = kmeans.predict(scaled_user_song)
    user_song_df_final = song_df
    user_song_df_final["Cluster"] = cluster_user_song

    return user_song_df_final







def get_audio_features(list_of_songs):
    import math
    import pickle
    import pandas as pd
    import sys
    import spotipy
    from spotipy.oauth2 import SpotifyClientCredentials
    from time import sleep
    
    song_ids = []

    black = {'danceability': "Null", 
           'energy': "Null", 
           'key': "Null",
           'loudness': "Null", 
           'mode':"Null", 
           'speechiness': "Null", 
           'acousticness': "Null", 
           'instrumentalness': "Null", 
            'liveness': "Null", 
            'valence': "Null", 
            'tempo': "Null", 
            'type': "Null", 
            'id': "Null", 
            'uri': "Null", 
            'track_href': "Null", 
            'analysis_url': "Null", 
            'duration_ms': "Null", 
            'time_signature': "Null"}
    
    keys = list(black.keys())
    
    df = pd.DataFrame()
    chunks = math.ceil(len(list_of_songs)/1000)
    for i in range(chunks): # chunks = 4 -> 0,1,2,3
        song_ids = []
        if ( i < chunks-1 ):
            j = i + 1
        else:
            j = len(list_of_songs)
        for index, song in enumerate(list_of_songs[1000*i:1000*j]): #[0:1000],[1000:2000],[2000:3000],[3000:]
            print("Looking for song: ",index)
            try:
                songs = sp.search(q=song, limit=1)
                song_ids.append(songs['tracks']['items'][0]['id'])
            except: # Si no esta no se para.
                print(song)
                song_ids.append("")
    
        print("Getting audio features")
        audio_feats = [sp.audio_features(song_id)[0] if ((song_id != None) and ( song_id != "")) else black for song_id in song_ids]
        name = "audio_feats_" + str(i) + ".pkl"
        with open(name, "wb") as handle:
            pickle.dump(audio_feats,handle)
        print("Created file: ",name)
        sleep(30)
        print('Sleeping for 30 seconds')





def get_pickels():
    import pickle
    import glob

    pkls = glob.glob("audio_feats_*.pkl")
    pkls.sort()
    pkls

    for pkl in pkls:
        try:
            print(pkl)
            with open(pkl, "rb") as handle:
                audio_feats = pickle.load(handle)
                audio_feats_df_nothot = (pd.DataFrame(audio_feats))
        except:
            print("Corrupted",pkl)
            continue

    return audio_feats_df_nothot

