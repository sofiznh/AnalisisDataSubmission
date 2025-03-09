import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Initialize Streamlit App
st.title("Bike Sharing Data Analysis")

# Data Wrangling
## Gathering Data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Ambil path file saat ini
df_bike_day = pd.read_csv(os.path.join(BASE_DIR, 'day.csv'))
df_bike_hour = pd.read_csv(os.path.join(BASE_DIR, 'hour.csv'))

# Cleaning Data
## Menghapus duplikasi jika ada
df_bike_day = df_bike_day.drop_duplicates(subset=['dteday'])
df_bike_hour = df_bike_hour.drop_duplicates(subset=['dteday', 'hr'])
## Mengonversi kolom tanggal ke tipe datetime
df_bike_day['dteday'] = pd.to_datetime(df_bike_day['dteday'])
df_bike_hour['dteday'] = pd.to_datetime(df_bike_hour['dteday'])
## Mengonversi beberapa kolom menjadi kategori untuk efisiensi memori
categorical_columns = ['season', 'holiday', 'weekday', 'workingday', 'weathersit']
for col in categorical_columns:
    df_bike_day[col] = df_bike_day[col].astype('category')
    df_bike_hour[col] = df_bike_hour[col].astype('category')

# Adding Streamlit Filter
min_date = min(df_bike_day["dteday"].min(), df_bike_hour["dteday"].min())
max_date = max(df_bike_day["dteday"].max(), df_bike_hour["dteday"].max())
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("image.jpeg")

    # Mengambil start_date & end_date dari date_input
    start_date = None
    end_date = None
    filter_date = st.date_input(
        label='Date Range',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

    try :
        if(filter_date[0]) :
            start_date = pd.to_datetime(filter_date[0])
    except Exception:
        pass
    
    try :
        if(filter_date[1]) :
            end_date = pd.to_datetime(filter_date[1])
    except Exception:
        pass

if(start_date) :
    df_bike_day = df_bike_day[(df_bike_day["dteday"] >= start_date)]
    df_bike_hour = df_bike_hour[(df_bike_hour["dteday"] >= start_date)]
if(end_date) :
    df_bike_day = df_bike_day[(df_bike_day["dteday"] <= end_date)]
    df_bike_hour = df_bike_hour[(df_bike_hour["dteday"] <= end_date)]

st.write("") 
st.markdown(
    "<h3 style='color: white; background-color: #1f77b4; padding: 10px; border-radius: 5px;'>Cleaned Dataset Overview</h3>",
    unsafe_allow_html=True
)
st.write("### Day Dataset")
st.write(df_bike_day.head())
st.write("### Hour Dataset")
st.write(df_bike_hour.head())
st.write("") 
st.markdown(
    "<h3 style='color: white; background-color: #1f77b4; padding: 10px; border-radius: 5px;'>Visualization & Explanatory Analysis</h3>",
    unsafe_allow_html=True
)
# Visualization & Explanatory Analysis
## Tren jumlah penyewaan sepeda per bulan
st.subheader("Bike Sharing Trends per Month")
month_names = {
    1: "Jan", 2: "Feb", 3: "Mar", 4: "Apr", 5: "May", 6: "Jun",
    7: "Jul", 8: "Aug", 9: "Sep", 10: "Oct", 11: "Nov", 12: "Dec"
}
monthly_counts = df_bike_day.groupby('mnth')['cnt'].sum()
monthly_counts.index = monthly_counts.index.map(month_names)
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=monthly_counts.index, y=monthly_counts.values, marker='o', linewidth=2.5)
plt.xlabel("Month")
plt.ylabel("Total Rental Bikes")
plt.grid(True)
st.pyplot(fig)

## Pola penyewaan sepeda berdasarkan jam dalam sehari
st.subheader("Average Bike Sharing per Hour")
hourly_counts = df_bike_hour.groupby('hr')['cnt'].mean()
fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x=hourly_counts.index, y=hourly_counts.values, marker='o', linewidth=2.5)
plt.xticks(range(0, 24), labels=[f"{h:02d}:00" for h in range(0, 24)], rotation=45)
plt.xlabel("Hour")
plt.ylabel("Average Rental Bikes")
plt.grid(True)
st.pyplot(fig)

## Jumlah penyewaan per musim
st.subheader("Total Bike Sharisng per Season")
season_names = {
    1: "Springer", 2: "Summer", 3: "Fall", 4: "Winter"
}
season_counts = df_bike_day.groupby('season', observed=True)['cnt'].sum()
season_counts.index = season_counts.index.map(season_names)

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(x=season_counts.index, y=season_counts.values, color="#1f77b4")
plt.xlabel("Season")
plt.ylabel("Total Rental Bikes")
plt.ticklabel_format(style='plain', axis='y')
plt.grid(axis="y", linestyle="--", alpha=0.7)
st.pyplot(fig)