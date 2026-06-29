# Counterparty-Exposure-Dashboard
# Pipeline:  laden -> aufbereiten -> servieren (Dash)
#
# Start:  pip install dash plotly pandas
#         python dashboard.py   ->  http://127.0.0.1:8050

import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, dash_table, Input, Output

FILE = r"/home/ucuber/Workspace/kurse/kurs-python/tag5/aufgaben/gegenparteien.txt"
GEWICHT = {"AAA": 0.2, "AA": 0.4, "A": 0.6, "BBB": 0.8, "BB": 1.0, "B": 1.5, "CCC": 2.0}

# --- Stufe 1: laden -----------------------------------------------------------
def laden(datei=FILE):
    return pd.read_csv(datei, sep="\t", names=["name", "rating", "exposure"])

# --- Stufe 2: aufbereiten -----------------------------------------------------
def aufbereiten(df):
    df = df.copy()
    df["gewicht"] = df["rating"].map(GEWICHT).fillna(1.0)
    df["gewichtet"] = df["exposure"] * df["gewicht"]
    df["anteil_%"] = (df["gewichtet"] / df["gewichtet"].sum() * 100).round(1)
    return df.sort_values("exposure", ascending=False)

DF = aufbereiten(laden())
PX_LAYOUT = dict(template="plotly_white", margin=dict(l=40, r=20, t=50, b=40))

# --- Stufe 3: servieren -------------------------------------------------------
app = Dash(__name__)
app.layout = html.Div(
    style={"fontFamily": "Inter, Arial, sans-serif", "background": "#ffffff",
           "color": "#2C2C2A", "maxWidth": "1100px", "margin": "0 auto", "padding": "24px"},
    children=[
        html.H2("Counterparty Exposure Report"),

        html.Label("Limit (EUR)"),
        dcc.Slider(id="limit", min=1_000_000, max=10_000_000, step=500_000,
                   value=5_000_000,
                   marks={i: f"{i//1_000_000}M" for i in range(1_000_000, 11_000_000, 1_000_000)}),

        html.Div(id="kpis", style={"display": "flex", "gap": "16px", "margin": "20px 0"}),

        dcc.Graph(id="bar_namen"),
        dcc.Graph(id="bar_rating"),

        html.H4("Limit-Verstoesse"),
        dash_table.DataTable(
            id="tabelle",
            columns=[{"name": c, "id": c} for c in ["name", "rating", "exposure", "gewichtet", "anteil_%"]],
            style_cell={"fontFamily": "Inter, Arial, sans-serif", "padding": "6px"},
            style_header={"backgroundColor": "#F1EFE8", "fontWeight": "600"},
            style_data={"backgroundColor": "#ffffff"},
        ),
    ],
)

def kpi_karte(titel, wert):
    return html.Div(
        style={"flex": "1", "padding": "14px 18px", "background": "#F4F3EE",
               "borderRadius": "10px", "border": "1px solid #D3D1C7"},
        children=[html.Div(titel, style={"fontSize": "13px", "color": "#5F5E5A"}),
                  html.Div(wert, style={"fontSize": "22px", "fontWeight": "600"})],
    )

@app.callback(
    Output("kpis", "children"), Output("bar_namen", "figure"),
    Output("bar_rating", "figure"), Output("tabelle", "data"),
    Input("limit", "value"),
)
def aktualisieren(limit):
    df = DF.copy()
    df["status"] = df["exposure"].apply(lambda x: "ueber Limit" if x > limit else "ok")

    kpis = [
        kpi_karte("Gegenparteien", f"{len(df)}"),
        kpi_karte("Exposure gesamt", f"{df['exposure'].sum():,.0f} EUR"),
        kpi_karte("Risikogewichtet", f"{df['gewichtet'].sum():,.0f} EUR"),
        kpi_karte("ueber Limit", f"{(df['exposure'] > limit).sum()}"),
    ]

    fig_namen = px.bar(df, x="name", y="exposure", color="status",
                       color_discrete_map={"ueber Limit": "#A32D2D", "ok": "#0F6E56"},
                       title="Exposure je Gegenpartei")
    fig_namen.add_hline(y=limit, line_dash="dash", line_color="#5F5E5A")
    fig_namen.update_layout(**PX_LAYOUT)

    per_rating = df.groupby("rating", as_index=False)["gewichtet"].sum()
    fig_rating = px.bar(per_rating, x="rating", y="gewichtet",
                        title="Risikogewichtetes Exposure je Rating")
    fig_rating.update_traces(marker_color="#185FA5")
    fig_rating.update_layout(**PX_LAYOUT)

    tab = df[df["exposure"] > limit][["name", "rating", "exposure", "gewichtet", "anteil_%"]]
    return kpis, fig_namen, fig_rating, tab.to_dict("records")


if __name__ == "__main__":
    app.run(debug=True)
