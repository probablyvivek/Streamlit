#Import the libraries
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from PIL import Image

#get the data
df = pd.read_csv("pokemon_data.csv")
df.head()

#data manipulation function
def data_manipulation():
    df['Name'] = df['Name'].str.lower()
    df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
    df['Legendary Status'] = df['Legendary'].map({True: 'Legendary', False: 'Not Legendary'})
data_manipulation()

st.set_page_config(page_title='Pokemon Stats', page_icon=':pokemon:')

#Home Button Function
def home():
    st.sidebar.info('Welcome to the Pokemon Stats App')
    from PIL import Image
    image = os.path.join('./Images', 'head.png')
    st.image(image,use_column_width=True)    
    image2 = os.path.join('./Images', 'pokemon.jpeg')
    st.image(image2, use_column_width=True)
    

#search Function
def search():
    st.sidebar.title('Search your fav Pokemon')
    st.sidebar.markdown('[Wiki Page](https://bit.ly/3grjJGI)')
    name = st.sidebar.text_input('Enter the name and click submit to get the stats: ')
    name = name.lower()
    #if name is blank, display error
    if name == '':
        st.subheader('You gotta enter a Name!!!')
    #if name is not found, display error
    elif name not in df['Name'].unique():
        st.subheader('Pokemon not found!!!')
    #if name is found, display stats
    else:
        if st.sidebar.button('Submit'):
            st.title('Here are the stats for ' + name.title())
            st.text('HP: ' + str(df.loc[df['Name'] == name, 'HP'].values[0]))
            st.text('Attack: ' + str(df.loc[df['Name'] == name, 'Attack'].values[0]))
            st.text('Defense: ' + str(df.loc[df['Name'] == name, 'Defense'].values[0]))
            st.text('Sp. Atk: ' + str(df.loc[df['Name'] == name, 'Sp. Atk'].values[0]))
            st.text('Sp. Def: ' + str(df.loc[df['Name'] == name, 'Sp. Def'].values[0]))
            st.text('Speed: ' + str(df.loc[df['Name'] == name, 'Speed'].values[0]))
            st.subheader('Total: ' + str(df.loc[df['Name'] == name, 'Total'].values[0]))
            st.subheader('Status: ' + str(df.loc[df['Name'] == name, 'Legendary Status'].values[0]))
            image = os.path.join('./Images', name + '.png')
            st.image(image,use_column_width=True)


#sidebar function
def sidebar():
    menu = ['Home', 'Search']
    choice = st.sidebar.selectbox('',menu)
    if choice == 'Home':
        home()
    elif choice == 'Search':
        search()
sidebar()
