import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table

from left_bar import left_side
from styles_file import styles
from analyser import data

page_5_layout = html.Div(children=[

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
            dash_table.DataTable(
                    id='datatable-interactivity_2',
                    columns=[
                        {"name": i, "id": i, "deletable": False, "selectable": False} for i in data.columns
                    ],
                    style_cell={
                        'whiteSpace': 'normal',
                        'height': 'auto',
                        'minWidth': '100px',
                        'maxWidth': '150px',
                        'textAlign': 'left'
                    },
                    style_table={
                        'overflowX' : 'auto'
                    },

                    data=data.to_dict('records'),
                    editable=True,
                    filter_action="native",
                    sort_action="native",
                    sort_mode="multi",
                    column_selectable="single",
                    row_selectable="multi",
                    row_deletable=True,
                    selected_columns=[],
                    selected_rows=[],
                    page_action="native",
                    page_current= 0,
                    page_size= 10,
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
