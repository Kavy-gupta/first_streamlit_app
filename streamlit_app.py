'''
import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title('My moms new healthy dinner')
streamlit.header('Breakfast Favorite')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 Kale spinach and rocket smoothie')
streamlit.text('🐔 hard boiled free-ranged egg')
streamlit.text('🥑🍞 avcoda toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


#import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
 
# streamlit.dataframe(my_fruit_list)

# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

# Display the table on the page.
streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruityvice_data(this_fruit_choice):
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + this_fruit_choice)
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    return fruityvice_normalized

#new section to display fruityive api response
streamlit.header('Fruityvice Fruit Advicde!')
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("please select a fruit to get information")
  else:
    back_from_function =get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
   
except URLError as e:
  streamlit.error()



import snowflake.connector

streamlit.header("the fruit load list conatins:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
        my_cur.execute("select * from fruit_load_list")
        return my_cur.fetchall()
if streamlit.button('get fruit load list'):
    my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
    my_data_rows=get_fruit_load_list()
    streamlit.dataframe(my_data_rows)


#add_my_fruit = streamlit.text_input('enter fruit name to add')
#my_cur.execute("insert into fruit_load_list values(add_my_fruit)")
#streamlit.write('thanks for adding  ', add_my_fruit)

def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
        my_cur.execute("insert into fruit_load_list values('"+ new_fruit +"')")
        return "thanks for adding " + new_fruit
add_my_fruit=streamlit.text_input("what fruit would you like to add?")
if streamlit.button('add a fruit to the list'):
      my_cnx=snowflake.connector.connect(**streamlit.secrets["snowflake"])
      back_from_function=insert_row_snowflake(add_my_fruit)
      streamlit.text(back_from_function)
'''

import pandas as pd
import streamlit as st
#import plotly.express as plt
#mport matplotlib.pyplot as plt

df = pd.read_csv('https://raw.githubusercontent.com/Kavy-gupta/first_streamlit_app/main/veg_plant_height.csv')
#st.dataframe(df)
#fig=plt.bar(df,x=plant_name,y=Low_End_of_Range,orientation="h",)
st.bar_chart(df['Low_End_of_Range'])
            
