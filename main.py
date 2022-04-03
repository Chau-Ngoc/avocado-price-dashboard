import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, dcc, html

avocado_df = pd.read_csv("avocado.csv")

country_options = [
    {"label": i, "value": i}
    for i in avocado_df.geography.sort_values().unique()
]

app = Dash()
app.layout = html.Div(
    [
        html.H1("Avocado Price Dashboard"),
        dcc.Dropdown(
            id="country-dropdown",
            options=country_options,
            value=country_options[0]["value"],
        ),
        dcc.Graph(id="avocado-average-line-graph"),
    ]
)


@app.callback(
    Output(
        component_id="avocado-average-line-graph", component_property="figure"
    ),
    Input(component_id="country-dropdown", component_property="value"),
)
def update_avocado_price_graph(country):
    fig = px.line(
        data_frame=avocado_df[avocado_df["geography"] == country],
        x="date",
        y="average_price",
        color="type",
        title=f"Average Avocado Price over Years in {country}",
        labels={
            "date": "Date",
            "average_price": "Average Price",
            "type": "Type",
        },
    )
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
