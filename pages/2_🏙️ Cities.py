# ==============
# Imports
# ==============

import pandas as pd
from PIL import Image
import streamlit as st
import aux_module
import plotly.express as px

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

st.set_page_config(page_title = 'Cities', page_icon = '🏙️', layout = 'wide')

# ==============
# Sidebar
# ==============

with st.sidebar:   
    st.markdown("<h1 style='text-align: center; color:black;'>pyFood</h1>", unsafe_allow_html=True)
    
    img = Image.open('logo.png')
    st.image(img)
    
    st.markdown("<h2 style='text-align: center; color:black;'>Cities View</h2>", unsafe_allow_html=True)
    
    st.write('---')
    
    st.subheader('Filter')
    filter = st.multiselect('Please, select the countries you are looking for.', 
                            options = list(df['country_name'].unique()), 
                            default = ['India', 'United States of America', 'England'])
    
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    st.markdown('##')
    
    st.caption('Powered by DS Brener')

# ==============
# Content
# ==============

st.title('Cities Overview Dashboard.')
st.header('Below you can visualize some important information about the cities in our records.')
st.markdown('---')


# Plot 1st chart

df_aux = (df[df['country_name'].isin(filter)][['country_name', 'City', 'Restaurant ID']]
          .groupby(['country_name', 'City']).count()
          .sort_values(['Restaurant ID'], ascending = False)
          .reset_index())

df_aux.rename(columns = {
                         'country_name': 'Country', 
                         'Restaurant ID': 'number_of_restaurants'
              }, inplace = True)

with st.container():
    st.subheader('Top 10 cities with most restaurants')
    
    fig = px.bar(
                 df_aux.head(10),
                 x = 'City',
                 y = 'number_of_restaurants',
                 labels = {
                           'number_of_restaurants': 'Number of Restaurants'
                 },
                 color = 'Country',
                 width = 1530,
                 height = 300,
                 text_auto = 'number_of_restaurants',
                 template = 'plotly_white'
    )
    
    fig.update_traces(textposition = 'inside')
    
    fig.update_layout(plot_bgcolor = 'rgba(0,0,0,0)')
    
    st.plotly_chart(fig, theme = None)
    
st.markdown('---')

# Plot 2nd/3rd charts

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Top 7 cities with restaurants average rating over 4.')
        
        df_aux = (df[(df['Aggregate rating'] > 4) & (df['country_name'].isin(filter))][['country_name', 'City', 'Restaurant ID']]
            .groupby(['country_name', 'City']).count()
            .sort_values(['Restaurant ID'], ascending = False)
            .reset_index()
        )
        
        df_aux.rename(
            columns = {
                'country_name': 'Country',
                'Restaurant ID': 'Quantity of Restaurants'
                      },
            inplace = True
        )
        
        fig = px.bar(
            df_aux.head(7),
            x = 'City',
            y = 'Quantity of Restaurants',
            color = 'Country',
            height = 300,
            text_auto = 'Quantity of Restaurants',
            template = 'plotly_white'
        )
        
        fig.update_traces(
            textposition = 'inside'
        )
        
        fig.update_layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            xaxis = {
                'categoryorder': 'total descending'
            }
        )
        
        st.plotly_chart(fig, use_container_width = True, theme = None)
        
    with col2:
        st.subheader('Top 7 cities with restaurants average rating under 2.5.')
        
        df_aux = (df[(df['Aggregate rating'] < 2.5) & (df['country_name'].isin(filter))][['country_name','City', 'Restaurant ID']]
            .groupby(['country_name','City']).count()
            .sort_values(['Restaurant ID'], ascending = False)
            .reset_index()
        )
        
        df_aux.rename(
            columns = {
                'country_name': 'Country Name',
                'Restaurant ID': 'Quantity of Restaurants'
            },
            inplace = True
        )
        
        fig = px.bar(
            df_aux.head(7),
            x = 'City',
            y = 'Quantity of Restaurants',
            color = 'Country Name',
            height = 300,
            template = 'plotly_white',
            text_auto = 'Quantity of Restaurants'
        )
        
        fig.update_traces(
            textposition = 'inside'
        )
        
        fig.update_layout(
            plot_bgcolor = 'rgba(0,0,0,0)',
            xaxis = {
                'categoryorder': 'total descending'
            }
        )
        
        st.plotly_chart(
            fig, use_container_width = True, theme = None
        )
        
st.markdown('---')

# Plot 4th chart

with st.container():
    st.subheader('10 cities with most distinct types of cuisines')
    
    df_aux = (
        df[df['country_name'].isin(filter)][['country_name', 'City', 'Cuisines']]
        .groupby(['country_name', 'City']).nunique()
        .sort_values(['Cuisines'], ascending = False)
        .reset_index()
    )
    
    df_aux.rename(
        columns = {
            'country_name': 'Country Name'
        },
        inplace = True
    )
    
    fig = px.bar(
        df_aux.head(10),
        x = 'City',
        y = 'Cuisines',
        color = 'Country Name',
        width = 1530,
        height = 300,
        template = 'plotly_white',
        text_auto = 'Cuisines'
    )
    
    fig.update_traces(
        textposition = 'inside'
    )
    
    fig.update_layout(
        plot_bgcolor = 'rgba(0,0,0,0)',
        xaxis = {
            'categoryorder': 'total descending'
        }
    )
    
    st.plotly_chart(
        fig, theme = None
    )
    