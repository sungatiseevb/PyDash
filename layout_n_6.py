import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table

from left_bar import left_side
from styles_file import styles
from analyser import data

page_6_layout = html.Div(children=[

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
            html.Div(
                style = {
                    'background-image' : 'url("https://png.pngtree.com/thumb_back/fw800/background/20190223/ourmid/pngtree-beautiful-gradient-technology-background-design-backgroundhand-in-hand-image_73877.jpg")',
                    'width' : '70%',
                    'height' : '50vh',
                    'color' : 'white'
                },
                children=[
                    html.H1("Пока не готово")
                ]
            )
        ],
        style=styles['MAIN-BLOCK']
    ),

    # FOOTER
    html.Div(
        children=[],
        style=styles['FOOTER']
    ),
], style=styles['MAIN_PAGE'])
