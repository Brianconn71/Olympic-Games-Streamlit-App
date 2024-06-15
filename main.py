import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Pandas - creates dataframes to organize data interpreted by mapping and charting functions

# Plotly - creates interactive plots and charts

# Before we setup streamlit,
# we need to access the csv file and create a pandas dataframe

# load Dataset
file_path = 'Summer_olympic_Medals.csv'
data = pd.read_csv(file_path)

# Helper Function to get medal counts
def get_medal_counts(df, group_by_column):
    return df.g