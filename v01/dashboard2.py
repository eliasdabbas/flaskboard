from dash import Dash, html

app = Dash(__name__, server=False, url_base_pathname='/dashboard2/')

app.layout = html.Div([
    html.H1('This is Dashboard 2 TWO!'),
])


