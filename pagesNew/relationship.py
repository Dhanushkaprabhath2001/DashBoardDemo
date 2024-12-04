import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/histogrma', name="Histogram 📊")


####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)


####################### SCATTER CHART #############################
def create_scatter_chart(x_axis="Age", y_axis="Fare"):
    return px.scatter(data_frame=df, x=x_axis, y=y_axis, height=600)

####################### WIDGETS #############################
columns = ["team_1_runs","team_1_wickets", "team_2_runs", "team_2_wickets", "world_cup_year", "bowler_one_wicket", "bowler_two_wicket", "batter_one_score", "batter_two_score"]

x_axis = dcc.Dropdown(id="x_axis", options=columns, value="Age", clearable=False)
y_axis = dcc.Dropdown(id="y_axis", options=columns, value="Fare", clearable=False)


####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    "X-Axis", x_axis, 
    "Y-Axis", y_axis,
    dcc.Graph(id="scatter")
])

####################### CALLBACKS ###############################
@callback(Output("scatter", "figure"), [Input("x_axis", "value"),Input("y_axis", "value"), ])
def update_scatter_chart(x_axis, y_axis):
    return create_scatter_chart(x_axis, y_axis)