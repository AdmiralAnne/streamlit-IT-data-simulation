import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df

male_count = df[df['Gender'] == 'M'].shape[0]
female_count = df[df['Gender'] == 'F'].shape[0]

male_count
female_count

# Count the number of males and females
gender_counts = df['Gender'].value_counts()

# Create a bar chart
plt.bar(gender_counts.index, gender_counts.values)
plt.xlabel("Gender")
plt.ylabel("Count")
plt.title("Number of Males and Females in the Dataset")
plt.show()