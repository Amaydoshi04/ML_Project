# Description: This file contains the code to support the main file.
# It contains the code to clean the data and create visualizations.\

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Load the dataset
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")

# Create a copy of the dataset
df1 = df.copy()

# Drop the Person ID column
df1 = df1.drop(["Person ID"], axis=1)

# Split blood pressure into systolic and diastolic pressure
df1["Systolic Pressure"] = df1["Blood Pressure"].apply(lambda x: int(x.split("/")[0]))
df1["Diastolic Pressure"] = df1["Blood Pressure"].apply(lambda x: int(x.split("/")[1]))

# Drop the original blood pressure column
df1 = df1.drop(["Blood Pressure"], axis=1)

decription = pd.DataFrame(
    {
        "Gender": "The gender of the person (Male/Female).",
        "Age": "The age of the person in years.",
        "Occupation": "The occupation or profession of the person.",
        "Sleep Duration (hours)": "The number of hours the person sleeps per day.",
        "Quality of Sleep (scale: 1-10)": "A subjective rating of the quality of sleep, ranging from 1 to 10.",
        "Physical Activity Level (minutes/day)": "The number of minutes the person engages in physical activity daily.",
        "Stress Level (scale: 1-10)": "A subjective rating of the stress level experienced by the person, ranging from 1 to 10.",
        "BMI Category": "The BMI category of the person (e.g., Underweight, Normal, Overweight).",
        "Blood Pressure (systolic/diastolic)": "The blood pressure measurement of the person, indicated as systolic pressure over diastolic pressure.",
        "Heart Rate (bpm)": "The resting heart rate of the person in beats per minute.",
        "Daily Steps": "The number of steps the person takes per day.",
        "Sleep Disorder": "The presence or absence of a sleep disorder in the person (None, Insomnia, Sleep Apnea).",
    },
    index=["Description"],
)


