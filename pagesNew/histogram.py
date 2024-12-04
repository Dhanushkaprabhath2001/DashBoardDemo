import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/distribution', name="Distribution 📊")


####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)


####################### HISTOGRAM ###############################
def create_distribution(col_name="world_cup_year"):
    return px.histogram(data_frame=df, x=col_name, height=600)

####################### WIDGETS ################################
columns = ["team_1_runs", "team_1_wickets","team_2_runs", "team_2_wickets", "world_cup_year", ]
dd = dcc.Dropdown(id="dist_column", options=columns, value="world_cup_year", clearable=False)

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Column:"),
    dd,
    dcc.Graph(id="histogram")
   
])

####################### CALLBACKS ################################
@callback(Output("histogram", "figure"), [Input("dist_column", "value"), ])
def update_histogram(dist_column):
    return create_distribution(dist_column)