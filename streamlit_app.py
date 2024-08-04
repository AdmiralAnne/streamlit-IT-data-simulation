import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df

# Count the number of males and females
gender_counts = df['Gender'].value_counts()
gender_counts

exp_counts = df['Experience (Years)'].value_counts()
exp_counts

st.bar_chart(exp_counts)
st.bar_chart(gender_counts)

option = st.selectbox(
    "Which Feature's Count value do you wanna see?",
    ("Gender'", "Experience (Years)", "Position"),
)

option_count = df[option].value_counts()
st.bar_chart(option_count)