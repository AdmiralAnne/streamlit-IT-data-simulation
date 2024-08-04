import streamlit as st
import pandas as pd
import numpy as np

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df

# the plan - Visualize the data - create inputs to change the visualizations
bar=st.bar_chart(data=df, x='Gender', y="Salary", x_label='Gender', y_label="Salary", color='Gender')
bar