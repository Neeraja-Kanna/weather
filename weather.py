import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from PIL import Image
logo = Image.open('logo1.png')
#pip install pandas numpy matplotlib seaborn streamlit
#to run streamlit :   streamlit run weathertest.py 
st.set_page_config(page_title="weather  EDA", page_icon=":bar_chart:", layout="wide")
st.image(logo)
st.title("Exploratory Data Analysis on Weather Dataset")
# File upload
uploaded_file = st.file_uploader("Choose a Weather Dataset csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.dataframe(data)
# Define the list of names
names = ["K.NEERAJA", "K.AMRUTHA", "K.VAMSI","B.SAI RAM","T.MUKESH","A.HEMANTH","CH.KALYAN"]

# Add the names to the sidebar
st.sidebar.title("Project Team Members:")

for name in names:
    st.sidebar.write(name)

st.sidebar.title("Under The Guidance of :")
st.sidebar.write("Dr.Bomma.Ramakrishna")
st.title("Weather Data Analysis")
if st.checkbox("Show raw data"):
        st.write(data)
if st.checkbox("Show first 25 rows"):
        st.write(data.head(25))
st.write("BASIC INFORMATION ON DATASET")
if st.checkbox("Show shape"):
        st.write(data.shape)
if st.checkbox("Show index"):
        st.write(data.index)
if st.checkbox("Show columns"):
        st.write(data.columns)
if st.checkbox("Show data types"):
        st.write(data.dtypes)
if st.checkbox("Show unique values for 'Weather' column"):
        st.write(data['Weather'].unique())
if st.checkbox("Show count of non-null values"):
        st.write(data.count())
if st.checkbox("Show unique values count for each column"):
        st.write(data.nunique())
st.write("APPLYING SPECIAL OR REQURIED QUERIES BASED ON THE DATASET")
if st.checkbox("Show unique 'Wind Speed' values"):
        st.write(data['Wind Speed_km/h'].unique())
if st.checkbox("Show number of times 'Weather is exactly Clear'"):
        st.write(data[data.Weather == 'Clear'].shape[0])
if st.checkbox("Show number of times 'Wind Speed was exactly 4 km/h'"):
        st.write(data[data['Wind Speed_km/h'] == 4].shape[0])
if st.checkbox("Show all Null Values"):
        st.write(data.isnull().sum())
if st.checkbox("Rename 'Weather' column to 'Weather Condition'"):
        data.rename(columns = {'Weather' : 'Weather Condition'}, inplace=True)
        st.write(data.head())
if st.checkbox("Show mean 'Visibility'"):
        st.write(data.Visibility_km.mean())
if st.checkbox("Show Standard Deviation of 'Pressure'"):
        st.write(data.Press_kPa.std())
if st.checkbox("Show Variance of 'Relative Humidity'"):
        st.write(data['Rel Hum_%'].var())
if st.checkbox("Show all instances when 'Snow' was recorded"):
        st.write(data[data['Weather Condition'].str.contains('Snow')])
if st.checkbox("Show all instances when 'Wind Speed is above 24' and 'Visibility is 25'"):
        st.write(data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)])
if st.checkbox("Show Mean value of each column against each 'Weather Condition'"):
        st.write(data.groupby('Weather Condition').mean())
if st.checkbox("Show Minimum value of each column against each 'Weather Condition'"):
        st.write(data.groupby('Weather Condition').min())
if st.checkbox("Show Maximum value of each column against each 'Weather Condition'"):
        st.write(data.groupby('Weather Condition').max())
if st.checkbox("Show all records where 'Weather Condition' is Fog"):
        st.write(data[data['Weather Condition'] == 'Fog'])
if st.checkbox("Show all instances when 'Weather is Clear' or 'Visibility is above 40'"):
        st.write(data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)])
if st.checkbox("Show all instances when 'Weather is Clear' and 'Relative Humidity is greater than 50' or 'Visibility is above 40'"):
        st.write(data[(data['Weather Condition'] == 'Clear') & ((data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40))])
# Convert date column to datetime
data["Date/Time"] = pd.to_datetime(data["Date/Time"])
# Create new column for month
data["Month"] = data["Date/Time"].dt.month
# Calculate mean temperature by month
mean_temp_by_month = data.groupby("Month")["Temp_C"].mean()
if st.checkbox("Average temperatures of individual months throughout the year"):
    if st.checkbox("January"):
        st.write('the average temperature of january month:',mean_temp_by_month[1],")
    if st.checkbox("February"):
        st.write('the average temperature of February month:',mean_temp_by_month[2],")
    if st.checkbox("March"):
        st.write('the average temperature of March month:',mean_temp_by_month[3],")
    if st.checkbox("April"):
        st.write('the average temperature of April month:',mean_temp_by_month[4],") 
    if st.checkbox("May"):
        st.write('the average temperature of may month:',mean_temp_by_month[5],")
    if st.checkbox("June"):
        st.write('the average temperature of june month:',mean_temp_by_month[6],")
    if st.checkbox("July"):
        st.write('the average temperature of july month:',mean_temp_by_month[7],")   
    if st.checkbox("August"):
        st.write('the average temperature of August month:',mean_temp_by_month[8],")
    if st.checkbox("September"):
        st.write('the average temperature of September month:',mean_temp_by_month[9],")
    if st.checkbox("October"):
        st.write('the average temperature of October month:',mean_temp_by_month[10],")
    if st.checkbox("November"):
        st.write('the average temperature of November month:',mean_temp_by_month[11],")
    if st.checkbox("December"):
        st.write('the average temperature of December month:',mean_temp_by_month[12],")
st.write("DATA VISUALIATION ON THE DATASET")
# Create histogram of temperatures
if st.checkbox("Frequency distribtion of temperatures throughout the year"):
   fig, ax = plt.subplots()
   sns.histplot(data=data, x="Temp_C", ax=ax)
   ax.set_xlabel("Temperature (Celsius)")
   ax.set_ylabel("Count")
   st.pyplot(fig)
#Is there a relationship between temperature and visibility?
# Data visualization question

# Create scatterplot of temperature and visibility
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="Temp_C", y="Visibility_km", ax=ax)
ax.set_xlabel("Temperature (Celsius)")
ax.set_ylabel("Visibility (km)")
# Display scatterplot
if st.checkbox(" Relationship between Temperature and Visibility"):
   st.pyplot(fig)
#What is the average temperature by month?
# Create bar chart of mean temperature by month
fig, ax = plt.subplots()
mean_temp_by_month.plot(kind="bar", ax=ax)
ax.set_xlabel("Month")
ax.set_ylabel("Mean Temperature (Celsius)")
ax.set_xticklabels(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], rotation=0)
# Display bar chart
if st.checkbox("show average temperature by month"):
   st.pyplot(fig)
#What is the average pressure by weather condition?

