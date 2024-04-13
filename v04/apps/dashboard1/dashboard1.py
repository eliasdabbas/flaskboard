import plotly.express as px
from dash import Dash, dcc, html
from dash_bootstrap_templates import load_figure_template

load_figure_template("all")


app = Dash(
    __name__,
    server=False,
    url_base_pathname="/test/dashboard1/",
)

app.layout = html.Div(
    [
        html.H1("This is Dashboard 1 ONE!"),
        html.Br(),
        dcc.Graph(
            figure=px.bar(
                x=[1, 2, 3, 4],
                y=[34, 23, 45, 34],
                title="Our First Interactive Chart!",
                template="cosmo",
            )
        ),
    ]
)

app.index_string = "{%app_entry%}{%config%}{%scripts%}{%renderer%}"
