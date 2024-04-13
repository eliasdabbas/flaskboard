import apps
import pandas as pd
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

apps.app_home.init_app(app)
apps.app1.init_app(app)
apps.app2.init_app(app)
apps.app_pop.init_app(app)

gapminder = pd.read_csv("apps/population/data/gapminder.csv")


@app.route("/")
def index():
    return render_template("main.html", app=apps.app_home)


@app.route("/dashboard1/")
def dashboard1():
    return render_template("main.html", app=apps.app1)


@app.route("/dashboard2/")
def dashboard2():
    print(app.url_map)
    return render_template("main.html", app=apps.app2)


@app.route("/population/<country>")
def population(country):
    if not country:
        abort(404)
    country_df = gapminder[gapminder["country"].eq(country)]

    year0 = country_df["year"].describe().astype(int)["min"]
    yearn = country_df["year"].describe().astype(int)["max"]

    max_pop = country_df["pop"].max()
    max_pop_year = country_df[country_df["pop"].eq(max_pop)]["year"].values[0]

    max_gdppercap = country_df["gdpPercap"].max()
    max_gdppercap_year = country_df[country_df["gdpPercap"].eq(max_gdppercap)][
        "year"
    ].values[0]

    summary = f"""
    The population of {country} is reported for the period <b>{year0} - {yearn}</b>. Its population peaked in <b>{max_pop_year}</b> at <b>{max_pop:,}</b>.
    <br>The GDP per capita last reported was <b>${max_gdppercap:,.0f}</b>, reported in <b>{max_gdppercap_year}</b>.
    """.strip()
    return render_template(
        "country.html", country=country, app=apps.app_pop, summary=summary
    )
