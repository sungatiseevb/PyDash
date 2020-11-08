import dash_core_components as dcc
import dash_html_components as html

from analyser import arr_by_row, count, names_of_product
from styles_file import styles

page_2_layout = html.Div(children=[

    # HEADER
    html.Div(
        children=[
            html.H3('Пример дашбордов')
        ],
        style=styles['Header']
    ),

    # LEFT-BAR
    html.Div(
        children=[
            dcc.Link('Страница первая', href='/', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Страница вторая', href='/page-2', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Страница третья', href='/page-3', style=styles['links_to_page'])
        ],
        style=styles['LEFT-BAR']
    ),

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