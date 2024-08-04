import streamlit as st
import pandas as pd
import numpy as np
from matplotlib.pyplot import plotly

st.title('📈 IT Data Simulation')

st.info('Salary for various IT Positions - configure using custom inputs that suit your needs.')

#import and view data
df = pd.read_csv('employee.csv')
df