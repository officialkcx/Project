import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import altair as alt



st.header('Market of used cars')
st.write('Filter the data below to see the price and model by model year')


df = pd.read_csv('vehicles_us.csv')

# Checkbox to filter by SUV type
show_suv = st.checkbox('Show only SUV type cars')

# Streamlit slider to filter by model year
min_year = df['model_year'].min()
max_year = df['model_year'].max()
year_range = st.slider('Select the range of model year', min_year, max_year, (min_year, max_year))

# Filter the DataFrame based on the selected year range
filtered_df = df[(df['model_year'] >= year_range[0]) & (df['model_year'] <= year_range[1])]

# Display the filtered DataFrame
st.write("Filtered Table of Models and Prices:")
st.dataframe(filtered_df[['model', 'price']])


st.header('Data analysis')
st.write("""
###### Analyzing condition and odometer dat of the used cars""")
# List of columns to be used for selections
list_for_hist = ['model', 'transmission', 'type', 'paint_color']

# Streamlit selectbox for histogram
selected_type = st.selectbox('select statistic to filter by', list_for_hist)

# Create and display histogram
fig1 = px.histogram(df, x='type', y ='odometer', color=selected_type)
fig1.update_layout(title=f"<b> Split of odometer by age {selected_type}</b>")
st.plotly_chart(fig1)

# Define age category function
def age_category(x):
    if x < 5:
        return '<5'
    elif x >= 5 and x < 10:
        return '5-10'
    elif x >= 10 and x < 20:
        return '10-20'
    else:
        return '>20'

# Calculate age and age category
df['age'] = 2024 - df['model_year']
df['age_category'] = df['age'].apply(age_category)

# List of columns to be used for scatter plot
list_for_scatter = ['price', 'model_year', 'odometer', 'transmission', 'type', 'paint_color']

# Streamlit selectbox for scatter plot
choice_for_scatter = st.selectbox('Dependency on', list_for_scatter)

# Create and display scatter plot
fig2 = px.scatter(df, x="age", y='condition', color="model", hover_data=['model_year'])
fig2.update_layout(title=f"<b> condition to age relationship {choice_for_scatter}</b>")
st.plotly_chart(fig2)