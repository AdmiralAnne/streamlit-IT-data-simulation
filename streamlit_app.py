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