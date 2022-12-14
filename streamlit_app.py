import streamlit
import pandas
import snowflake.connector
import requests
from urllib.error import URLError

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

#create the repeatable code block / function
def get_fruityvice_data(fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized


#new section
streamlit.header('Fruityvice Fruit Advice')
try:
  fruit_choice = streamlit.text_input("What fruit would you like information about?") #creating a variable to be passed into the fruityvice_response API request
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function = get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)

except URLError as e:
  streamlit.error()

#import snowflake.connector

streamlit.header("The Fruit Load List Contains:")
#snowflake related functions
def get_fruit_load_list():
  with my_cnx.cursor() as my_cur:
    my_cur.execute("select * from fruit_load_list")
    return my_cur.fetchall()

# add a button to load the fruit
if streamlit.button('Get Fruit Load List'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe(my_data_rows)

#don't run anything past here while we trubleshoot
streamlit.stop()

# Allow the end user to add a fruit to the list
add_my_fruit = streamlit.text_input("What fruit would you like to add?", "jackfruit") 
streamlit.write("Thanks for adding ", add_my_fruit) 

#this will not work correctly 
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
