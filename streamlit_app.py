import streamlit
streamlit.title('My moms new healthy dinner')
streamlit.header('Breakfast Favorite')
streamlit.text('🥣 omega 3 and blueberry oatmeal')
streamlit.text('🥗 Kale spinach and rocket smoothie')
streamlit.text('🐔 hard boiled free-ranged egg')
streamlit.text('🥑🍞 avcoda toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
