from dash import Dash, dcc, html, Input, Output
from scripts.load_data import load_cases_rates
from scripts.plots import lineplot

# Load dataframe beforehand so all users will use the same df, without loading it each time

df = load_cases_rates()


# Initializing Dash web app

app = Dash(__name__)

# exposde the flask server variable

server = app.server

# app layout are the components that will be displayed in the browser

app.layout = html.Div([

    html.H1("Rates by year"),

    dcc.Dropdown(
        id = 'group-dropdown',
        options = df['group'].unique(),
        value = "all groups"),

    dcc.Graph(id='trend-graph')
])

# Registering a callback so whenever a property of the input component changes, Dash calls the callback function 
# and update output component


@app.callback(
    Output('trend-graph', 'figure'), # what to update: component, property of the component
    Input('group-dropdown', 'value') # what to watch for: component, property of the component 
)

# This  is the callback function

def update_graph(selected_group):
    # Filter dataframe based on the selected group
    filtered_df = df[df['group'] == selected_group]

    # Call your plot function
    return lineplot(
        df = filtered_df,
        x_col = 'year',    
        y_col = 'rate',     
        color_col = 'group')

# Start the server
if __name__ == "__main__":
    app.run_server(debug = True)