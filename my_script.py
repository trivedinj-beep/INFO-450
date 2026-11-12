
import pandas as pd
import streamlit as st 
st.set_page_config(page_title="netratrivedi-info450") 
import plotly.express as px 

df=pd.read_csv("Advertising_F.csv")
st.title("Advertising Effectiveness Trivedi")

st.sidebar.header("Filters")
x_var=st.selectbox("X axis",["TV","radio","newspaper"])

#show scatterplot
fig=px.scatter(df,x=x_var,y='sales',
           labels={'TV': 'Tv add spend', 'radio': 'Radio add spend'})

st.plotly_chart(fig)

#show the barplot 

sales_per_city=df.groupby('City')['sales'].sum().reset_index()
fig=px.bar(sales_per_city,x='City',y='sales',title="data is fun")
st.plotly_chart(fig)

#show the dataframe
st.dataframe(df)
