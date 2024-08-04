import streamlit as st
import pandas as pd
import numpy as np

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df

male_count = df[df['Gender'] == 'M'].shape[0]
female_count = df[df['Gender'] == 'F'].shape[0]

male_count
female_count

st.bar_chart(data=df, x="male_count", y="female_count", x_label="male_count", y_label="female_count", color='Gender', horizontal=False, stack=None, width=None, height=None, use_container_width=True)