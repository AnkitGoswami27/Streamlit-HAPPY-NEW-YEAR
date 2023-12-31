import requests
import streamlit as st
from streamlit_lottie import st_lottie

# Set page configuration
st.set_page_config(
    page_title="NEW YEAR",
    page_icon="✨",  # You can customize the page icon
      # Set layout to wide for full-width content
)
st.title("✨✨HAPPY NEW YEAR✨✨")

# Function to load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_coding = load_lottieurl("https://lottie.host/f284a35b-7d95-4cba-a11a-e265215f5576/7ruGdGORVe.json")

# Display the Lottie animation
st_lottie(lottie_coding, height=300, key="coding2")

# Display the title with updated styling
st.write("✨✨Wishing you 365 days of success, 52 weeks of laughter, and 12 months of love. Happy New Year to you and your family✨✨")
