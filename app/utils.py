# app/utils.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data():
    # Placeholder: Replace with actual data fetching
    data = pd.DataFrame({
        'Country': ['Benin', 'Sierra Leone', 'Togo', 'Benin', 'Togo', 'Sierra Leone'],
        'GHI': [189.55, 189.55, 221.71, 150.0, 300.0, 180.2]
    })
    return data

def plot_avg_ghi(data):
    avg = data.groupby('Country')['GHI'].mean().sort_values(ascending=False)
    plt.figure(figsize=(8, 4))
    sns.barplot(x=avg.values, y=avg.index)
    plt.xlabel("Average GHI (W/m²)")
    plt.title("Average GHI by Country")
    return plt

def plot_ghi_distribution(data, country):
    subset = data[data['Country'] == country]
    plt.figure(figsize=(8, 4))
    sns.histplot(subset['GHI'], bins=20, kde=True)
    plt.title(f"GHI Distribution in {country}")
    plt.xlabel("GHI (W/m²)")
    return plt
