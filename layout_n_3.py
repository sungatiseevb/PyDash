import dash_core_components as dcc
import dash_html_components as html

from styles_file import styles

page_3_layout = html.Div(children=[

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

        ],
        style=styles['MAIN-BLOCK']
    ),

    # FOOTER
    html.Div(
        children=[],
        style=styles['FOOTER']
    ),
], style=styles['MAIN_PAGE'])