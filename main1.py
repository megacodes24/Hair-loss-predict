# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data, predict

# Configure the app
st.set_page_config(
    page_title='Hair Loss Prediction',
    page_icon='brain',
    layout='wide',
    initial_sidebar_state='auto'
)

# Import pages
from Tabs import home, data, predict

# Dictionary for pages
Tabs = {
    "Home": home,
    "Data Info": data,
    "Prediction": predict,
    #"About me": about
}

# Create a sidebar
# Add title to sidebar
st.sidebar.title("Navigation")

# Create radio option to select the page
page = st.sidebar.radio("Pages", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Debugging: Print the flags.writeable property of y before passing it to predict
print("Before predict - y.flags.writeable:", y.flags.writeable)

# Call the app function of selected page to run
if page in ["Prediction"]:
    Tabs[page].app(df, X, y)
elif (page == "Data Info"):
    Tabs[page].app(df)
else:
    Tabs[page].app()

# Debugging: Print the flags.writeable property of y after passing it to predict
print("After predict - y.flags.writeable:", y.flags.writeable)

