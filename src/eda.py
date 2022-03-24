
def plots():
    # Import python modules 
    import pandas as pd
    import numpy as np
    import streamlit as st
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly as plt
    import plotly.express as px
    import plotly.graph_objects as go
    from streamlit_lottie import st_lottie
    from streamlit_option_menu import option_menu
    import dash
    from dash import Dash, dcc, html, Input, Output
    #from dash import Dash, dcc, html, Input, Output

    import json
    #import plotly.io as pio


    
    sns.set_theme(style="darkgrid")

    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})





## --- CONTAINER 1 STARTS HERE --- ##
# -> Evolution of the absolute hashrate (monhtly average) by country 2019-2021
#        -> line plot
#        -> bar plot

    
    padding = 20
    st.markdown(f""" <style>
        .reportview-container .main .block-container{{
            padding-top: {padding}rem;
            padding-right: {padding}rem;
            padding-left: {padding}rem;
            padding-bottom: {padding}rem;
        }} </style> """, unsafe_allow_html=True)

    c1 = st.container()

    with c1:
        st.markdown("<h1 style='text-align: center; color: black;'>📈 Evolution of the absolute hashrate (monthly average) by country from 2019 to 2021</h1>", unsafe_allow_html=True)

        col1,col2 = st.columns(2)

        with col1:
            area = px.line(bitcoin_mining, x="date", y='monthly_absolute_hashrate_EH/S', color='country',
                        labels={
                             "date": "Date",
                             "monthly_absolute_hashrate_EH/S": "Absolute Hashrate (monthly average)",
                             "country": "Country"
                         },
                         color_discrete_sequence=px.colors.qualitative.Pastel,
                         height=400,
                         width=600)
            st.plotly_chart(area) 

        with col2:
            pie = px.pie(bitcoin_mining, values='monthly_absolute_hashrate_EH/S', names='country',
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        height=500,
                        width=500)
            st.plotly_chart(pie)
            #bar = px.bar(bar_df, x='country', y='monthly_absolute_hashrate_EH/S', color = 'country',
            #            labels = {
            #                'monthly_absolute_hashrate_EH/S':'Absolute Hashrate (monthly average)',
            #               'country':'Country'
            #           },
            #            color_discrete_sequence= px.colors.sequential.Pastel,
            #            height=400,
            #            width=600)
            #st.plotly_chart(bar) 




## --- CONTAINER 2 STARTS HERE --- ##
# -> World Map showing Absolute Hashrate by country
#        -> choropleth map


    c2 = st.container()

    with c2:
        st.markdown("<h1 style='text-align: center; color: black;'>🗺 World Map showing Absolute Hashrate by country</h1>", unsafe_allow_html=True)



        ## --- Choropleth Map code STARTS here --- ##

        countries = [(i,world_map['features'][i]['properties']['ADMIN']) for i in range(len(world_map['features']))]
        index_list = [42,108,191,107,61,238]
        country_list = ['Mainland China','Iran, Islamic Rep.','Russian Federation','Ireland *','Germany *','United States']

        def replace_countries(df, index_list, countries_list ):
            df2 = df.copy()
            for elem in zip(index_list,country_list):
                df2['features'][elem[0]]['properties']['ADMIN'] = elem[1]
            return df2

        new_json = replace_countries(world_map, index_list, country_list)   



        world_map_id = {}
        
        for feature in world_map['features']:
            feature['id'] = feature['properties']['ADMIN']
            world_map_id[feature['properties']['ISO_A3']] = feature['id']

        col1, col2, col3 = st.columns(3)

        with col2: 
            ## -- dropdown choropleth x year -- ##
            year_options = sum_df['year'].unique().tolist()
            year = st.selectbox('Which year would you like to see?', year_options, 0)
            sum_df = sum_df[sum_df['year']==year]

            ## -- choropleth fig -- ##
            fig_mo = px.choropleth(sum_df, geojson=world_map, locations='country',
                                    color='monthly_absolute_hashrate_EH/S',
                                    labels={'monthly_absolute_hashrate_EH/S':'Monthly Absolute Hashrate'}
                                    )
            fig_mo.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


            st.plotly_chart(fig_mo) 

        ## --- Coropleth Map code ENDS here --- ##


        



## --- CONTAINER 3 STARTS HERE --- ##
# -> Absolute Hashrate by country per year (2019, 2020, 2021)
#        -> select box
#        -> bar plot


    c3 = st.container()

    with c3:
        st.markdown("<h1 style='text-align: center; color: black;'>🗓 Absolute Hashrate by country per year</h1>", unsafe_allow_html=True)

        year_options = bitcoin_mining['year'].unique().tolist()
        #year = st.selectbox('Which year would you like to see?', year_options, 0)
        #bitcoin_mining = bitcoin_mining[bitcoin_mining['year']==year]

        bitcoin_mining_plot = px.bar(bitcoin_mining, x='country', y='monthly_absolute_hashrate_EH/S',
                    labels={
                                "country": "Country",
                                "monthly_absolute_hashrate_EH/S": "Absolute Hashrate (monthly average)",
                            },
                        color='country',
                        animation_frame='date', animation_group='country',
                        color_discrete_sequence=px.colors.qualitative.Pastel,
                        height=600,
                        width=1000)
        st.plotly_chart(bitcoin_mining_plot)



