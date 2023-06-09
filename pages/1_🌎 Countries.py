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

st.set_page_config(page_title = 'Countries', page_icon = '🌎', layout = 'wide')

# ==============
# Sidebar
# ==============

with st.sidebar:   
    st.markdown("<h1 style='text-align: center; color:black;'>pyFood</h1>", unsafe_allow_html=True)
    
    img = Image.open('logo.png')
    st.image(img)
    
    st.markdown("<h2 style='text-align: center; color:black;'>Countries View</h2>", unsafe_allow_html=True)
    
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

st.title('Countries Overview Dashboard.')
st.header('Below you can visualize some information of our records separated by country.')
st.markdown('---')


# Plot 1st chart

df_aux = (df[df['country_name'].isin(filter)][['country_name','City']]
          .groupby(['country_name']).nunique()
          .sort_values(['City'], ascending = False)
          .reset_index())
df_aux.rename(columns = {'City': 'total_cities'}, inplace = True)

with st.container():
    st.subheader('Total of Cities per Country')
    
    fig = px.bar(df_aux, 
                 x = 'country_name', 
                 y = 'total_cities',
                 labels = {'country_name': 'Country Name',
                           'total_cities': 'Total Cities'},
                 width = 1530,
                 height = 300,
                 text_auto = 'total_cities',
                 template = 'plotly_white')
    
    fig.update_traces(textposition = 'inside')
    
    fig.update_layout(plot_bgcolor = 'rgba(0,0,0,0)')
    
    st.plotly_chart(fig, theme = None)

st.markdown('---')

# Plot 2nd chart

df_aux = (df[df['country_name'].isin(filter)][['country_name', 'Restaurant ID']]
          .groupby('country_name').count()
          .sort_values('Restaurant ID', ascending = False)
          .reset_index())
df_aux.rename(columns = {'Restaurant ID': 'total_restaurants'}, inplace = True)

with st.container():
    st.subheader('Total of restaurants registered per Country')

    fig = px.bar(df_aux, 
                 x = 'country_name',
                 y = 'total_restaurants',
                 labels = {'country_name' : 'Country Name',
                           'total_restaurants': 'Total Restaurants'},
                 width = 1530,
                 height = 360,
                 text_auto = 'total_restaurants',
                 template = 'plotly_white')
    
    fig.update_traces(textposition = 'inside')
    
    fig.update_layout(plot_bgcolor = 'rgba(0,0,0,0)')
    
    st.plotly_chart(fig, theme = None)

st.markdown('---')

# Plot 3rd/4th chart

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader('Average Evaluation per Country')
        
        df_aux = (df[df['country_name'].isin(filter)][['country_name', 'Votes']]
                  .groupby(['country_name']).mean()
                  .sort_values(['Votes'], ascending = False)
                  .reset_index())
        
        df_aux['Votes'] = df_aux['Votes'].round(2)
        
        fig = px.bar(df_aux, 
                     x = 'country_name',
                     y = 'Votes',
                     labels = {'country_name': 'Country Name',
                               'Votes': 'Average Evaluation'},
                     height = 410,
                     text_auto = '.4s',
                     template = 'plotly_white')
        
        fig.update_traces(textposition = 'inside')
        
        fig.update_layout(plot_bgcolor = 'rgba(0,0,0,0)')
        
        st.plotly_chart(fig, use_container_width = True, theme = None)
    
    with col2:
        st.subheader('Average Cost for Two per Country')
        
        df_aux = (df[df['country_name'].isin(filter)][['country_name', 'Average Cost for two']]
                  .groupby(['country_name']).mean()
                  .sort_values(['Average Cost for two'], ascending = False)
                  .reset_index())
        
        df_aux['Average Cost for two'] = df_aux['Average Cost for two'].round(2)
        
        fig = px.bar(df_aux,
                     x = 'country_name',
                     y = 'Average Cost for two',
                     labels = {
                         'country_name': 'Country Name',
                         'Average Cost for two': 'Average Cost for Two'
                     },
                     height = 410,
                     text_auto = '.4s',
                     template = 'plotly_white')
        
        fig.update_traces(textposition = 'inside')
        
        fig.update_layout(plot_bgcolor = 'rgba(0,0,0,0)')
        
        st.plotly_chart(fig, use_container_width = True, theme = None)
        