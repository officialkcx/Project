import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



st.header('Market of used cars.Original data')
st.write('Filter the data below to see the ads by manufacturer')


df = pd.read_csv('vehicles_us.csv')
df = df.drop(df.columns[0], axis=1)



manufacturer_choise = df['model'].unique()

selected_manu = st.selectbox('Select an manufactirar', manufacturer_choise )

min_year, max_year = int(df['model_year'].min()), int(df['model_year'].max())


year_range = st.slider("Choose years", value=(min_year, max_year), min_value=min_year,max_value= max_year)



actual_range = list(range(year_range[0], year_range[1]+1))


df_filtered = df[ (df.model == selected_manu) & (df.model_year.isin(list(actual_range)) )]

df_filtered


st.header('Price analysis')
st.write("""
###### Let's analyze what influences price the most. We will check how distibution of price varies depending on  transmission, engine or body type and state
""")

list_for_hist = ['price', 'model_year', 'odometer', 'transmission', 'type', 'paint_color']

selected_type = st.selectbox('Split for price distribution',list_for_hist)

fig1 = px.histogram(df, x="price",color = selected_type )
fig1.update_layout(title= "<b> Split of price by {}</b>".format(selected_type))
st.plotly_chart(fig1)


def age_category(x):
    if x<5: return '<5'
    elif  x>=5 and x<10: return '5-10'
    elif x>=10 and x<20: return '10-20'
    else: return '>20'

df['age'] = 2024 - df['model_year']

df['age_category'] = df['age'].apply(age_category)

list_for_scatter = list_for_hist = ['price', 'model_year', 'odometer', 'transmission', 'type', 'paint_color']


choice_for_scatter = st.selectbox('Price dependency on',list_for_scatter)

fig2 = px.scatter(df, x="price", y=choice_for_scatter, color ="model",hover_data=['model_year'])
fig2.update_layout(title="<b> Price vs {}</b>".format(choice_for_scatter))
st.plotly_chart(fig2)