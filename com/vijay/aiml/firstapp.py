import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
from pathlib import Path

# --- Path Logic (Which you nailed!) ---
current_file = Path(__file__).resolve()
project_root = current_file.parents[3]
csv_path = project_root / "resources" / "tip.csv"

# --- THE FIX ---
# DON'T USE: df = sns.load_dataset(csv_path)
# USE THIS INSTEAD:
try:
    df = pd.read_csv(csv_path)
    st.write("Successfully loaded your local CSV!")
except Exception as e:
    st.error(f"Error loading CSV: {e}")

# Now you can use Seaborn to plot that DataFrame
if 'df' in locals():
    st.subheader("My Local Bar Chart")
    fig, ax = plt.subplots()
    # Note: Make sure 'day' and 'total_bill' exist in your tip.csv!
    sns.barplot(data=df, x='day', y='total_bill', ax=ax)
    st.pyplot(fig)