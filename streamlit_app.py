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
fruits_to_show = my_fruit_list.loc[fruits_selected] #displays data frame exclusively for the fruits_selected

streamlit.dataframe(fruits_to_show) #streamlit to present the dataframe pulled from S3 by pandas

#new section
streamlit.header('Fruityvice Fruit Advice')
fruit_choice = streamlit.text_input("What fruit would you like information about?", "Kiwi") #creating a variable to be passed into the fruityvice_response API request
streamlit.write("The user entered ", fruit_choice) 

#new section to display fruityvice api response
import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json()) #just writes the data on the screen

#take the json version of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#format output as a table
streamlit.dataframe(fruityvice_normalized)

#don't run anything past here while we trubleshoot
streamlit.stop()

import snowflake.connector

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The Fruit Load List Contains:")
streamlit.dataframe(my_data_rows)

# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input("What fruit would you like to add?", "jackfruit") 
streamlit.write("Thanks for adding ", add_my_fruit) 

#this will not work correctly 
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
