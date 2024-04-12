from dash import Dash, html, dcc, Input, Output

app = Dash(__name__, server=False, url_base_pathname='/test/dashboard2/')

app.layout = html.Div([
    html.H1('This is Dashboard 2 TWO!'),
    html.H2("Let's have some interactivity..."),
    html.Br(),
    dcc.Slider(id='slider', min=0, max=25, step=1, value=10, included=False), html.Br(),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), Input('slider', 'value'))
def show_number(number):
    return html.H3(f"You have chosen the number: {number}!")
