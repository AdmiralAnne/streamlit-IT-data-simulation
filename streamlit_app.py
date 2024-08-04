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
option_count
st.bar_chart(option_count, color='')

# new code:
# Function to generate a color palette based on first column values
def generate_colors(unique_values):
    import matplotlib.pyplot as plt
    import matplotlib.colors as mcolors

    # Use a colormap with enough colors for potential uniqueness
    colors = plt.cm.tab20(np.linspace(0, 1, len(unique_values) + 5))
    # Convert to hex codes and ensure uniqueness (optional)
    hex_colors = [mcolors.to_hex(color) for color in colors]
    # Optionally enforce uniqueness (consider performance for large datasets)
    unique_hex_colors = list(dict.fromkeys(hex_colors))
    return unique_hex_colors[:len(unique_values)]  # Take the first N colors

# Get unique values from the first column of option_count
unique_values = option_count.index.to_numpy()

# Generate colors based on unique values
colors = generate_colors(unique_values)

# Create the bar chart with custom colors
st.bar_chart(option_count, color=colors)