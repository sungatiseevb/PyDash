import dash_core_components as dcc
import dash_html_components as html

from analyser import arr_by_row, count, names_of_product
from styles_file import styles
from left_bar import left_side

page_2_layout = html.Div(children=[

    # HEADER
    html.Div(
        children=[
            html.H3('Пример дашбордов')
        ],
        style=styles['Header']
    ),

    # LEFT-BAR
    left_side,


    # MAIN-BLOCK
    html.Div(
        children=[
            dcc.Dropdown(
                id='products_dd_id',
                options=[{'label': arr_by_row[i][0], 'value': arr_by_row[i][0]} for i in range(len(arr_by_row))],
                style=styles['DROPDOWN_PRODUCTS']
            ),

            dcc.Graph(
                id='products_d',
                style=styles['graph_product'],
                figure={'data': [
                    {'y': count[names_of_product.index('ИП')]},
                ]
                },
            ),
        ],
        style=styles['MAIN-BLOCK']
    ),

    # FOOTER
    html.Div(
        children=[],
        style=styles['FOOTER']
    ),
], style=styles['MAIN_PAGE'])