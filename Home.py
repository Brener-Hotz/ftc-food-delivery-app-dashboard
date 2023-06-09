# ==============
# Imports
# ==============

import pandas as pd
import aux_module
import folium
from folium.plugins import MarkerCluster
from PIL import Image
import streamlit as st
from streamlit_folium import folium_static

# ==============
# Data upload
# ==============

df = pd.read_csv('csv/zomato.csv')

# ==============
# Data cleanup
# ==============

df.drop_duplicates(keep = 'first', inplace = True)
df = df[df['Average Cost for two'] < 80000]
df.reset_index(drop = True, inplace = True)
df.dropna(inplace = True)

# ==============
# Data treatment
# ==============

df['country_name'] = df.apply(lambda x: aux_module.to_country_name(x['Country Code']), axis = 1)

df['Price range'] = df.apply(lambda x: aux_module.convert_price_range(x['Price range']), axis = 1)

df['Rating color'] = df.apply(lambda x: aux_module.to_color_name(x['Rating color']), axis = 1)

df['Cuisines'] = df.apply(lambda x: aux_module.split_cuisines(x['Cuisines']), axis = 1)

# ==============
# Streamlit Layout
# ==============

st.set_page_config(page_title = 'Home', page_icon = '🏠', layout = 'wide')

with st.sidebar:   
    st.markdown("<h1 style='text-align: center; color:black;'>pyFood</h1>", unsafe_allow_html=True)
    
    img = Image.open('logo.png')
    st.image(img)
    
    st.markdown("<h2 style='text-align: center; color:black;'>The perfect app to delivery your food.</h2>", unsafe_allow_html=True)
    
    st.write('---')
    
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    
    st.caption('Powered by DS Brener')
    
# Main page design

st.title('Welcome to pyFood!')

st.header('Please, meet all our restaurants around the world.')

st.subheader('We have the following metrics in our range:')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5, gap = 'small')
    
    col1.metric('Registered Restaurants', df.shape[0])
    col2.metric('Registered Countries', len(df['country_name'].unique()))
    col3.metric('Registered Cities', len(df['City'].unique()))
    col4.metric('Total of Evaluations', f"{df['Votes'].sum():,}")
    col5.metric('Types of Cuisines', len(df['Cuisines'].unique()))

st.write('---')

with st.container():
    col1, col2, col3 = st.columns([1,3,1], gap = 'small')
    
    my_map = folium.Map(location = [25.436298, 78.567352], zoom_start = 2)
    
    mkr_cluster = MarkerCluster(name='Markers').add_to(my_map)
    
    df.apply(lambda row: folium.Marker(location = [row['Latitude'], row['Longitude']], 
                                       popup = row['Restaurant Name'],
                                       icon = folium.Icon(color = 'red', icon = 'fa-cutlery', prefix = 'fa')).add_to(mkr_cluster), axis = 1)
    
    with col2:
        folium_static(my_map, width = 900)
