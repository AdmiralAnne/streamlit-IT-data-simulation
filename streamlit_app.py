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
    ("Gender", "Experience (Years)", "Position"),
)

st.write('you have selected: ', option)

option_count = df[option].value_counts()
st.bar_chart(option_count, color='count')

# new code:

# Count occurrences
option_count = df[option].value_counts()
option_count