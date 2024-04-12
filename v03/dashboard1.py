import plotly.express as px
from dash import Dash, Input, Output, dcc, html
from dash_bootstrap_templates import load_figure_template
load_figure_template('cosmo')
app = Dash(__name__, server=False, url_base_pathname="/test/dashboard1/")

app.layout = html.Div(
    [
        html.H1("This is Dashboard 1 ONE!"),
        html.Br(),
        dcc.Graph(
            id="graph",
            figure=px.bar(
                x=[1, 2, 3, 4], y=[34, 23, 45, 34], title="Our First Interactive Chart!", template='cosmo'
            ),
        ),
        dcc.Location(id="location"),
        html.Br(),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("graph", "figure"),
    Output("output", "children"),
    Input("graph", "figure"),
    Input("location", "href"),
)
def show_url(graph, url):
    print(graph)
    graph["layout"]["title"] = url.split("/")[-1] + " Chart"
    return graph, f"You are here: {url}"