## --- CONTAINER 4 STARTS HERE --- ##
# -> China's ups and downs
#        -> line plot
#        -> area plot
#        -> choropleth map

    c4 = st.container()

    with c4:

        st.markdown("<h1 style='text-align: center; color: black;'>🇨🇳 China's ups and downs</h1>", unsafe_allow_html=True)
        st_lottie(lottie_rolla, height=150, key='coding')

        col1, col2, col3 = st.columns(3)

        with col1:
            china_line = px.line(china_mining, x="Date", y='Share of Chinese hashrate', color='Province',
                 labels={
                         "Date": "Date",
                         "Share of Chinese hashrate": "Share of Chinese Hashrate by Province",
                         "Province": "Province"
                     },
                     title='Evolution of Chinese shared hashrate (monthly average) by province from 2019 to 2021',
                     color_discrete_sequence=px.colors.qualitative.Pastel)
            st.plotly_chart(china_line)

            china_mining_plot = px.bar(china_mining, x='Province', y='Share of Chinese hashrate',
                        labels={
                                    "Date": "Date",
                                    "Share of Chinese Hashrate by Province": "Share of Chinese Hashrate by Province",
                                },
                            color='Province',
                            animation_frame='Date', animation_group='Province',
                            color_discrete_sequence=px.colors.qualitative.Pastel,
                            height=600,
                            width=1100)
            st.plotly_chart(china_mining_plot)

        with col3:
            #st.write('#')
            st.write('#')
            st.subheader('Seasons')
            st.write('Sichuan and Xinjiang were well known locations for mining Bitcoin because of their cheap hydropower. ')
            st.write('The rainy season creates excessive hydropower, which makes electricity cheaper and so mining is more profitable.')
            st_lottie(lottie_hydro, height=250, key='hydro')
        #china_line = px.line(bitcoin_mining[(bitcoin_mining['country']=='Mainland China')], x="date", y='monthly_absolute_hashrate_EH/S', color='country')
        #st.plotly_chart(china_line)


## --- CONTAINER 5 STARTS HERE --- ##
# -> Bonus: Mining Pools info 2019
#        -> pie plot


    c5 = st.container()
    with c5:

        st.markdown("<h1 style='text-align: center; color: black;'>⛏ Emerging mining locations</h1>", unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col2:
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st.write("#")
            st_lottie(lottie_up, height=200, key='up')

        with col1:
            #mask = sum_df['country'] == 'United States'

            # dropdown #
            #year_options_two = sum_df['year'].unique().tolist()
            #year_two = st.selectbox('Which year would you like to see?', year_options_two, 0)
            #sum_df_two = sum_df[sum_df['year']==year_two]


            #usa = px.bar(sum_df[sum_df['country'].isin(['United States','Kazakhstan', 'Mainland China', 'Russian Federation'])], x='country', y='monthly_absolute_hashrate_EH/S',              
            #    color = 'country',
            #    labels = {  'monthly_absolute_hashrate_EH/S':'Absolute Hashrate (monthly average)',
            #                 'country':'Country'
            #            },
            #    animation_frame='year', animation_group='country',
            #    color_discrete_sequence=px.colors.qualitative.Pastel)

            #st.plotly_chart(usa)

            sum_df_filtered = sum_df[sum_df['country'].isin(['United States','Kazakhstan', 'Mainland China', 'Russian Federation'])]
            #st.dataframe(sum_df_filtered)

            #emerging = px.bar(sum_df_filtered,
            #                x='country', y='monthly_absolute_hashrate_EH/S',
            #                labels={
            #                        'monthly_absolute_hashrate_EH/S':'Absolute Hashrate (monthly average)',
            #                        'country':'Country'
            #                    },
            #                color='country',
            #                color_discrete_sequence=px.colors.qualitative.Pastel,
            #                animation_frame='date',
            #                animation_group='country')
            #st.plotly_chart(emerging)
            #st.dataframe(bitcoin_mining)

            bitcoin_mining_f = bitcoin_mining[bitcoin_mining['country'].isin(['United States','Kazakhstan', 'Mainland China', 'Russian Federation'])]
            prueba = px.bar(bitcoin_mining_f,
                            x='country', y='monthly_absolute_hashrate_EH/S',
                            labels={
                                    'monthly_absolute_hashrate_EH/S':'Absolute Hashrate (monthly average)',
                                    'country':'Country'
                                },
                            color='country',
                            color_discrete_sequence=px.colors.qualitative.Pastel,
                            animation_frame='date',
                            animation_group='country')
            st.plotly_chart(prueba)
        


## --- CONTAINER 6 STARTS HERE --- ##
# -> Bonus: Mining Pools info 2019
#        -> pie plot


    #c6 = st.container()
    #with c6:
        #st.markdown("<h1 style='text-align: center; color: black;'>🛠 Bonus: Mining Pools info 2019</h1>", unsafe_allow_html=True)



    hashrate_2020 = px.bar(hashrate_2020, x='country', y='monthly_absolute_hashrate_EH/S',
                labels={
                         "country": "Country",
                         "monthly_absolute_hashrate_EH/S": "Absolute Hashrate (monthly average)",
                     },
                 color='country',
                 title='Aboslute Hashrate (monthly average) in 2020')
    
    hashrate_2021 = px.bar(hashrate_2021, x='country', y='monthly_absolute_hashrate_EH/S',
                labels={
                         "country": "Country",
                         "monthly_absolute_hashrate_EH/S": "Absolute Hashrate (monthly average)",
                     },
                 color='country',
                 title='Aboslute Hashrate (monthly average) in 2021')

            
       #fig2 = px.bar(data, y='Region', x='Debt', color = 'Status')

        #st.pyplot(fig1) # Seaborn or matploib
    #st.plotly_chart(area) # Plotly
    #st.plotly_chart(bar) # Plotly
    #st.plotly_chart(hashrate_2019) # Plotly
    #st.plotly_chart(hashrate_2020) # Plotly
    #st.plotly_chart(hashrate_2021) # Plotly