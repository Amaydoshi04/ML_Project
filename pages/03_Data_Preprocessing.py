# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import streamlit as st

# Load the dataset from support.py
from support import df, df1, decription

# Set the page configuration
st.set_page_config(
    page_title="Data Preprocessing", page_icon=":zzz:", layout="centered"
)

# Set page title
st.title("Data Preprocessing")

# Display the first 5 rows of the dataset
st.markdown("### Dataset Preview")

with st.expander("Click here to view the dataset"):
    st.table(df)

# Basic information about the dataset
st.markdown("### Basic Information")

# Shape
st.markdown("#### Shape of the Dataset")
st.write(f"The dataset contains {df.shape[0]} rows and {df.shape[1]} columns.")

# Columns
st.markdown("#### Columns in the Dataset")
st.table(decription)

# Data types
st.markdown("#### Data Types")
st.table(df.dtypes)

# Descriptive Statistics
st.markdown("### Descriptive Statistics")
st.table(df.describe())

# Unique Values for each categorical column
st.markdown("#### Unique Values for Categorical Columns")
for col in df.select_dtypes(include=["object"]).columns:
    st.write(f"**{col}** : {df[col].unique()}")

# Data cleaning
st.markdown("### Data Cleaning")
st.markdown("#### Dropping Columns")
st.write("We will drop the 'Person ID' column as it is not required for our analysis.")
st.code("df1 = df.drop(['Person ID'], axis=1)")

# Splitting the 'Blood Pressure' column
st.markdown("#### Splitting and Dropping the 'Blood Pressure' Column")
st.write(
    "We will split the 'Blood Pressure' column into 'Systolic Pressure' and 'Diastolic Pressure' as the original attribute is unusable."
)
st.code(
    "df1['Systolic Pressure'] = df1['Blood Pressure'].apply(lambda x: int(x.split('/')[0]))"
)
st.code(
    "df1['Diastolic Pressure'] = df1['Blood Pressure'].apply(lambda x: int(x.split('/')[1]))"
)
st.code("df1 = df1.drop(['Blood Pressure'], axis=1)")

# Checking Null Values
st.markdown("#### Checking for Null Values")
st.table(df1.isnull().sum())
