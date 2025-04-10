import streamlit as st
import pandas as pd
import numpy as np

# Title of the app
st.title("Simple Streamlit App")

# Displaying a header and text
st.header("Welcome!")
st.write("This is an example of a simple Streamlit application.")

# Text input widget
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to the app.")

# Slider widget
number = st.slider("Select a number", 1, 100, 50)
st.write("You selected:", number)

# Displaying a random data frame and a line chart
data = pd.DataFrame(
    np.random.randn(100, 2),
    columns=["Column 1", "Column 2"]
)
st.write("Random data:")
st.dataframe(data)
st.line_chart(data)

