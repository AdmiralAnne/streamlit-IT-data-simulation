import streamlit as st
import pandas as pd
import numpy as np
import pygwalker as pyg

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df

male_count = df[df['Gender'] == 'M'].shape[0]
female_count = df[df['Gender'] == 'F'].shape[0]

male_count
female_count

walker = pyg.walk(df)