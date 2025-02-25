from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

with st.echo(code_location='below'):
    
    # Format the header.
    st.title('My Parents New Healthy Diner')
    st.header('Breakfast Menu')
             
    st.text('Omega 3 & Blueberry Oatmeal')
    st.text('Kale, Spinach & Rocket Smoothie')
    st.text('Hard-Boilded Fre-Range Egg')
    
    # Get data sample from Snowflake AWS S3 bucket.
    my_fruit_list = pd.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
    my_fruit_list = my_fruit_list.set_index('Fruit')
    
    # Add multi-select picker.
    fruits_selected = st.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries'])
    
    # Render dataframe.
    fruits_to_show = my_fruit_list.loc[fruits_selected]
    st.dataframe(fruits_to_show)
    
    
    
    
   
