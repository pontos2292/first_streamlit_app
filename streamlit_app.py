import streamlit
import pandas

streamlit.title("My Parent's New Healthy Diner")
streamlit.header("Breakfast Favorites")
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text("🥑🍞 Avocado Toast")

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt") #pandas to import csv with macros from AWS S3

# Set index for pick list to the actual fruit name
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put a pick list here so they can pick the fruit they want to include 
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado', 'Strawberries']) #passed avocado and strawberries as examples
fuits_to_show = my_fruit_list.loc[fruits_selected] #displays data frame exclusively for the fruits_selected

streamlit.dataframe(fruits_to_show) #streamlit to present the dataframe pulled from S3 by pandas

