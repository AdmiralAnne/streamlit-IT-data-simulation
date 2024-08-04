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

# st.write('you have selected: ', option) # not needed at the moment

option_count = df[option].value_counts()
st.bar_chart(option_count)

with st.expander('chart data'):
    option_count

position = st.selectbox(
    "Which JOB Position's stats do you wanna see?",
    ('Web Developer', 'IT Manager', 'IT Security Analyst','Database Administrator (DBA)', 'Systems Administrator', 'DevOps Engineer', 'Systems Analyst','Software Engineer','Network Administrator','IT Support Specialist', 'Cloud Solutions Architect'),
)

# create new dataframe for specific Job Positions
salary_df = df[df['Position'] == position]

# insights on position
max_salary = salary_df['Salary'].max()
st.write("Maximum salary data")

max_salary_df = df[df['Salary'] == max_salary][['Experience (Years)', 'Position', 'Salary']]
max_salary_df

min_salary = salary_df['Salary'].min()
st.write("Minimum salary data")

min_salary_df = df[df['Salary'] == min_salary][['Experience (Years)', 'Position', 'Salary']]
min_salary_df


# st.line_chart(salary_df, x='ID', y='Salary', color='Position') # not east to understand 
st.line_chart(salary_df, x='Experience (Years)', y='Salary', color='Position') # easier to understand

with st.expander('Position data frame'):
    salary_df


# new section for salary chart - for all Positions
st.subheader('Salary Variations for various Positions:')
# Create the line chart
st.line_chart(df, x='ID', y='Salary', color='Position')