import streamlit as st

# Python libraries
import pandas as pd
import random
import pickle
import streamlit as st
import requests
import json
import spotipy as sp
from time import sleep
from random import sample
from spotipy.oauth2 import SpotifyClientCredentials
from turtle import title
#sys.path.insert(1, '/Users/mariasoriano/Desktop/Ironhack/Spotipy/config.py')
from spotipy import SpotifyClientCredentials
from sklearn.preprocessing import StandardScaler



# User module files
from eda import plots
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from functions import *




# Spotify credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id= client_id,
                                                           client_secret= client_secret_id))


## --- DATA
hot100 = pd.read_csv('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/data/feats_concated_top100.csv') # hot100 feats concated
nothot_songs = pd.read_csv('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/data/feats_concated_nothot.csv') # nothotsongs feats concated
clustered_nothot_final = pd.read_csv('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/cluster_nothot.csv') # nothotsongs clustered
clustered_hot = pd.read_csv('/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/data/clustered_hot100.csv') # hot100 clustered



## --- FUNCTIONS


## --- ANIMATIONS 
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
      return None
    return r.json()



lottie_music = load_lottieurl('https://assets4.lottiefiles.com/packages/lf20_cbjntxzb.json')
#/Users/mariasoriano/Desktop/Ironhack/lab-web-scraping-single-page/src/lottie/lf30_editor_ofnszbqo.json
#https://assets3.lottiefiles.com/packages/lf20_vixkj2dq.json




def song_recommender_final(title_of_song):

        if title_of_song in hot100['title'].tolist():


          hot100_clustered = cluster_top_100(hot100) 
          title_cluster = hot100_clustered['Cluster'][hot100_clustered["title"] == title_of_song].values[0]
          matching_songs = hot100_clustered[hot100_clustered['Cluster'] == title_cluster]
          matched_song = matching_songs.sample()
          #cover = get_cover(matched_song)
          #searched_url = search_url(matched_song)
          return f"We recommend you try {matched_song['title'].values[0]} by {matched_song['artist'].values[0]}"

        else:

          song_clustered_df = cluster_user_song(title_of_song) #create df from user's song that contains cluster
          user_song_cluster = song_clustered_df['Cluster'].values[0] #from the user df get the cluster value
          # so far we have: df user with cluster / only cluster value from user song
          #nothot_songs_clustered = cluster_nothot(nothot_songs) #cluster the nothot songs
          matching_songs = clustered_nothot_final[clustered_nothot_final['Cluster'] == user_song_cluster]
          matched_song = matching_songs.sample()
          return f"We recommend you try {matched_song['title'].values[0]} by {matched_song['artist'].values[0]}  "





def main():
  
    #############  
    # Main page #
    #############   

  st.set_page_config(page_title="GNOD Song Recommender", page_icon=":headphones:", layout="wide")

    
    #if ( choice == 'Home' ):
    

    #### ---- not sure if I will add a menu or no ---- ####
  selected = option_menu(
      menu_title=None,
      options=['Home', 'Stop'],
      icons=['house', 'stop-circle'],
      menu_icon='list',
      default_index=0,
      orientation='horizontal',
      styles={
        "container": {"padding": "0!important", "background-color": "mediumpurple"},
        "icon": {"color": "black", "font-size": "20px"}, 
        "nav-link": {"font-size": "14px", "text-align": "left", "margin":"0px", "--hover-color": "lavender"},
        "nav-link-selected": {"background-color": "#D7B0F5"},
      }
    )



  if selected == 'Home':

      c1 = st.container()
      with c1:
        col1, col2, col3 = st.columns(3)
        with col2:  
          st.write("#")
          st.write("#")
          st.write("#")

          st.title('..GNOD presents..')
          st.title('your NEW favorite song recommender')
          #st.markdown("<h2 style='text-align: center; color: black;'>GNOD presents...</h2>", unsafe_allow_html=True)
          #st.markdown("<h1 style='text-align: center; color: black;'>your NEW favorite song recommender</h1>", unsafe_allow_html=True)
          st_lottie(lottie_music, height=100, key='music')
      #st.markdown("<h5 style='text-align: center; color: black;'>Web scrapping / API project</h5>", unsafe_allow_html=True)
      #st.markdown("<h6 style='text-align: center; color: black;'>Date: March 2022</h6>", unsafe_allow_html=True)
      #st.markdown("<h6 style='text-align: center; color: black;'>Created by: Maria Soriano 👋🏼</h6>", unsafe_allow_html=True)
      #st.image('/Users/mariasoriano/Desktop/Soriano Tech/jardín digital/podcast_cover/stech95.jpg', width=120) 


      user_option = False
      st.markdown("""---""")

      c2 = st.container()
      with c1:
        col1, col2, col3 = st.columns(3)

        with col2:
          title = st.text_input('Enter the title of a song', '')
          search_button = st.button('Search')

          if search_button:
            recommended_song = song_recommender_final(title)
            st.write(recommended_song)

         
          st.write("#")
          st.write("#")
          st.write("#")
         # with st.spinner(text='Finding your next favorite song...'):
            #here I should use a function to search for a song
      #while (user_option == True):
        #st.markdown(
        #  f"""
        #  * Title : {title}
        #"""
        #)

        c3 = st.container()
        with c2:
          col1, col2, col3, col4, col5 = st.columns(5)
          with col1:
            image_animal = search_image('Heat Waves')
            st.image(image_animal)
          with col2:
            image_justin = search_image('Peaches')
            st.image(image_justin)
          with col3:
            image_adele = search_image('Easy On Me')
            st.image(image_adele)
          with col4:
            image_stay = search_image('STAY')
            st.image(image_stay)
          with col5:
            image_shawn = search_image('Bam Bam')
            st.image(image_shawn)

          st.write("#")
          st.write("#")
          st.write("#")
          st.write("#")

          c4 = st.container()
          with c4:
            col1, col2 = st.columns(2)

            with col1:
              st.subheader('The Hot 100')

            with col2:
              st.subheader('Other songs you have not heard about (yet)')
           


      
      ## ---- function pseudocode ---- ##


      



        #else:

          
      # 1. get the song uri ------ done
      # 2. get the audio features ------ done
      # 3. create a df ------ done
      # 4. load the scaler and apply to the audio features ----- done
      # 5. load and use the model to predict the cluster ------ done
      # 6. if statement.
        # 7. if song isin hot100 
            # 7.1 filter by rows in which the cluster is the same as user's song
            # 7.2 display a random hot100 song

        # 8. else is in nothotlist songs
            # 8.1 filter by rows in which the cluster is the same as user's song
            # 8.1 display a random nothot song


      #selection= input(¿Deseas otra recomendacion?:)


  



      
  elif ( selected == 'Plots and more' ):
    plots()
    pass
    
  else:
    st.stop()
      
    
main()




















