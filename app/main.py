# app/main.py

import streamlit as st
from .utils import load_data, plot_avg_ghi, plot_ghi_distribution

# Load data
data = load_data()

# Page Title
st.title("Solar GHI Insights Dashboard")

# Sidebar Filters
st.sidebar.header("Filters")
countries = data['Country'].unique()
selected_countries = st.sidebar.multiselect("Choose Countries:", options=countries, default=list(countries))
ghi_min, ghi_max = float(data['GHI'].min()), float(data['GHI'].max())
range_vals = st.sidebar.slider("GHI Range (W/m²)", min_value=ghi_min, max_value=ghi_max, value=(ghi_min, ghi_max))

# Data Filtering
filtered_data = data[
    (data['Country'].isin(selected_countries)) & 
    (data['GHI'] >= range_vals[0]) & 
    (data['GHI'] <= range_vals[1])
]

# 1. Average GHI Bar Plot
st.header("Average GHI by Country")
fig1 = plot_avg_ghi(filtered_data)
st.pyplot(fig1)

# 2. GHI Distribution per selected country
st.header("GHI Distribution")
for country in selected_countries:
    fig = plot_ghi_distribution(filtered_data, country)
    st.pyplot(fig)

# 3. Summary & Key Insights
st.header("Key Insights")
if not filtered_data.empty:
    summary = (
        filtered_data.groupby('Country')['GHI']
        .agg(['mean', 'median', 'std'])
        .reset_index()
    )
    for _, row in summary.iterrows():
        st.write(f"**{row['Country']}** - Mean: {row['mean']:.2f}, Median: {row['median']:.2f}, Std Dev: {row['std']:.2f}")
else:
    st.write("No data to display with current filters.")