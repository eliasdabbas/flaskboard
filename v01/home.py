from dash import Dash, html

app = Dash(__name__, server=False, url_base_pathname='/')

app.layout = html.Div([
    html.H1('Hello, World! - Home Page'),
])