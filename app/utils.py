# File: app/utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

def load_data(country: str) -> pd.DataFrame:
    """Load the CSV corresponding to the given country."""
    file_map = {
        "Benin": "data/benin-malanville.csv",
        "Sierra Leone": "data/sierraleone-bumbuna.csv",
        "Togo": "data/togo-dapaong_qc.csv"
    }
    df = pd.read_csv(file_map[country])
    df["country"] = country
    return df

def create_boxplot(df: pd.DataFrame, metric: str):
    """Create a boxplot for the specified metric."""
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.boxplot(x='country', y=metric, data=df, palette="Set2", ax=ax)
    ax.set_title(f"Boxplot of {metric} by Country")
    ax.set_xlabel("Country")
    ax.set_ylabel(metric)
    return fig

def create_top_regions_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Placeholder function for creating a top regions table.
    If your dataset contains a 'region' column and additional metrics,
    you could group by region and rank by one of the metrics (e.g., GHI).
    """
    if 'region' in df.columns:
        table = (df.groupby("region")["GHI"]
                   .mean()
                   .reset_index()
                   .sort_values(by="GHI", ascending=False))
        return table
    else:
        return pd.DataFrame()
