import dash_bootstrap_components as dbc
from urllib.parse import unquote
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html
from dash.exceptions import PreventUpdate
from dash_bootstrap_templates import load_figure_template

load_figure_template("all")

gapminder = pd.read_csv("apps/population/data/gapminder.csv")

app = Dash(
    __name__,
    server=False,
    url_base_pathname="/test/population/",
)

app.layout = html.Div(
    [
        html.Div(
            [
                dbc.DropdownMenu(
                    [
                        dbc.DropdownMenuItem(
                            country, href=f"/population/{country}", external_link=True
                        )
                        for country in gapminder["country"]
                        .drop_duplicates()
                        .sort_values()
                    ],
                    label="Change country",
                ),
            ],
            style={"float": "right"},
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Div(
            [
                dbc.Label("Add/compare other countries:"),
                dcc.Dropdown(
                    options=[
                        country
                        for country in gapminder["country"]
                        .drop_duplicates()
                        .sort_values()
                    ],
                    clearable=False,
                    multi=True,
                    id="dropdown",
                ),
            ],
        ),
        html.Br(),
        html.Div(id="output"),
        dcc.Location(id="location"),
    ],
)


@app.callback(Output("dropdown", "value"), Input("location", "pathname"))
def set_dropdown_from_url(country):
    if not country:
        raise PreventUpdate
    country = country.split("/")[-1]
    return unquote(country)


@app.callback(
    Output("output", "children"),
    Input("dropdown", "value"),
)
def make_pop_chart(countries):
    if not countries:
        raise PreventUpdate
    if isinstance(countries, str):
        countries = [countries]
    country_df = gapminder[gapminder["country"].isin(countries)]
    fig = px.line(
        country_df,
        x="year",
        y="pop",
        markers=True,
        color="country",
        template="slate",
        height=600,
        title=f"Population Growth<br>{', '.join(countries)}",
    )
    fig.layout.hovermode = "x unified"
    return html.Div([dcc.Graph(figure=fig)])


app.index_string = "{%app_entry%}{%config%}{%scripts%}{%renderer%}"
