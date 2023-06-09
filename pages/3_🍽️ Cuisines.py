# ==============
# Imports
# ==============

import pandas as pd
from PIL import Image
import streamlit as st
import plotly.express as px
import aux_module

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

st.set_page_config(page_title = 'Cuisines', page_icon = '🍽️', layout = 'wide')

# ==============
# Sidebar
# ==============

with st.sidebar:   
    st.markdown("<h1 style='text-align: center; color:black;'>pyFood</h1>", unsafe_allow_html=True)
    
    img = Image.open('logo.png')
    st.image(img)
    
    st.markdown("<h2 style='text-align: center; color:black;'>Cuisines View</h2>", unsafe_allow_html=True)
    
    st.write('---')
    
    st.subheader('Filter')
    
    country_filter = st.multiselect('Please, select the countries you are looking for.', 
                            options = list(df['country_name'].unique()), 
                            default = ['India', 'United States of America', 'England'])
    
    st.markdown('##')
    
    cuisines_range = st.slider(
        'How many restaurants do you want to see?',
        0,
        20,
        10
    )

    st.markdown('##')
    
    st.caption('Powered by DS Brener')

# ==============
# Content
# ==============

st.title('Cuisines Overview Dashboard.')
st.header('Our restaurants have a bunch of diferent types of cuisines. Below you can see their ratings.')

with st.container():
    col1, col2, col3, col4, col5 = st.columns(5)
    
    df_aux = (
        df[['Restaurant ID', 'Restaurant Name', 'Cuisines', 'Aggregate rating']]
        .groupby(['Restaurant ID', 'Restaurant Name', 'Cuisines']).max()
        .sort_values(['Aggregate rating'], ascending = False)    
    )
    
    df_aux = df_aux[df_aux['Aggregate rating'] == 4.9]
    
    df_aux = df_aux.sort_values(['Restaurant ID']).reset_index().head(5)
    
    with col1:
        st.metric(f"{df_aux.loc[0, 'Cuisines']}: {df_aux.loc[0, 'Restaurant Name']}", '4.9/5.0')
    
    with col2:
        st.metric(f"{df_aux.loc[1, 'Cuisines']}: {df_aux.loc[1, 'Restaurant Name']}", '4.9/5.0')
        
    with col3:
        st.metric(f"{df_aux.loc[2, 'Cuisines']}: {df_aux.loc[2, 'Restaurant Name']}", '4.9/5.0')
    
    with col4:
        st.metric(f"{df_aux.loc[3, 'Cuisines']}: {df_aux.loc[3, 'Restaurant Name']}", '4.9/5.0')
    
    with col5:
        st.metric(f"{df_aux.loc[4, 'Cuisines']}: {df_aux.loc[4, 'Restaurant Name']}", '4.9/5.0')

st.markdown('---')

with st.container():
    col1, col2, col3 = st.columns([1,4,1])
    
    with col2:
        st.header(f'Best Restaurants based on your filter')
        
        df_aux = df[df['country_name'].isin(country_filter)]
        
        df_aux = (
            df_aux[['Restaurant ID', 'Restaurant Name', 'country_name','City', 'Cuisines', 'Average Cost for two', 'Aggregate rating', 'Votes']]
            .groupby(['Restaurant ID', 'Restaurant Name', 'Cuisines']).max()
            .sort_values(['Aggregate rating'], ascending = False))
        
        df_aux = df_aux[df_aux['Aggregate rating'] == 4.9]
        
        df_aux = df_aux.sort_values(['Restaurant ID']).reset_index().head(cuisines_range)
        
        df_aux
        
st.markdown('---')

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader(f'Top {cuisines_range} best type of Cuisines')
        
        df_aux = df[df['country_name'].isin(country_filter)]
        
        df_aux = (
            df_aux[['Cuisines', 'Aggregate rating']]
            .groupby(['Cuisines']).mean()
            .sort_values(['Aggregate rating'], ascending = False)
            .reset_index()
        )
        
        fig = px.bar(
            df_aux.head(cuisines_range),
            x = 'Cuisines',
            y = 'Aggregate rating',
            labels = {
                'Aggregate rating': 'Mean of Aggregate Rating'
            },
            height = 400,
            text_auto = '.3s',
            template = 'plotly_white'
        )
        
        fig.update_traces(textposition = 'inside')
        
        fig.update_layout(
            plot_bgcolor = 'rgba(0,0,0,0)'            
        )
        
        st.plotly_chart(fig, use_container_width = True, theme = None)
        
    with col2:
        st.subheader(f'Top {cuisines_range} worst type of Cuisines')
        
        df_aux = df[df['country_name'].isin(country_filter)]
        
        df_aux = (
            df_aux[['Cuisines', 'Aggregate rating']]
            .groupby(['Cuisines']).mean()
            .sort_values(['Aggregate rating'])
            .reset_index()
        )
        
        fig = px.bar(
            df_aux.tail(cuisines_range),
            x = 'Cuisines',
            y = 'Aggregate rating',
            labels = {
                'Aggregate rating': 'Mean of Aggregate Rating'
            },
            height = 400,
            text_auto = '.3s',
            template = 'plotly_white'
        )
        
        fig.update_traces(textposition = 'inside')
        
        fig.update_layout(
            plot_bgcolor = 'rgba(0,0,0,0)'            
        )
        
        st.plotly_chart(fig, use_container_width = True, theme = None)
    