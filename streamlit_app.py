import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

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
# Function to generate a color palette
def generate_colors(n_colors):
    colors = plt.cm.get_cmap('tab20')(np.linspace(0, 1, n_colors))
    return [mcolors.to_hex(color) for color in colors]

st.write('you have selected: ', option)

# Count occurrences
option_count = df[option].value_counts()

# Generate colors based on the number of unique values
colors = generate_colors(len(option_count))

# Create the bar chart with custom colors
st.bar_chart(option_count, color=colors)