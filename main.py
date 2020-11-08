import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from analyser import count, names_of_product
from layout_n_1 import page_1_layout
from layout_n_2 import page_2_layout
from layout_n_3 import page_3_layout

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

server = app.server
# Update the index
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    else:
        return 404
    # You could also return a 404 "URL not found" page here


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

if __name__ == '__main__':
    app.run_server(debug = False)

