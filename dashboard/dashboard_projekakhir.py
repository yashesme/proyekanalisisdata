import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Load data
hour_df = pd.read_csv("hour.csv")
day_df = pd.read_csv("day.csv")

# Preprocess data
datetime_columns = ["dteday"]
for column in datetime_columns:
    hour_df[column] = pd.to_datetime(hour_df[column])
    day_df[column] = pd.to_datetime(day_df[column])

all_df = pd.merge(left=day_df, right=hour_df, how="left", left_on="instant", right_on="instant")

# Sidebar
st.sidebar.title('Bike Sharing')
image = Image.open("bike.png")
st.sidebar.image(image, caption='Bike Sharing', use_column_width=True)

# Title
st.title('Bike Sharing 🚲')

# Total Penyewaan Sepeda
total_cnt = all_df['cnt_y'].sum()
st.write(f"Total Penyewaan Sepeda: {total_cnt}")

# Total Penyewa Casual
total_casual = all_df['casual_y'].sum()
st.write(f"Total Penyewa Casual: {total_casual}")

# Total Penyewa Registered
total_registered = all_df['registered_y'].sum()
st.write(f"Total Penyewa Registered: {total_registered}")

# Grafik Penyewaan Bulanan
monthly_rentals = all_df.groupby('mnth_x')['cnt_y'].sum().reset_index()
st.subheader('Grafik Penyewaan Bulanan')
plt.figure(figsize=(10, 6))
sns.lineplot(data=monthly_rentals, x='mnth_x', y='cnt_y', marker='o')
plt.title('Total Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penyewaan')
plt.xticks(monthly_rentals['mnth_x'])
st.pyplot(plt)

# Grafik Penyewaan Musiman
seasonal_rentals = all_df.groupby('season_x')['cnt_y'].sum().reset_index()
st.subheader('Grafik Penyewaan Musiman')
plt.figure(figsize=(10, 6))
sns.lineplot(data=seasonal_rentals, x='season_x', y='cnt_y', marker='o')
plt.title('Total Penyewaan Sepeda per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Penyewaan')
plt.xticks(seasonal_rentals['season_x'], ['Spring', 'Summer', 'Fall', 'Winter'])
st.pyplot(plt)

# Grafik Penyewa Casual dan Registered per Bulan
monthly_rentals = all_df.groupby('mnth_x')[['casual_y', 'registered_y']].sum().reset_index()
st.subheader('Grafik Perbandingan Penyewaan Casual dan Registered')
plt.figure(figsize=(10, 6))
plt.plot(monthly_rentals['mnth_x'], monthly_rentals['casual_y'], marker='o', label='Casual Rentals')
plt.plot(monthly_rentals['mnth_x'], monthly_rentals['registered_y'], marker='o', label='Registered Rentals')
plt.title('Perbandingan Total Penyewaan Casual dan Registered per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Total Penyewaan')
plt.xticks(monthly_rentals['mnth_x'])
plt.legend()
plt.grid(True)
st.pyplot(plt)

# Grafik Penyewa Casual dan Registered per Musim
seasonal_rentals = all_df.groupby('season_x')[['casual_y', 'registered_y']].sum().reset_index()
plt.figure(figsize=(10, 6))
plt.plot(seasonal_rentals['season_x'], seasonal_rentals['casual_y'], marker='o', label='Casual Rentals')
plt.plot(seasonal_rentals['season_x'], seasonal_rentals['registered_y'], marker='o', label='Registered Rentals')
plt.title('Perbandingan Total Penyewaan Casual dan Registered per Musim')
plt.xlabel('Musim')
plt.ylabel('Total Penyewaan')
plt.xticks(seasonal_rentals['season_x'], ['Spring', 'Summer', 'Fall', 'Winter'])
plt.legend()
plt.grid(True)
st.pyplot(plt)