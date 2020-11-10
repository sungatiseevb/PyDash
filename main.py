from random import randrange

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from analyser import count, names_of_product
from layout_n_1 import page_1_layout
from layout_n_2 import page_2_layout
from layout_n_3 import page_3_layout
from layout_n_4 import page_4_layout
from layout_n_5 import page_5_layout
from layout_n_6 import page_6_layout
import plotly.graph_objects as go

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

pages = {'/' : page_1_layout, '/page-2' : page_2_layout, '/page-3' : page_3_layout, '/page-4' : page_4_layout,
         '/page-5' : page_5_layout, '/page-6' : page_6_layout, '/page-7' : page_6_layout, '/page-8' : page_6_layout, '/page-9' : page_6_layout}

server = app.server
# Update the index
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    try:
        return pages[pathname]
    except KeyError:
        return 404

@app.callback(
    Output('products_d', 'figure'),
    Input('products_dd_id', 'value'))
def update_time_srez(val):
    try:
        return {'data': [
            {'y': count[names_of_product.index(val)]},
        ]}
    except ValueError:
        return {'data': [
            {'y': count[2]},
        ]}


@app.callback(
    Output("my-daq-gauge1", "value"),
    Output("my-daq-gauge2", "value"),
    Output("my-graph", "figure"),
    Input("timing", "n_intervals"),
)
def update_g(n_intervals):
    pressure_1 = randrange(10)  # mimics data pulled from live database
    pressure_2 = randrange(10)  # mimics data pulled from live database

    fig = go.Figure(
        [
            go.Bar(
                x=["valve 1", "valve 2"],
                y=[pressure_1, pressure_2],
            )
        ]
    )
    fig.update_layout(yaxis={"range": [0, 10]})

    return pressure_1, pressure_2, fig


if __name__ == '__main__':
    app.run_server(debug = True)

