# File: app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from utils import load_data, create_boxplot, create_top_regions_table

def main():
    st.title("Solar Potential Dashboard")
    st.markdown("Visualizing solar irradiance metrics across countries.")

    # Sidebar widget to select one or more countries
    countries = st.sidebar.multiselect(
        "Select Countries", 
        options=["Benin", "Sierra Leone", "Togo"],
        default=["Benin", "Sierra Leone", "Togo"]
    )

    # Button to load data after country selection
    if st.sidebar.button("Load Data"):
        # Load and combine data for the selected countries
        data_frames = [load_data(country) for country in countries]
        df_all = pd.concat(data_frames, ignore_index=True)
        st.write("Data Snapshot", df_all.head())

        # Select metric to plot
        metric = st.selectbox("Select an Irradiance Metric", ["GHI", "DNI", "DHI"])
        st.subheader(f"Boxplot: {metric} by Country")
        fig = create_boxplot(df_all, metric)
        st.pyplot(fig)

        # (Optional) Display top regions table if region information is available
        top_regions = create_top_regions_table(df_all)
        if not top_regions.empty:
            st.subheader("Top Regions by Average GHI")
            st.dataframe(top_regions)
        else:
            st.info("No 'region' column available in the dataset for regional ranking.")

if __name__ == "__main__":
    main()
