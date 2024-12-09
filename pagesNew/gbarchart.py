import pandas as pd
import dash
from dash import dcc, html, callback
import plotly.express as px
from dash.dependencies import Input, Output

dash.register_page(__name__, path='/barchart', name="BARCHART ")

####################### LOAD DATASET #############################
url = "https://raw.githubusercontent.com/Dhanushkaprabhath2001/DashBoardDemo/refs/heads/main/data/cricket_data%20(2).csv"
df = pd.read_csv(url)

####################### WIDGETS ################################

# Extract unique years from the DataFrame
#years = df['world_cup_year'].unique()

# Create options for the year dropdown
#year_options = [{'label': str(year), 'value': year} for year in years]

# Create options for the function dropdown
function_options = [
    {'label': 'Mean', 'value': 'mean'},
    {'label': 'Sum', 'value': 'sum'},
    {'label': 'Count', 'value': 'count'}
]

# Create options for the variable dropdown
variable1_options = [
    {'label': 'team_1_runs', 'value': 'team_1_runs'},
    {'label': 'team_2_runs', 'value': 'team_2_runs'},
    # Add more variables as needed
]

variable2_options = [
    {'label': 'team_1_runs', 'value': 'team_1_runs'},
    {'label': 'team_2_runs', 'value': 'team_2_runs'},
    # Add more variables as needed
]


dd_function = dcc.Dropdown(id="filter_function", options=function_options, value='mean', multi=False, clearable=False)
dd_variable1 = dcc.Dropdown(id="filter_variable", options=variable_options, value=None, multi=False, clearable=False)
dd_variable2 = dcc.Dropdown(id="filter_variable", options=variable_options, value=None, multi=False, clearable=False)

####################### FUNCTIONS ################################

def create_distribution(variable, function, year=None):
    if year is not None:
        df_filtered = df[df["world_cup_year"] == year]
    else:
        df_filtered = df

    if function == 'mean':
        value = df_filtered[variable].mean()
    elif function == 'sum':
        value = df_filtered[variable].sum()
    else:
        value = df_filtered[variable].count()

    fig = px.bar(x=[variable], y=[value])
    fig.update_layout(title=f"{function} of {variable} for year {year}")
    return fig

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Br(),
    html.P("Select Function:"),
    dd_function,
    html.Br(),
    html.P("Select Variable:"),
    dd_variable,
    html.Br(),
    html.P("Select Variable:"),
    dd_year,
    html.Br(),
    dcc.Graph(id="barchart")
])

####################### CALLBACKS ################################

@callback(
    Output("barchart", "figure"),
    [Input("filter_function", "value"), Input("filter_variable", "value"), Input("filter_variable", "value")]
)
def update_histogram(function, variable, ):
    return create_distribution(variable, function, year)