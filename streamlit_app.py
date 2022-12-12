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
streamlit.dataframe(my_fruit_list) #streamlit to present the dataframe pulled from S3 by pandas

