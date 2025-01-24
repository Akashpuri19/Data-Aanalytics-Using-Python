import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

#load the titanic datatset
titanic = sns.load_dataset("titanic")


st.title("Titanic Dataset Dashboard")
st.sidebar.header("filter options")


st.dataframe(titanic)