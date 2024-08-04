import streamlit as st
import pandas as pd
import numpy as np

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')
with st.expander('Raw Data'):
    #import and view data
    df = pd.read_csv('employee.csv')
    df

# visualize the count of each variable in each column / faeture 
option = st.selectbox(
    "Which Feature's Count value do you wanna see?",
    ('Gender', 'Experience (Years)', 'Position'),
)

st.write('you have selected: ', option)

option_count = df[option].value_counts()
st.bar_chart(option_count)

with st.expander('chart data'):
    option_count

# new section for salary chart
st.subheader('Salary Variations for various Positions:')
# Create the line chart
st.line_chart(df, x='ID', y='Salary', color='Position')

position = st.selectbox(
    "Which JOB Position's stats do you wanna see?",
    ('Web Developer', 'IT Manager', 'IT Security Analyst','Database Administrator (DBA)', 'Systems Administrator', 'DevOps Engineer', 'Systems Analyst','Software Engineer','Network Administrator','IT Support Specialist', 'Cloud Solutions Architect'),
)

# create new dataframe for specific Job Positions
salary_df = df[df['Position'] == position]
salary_df
# insights on position
max_salary = salary_df['Salary'].max()
st.info("Maximum salary:",max_salary)

min_salary = salary_df['Salary'].min()
st.info("Minimum salary:",min_salary)