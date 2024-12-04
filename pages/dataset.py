import pandas as pd
import dash
from dash import html, dcc
import plotly.graph_objects as go

url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

dash.register_page(__name__, path='/dataset', name="Dataset 📋", order=1)


