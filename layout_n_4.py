import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
import dash_table

from left_bar import left_side
from styles_file import styles
from analyser import top_10_debtors

page_4_layout = html.Div(children=[

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
        id = 'MAINBLOCKID',
        children=[
            html.H1('Можно выводить таблицы'),
            html.H2('Топ 10 задолжников'),
            dash_table.DataTable(
                id='my_table',
                columns=[{"name": i, "id": i, "deletable": True, "selectable": True } for i in top_10_debtors.columns],
                data=top_10_debtors.to_dict('records'),
                editable=True,
                row_deletable=True,
                column_selectable="single",
                selected_columns=[],
                selected_rows=[],
                style_cell={
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'minWidth': '100px',
                    'maxWidth': '150px',
                    'textAlign': 'left'
                },
                style_header={
                    'backgroundColor': 'rgb(230, 230, 230)',
                    'fontWeight': 'bold'
                },
                row_selectable = 'multi',
                virtualization=True,
                style_table={'width': 600, 'overflowX' : 'auto'},
                style_as_list_view=True, # if you want see this as list

                # style_cell_conditional=[
                #         {
                #             'if': {'column_id': c},
                #             'textAlign': 'center'
                #         } for c in ['Сумма основного долга', 'Region']
                # ], #
                style_data_conditional=[
                    {
                        'if': {'row_index': 'odd'},
                        'backgroundColor': 'rgb(248, 248, 248)'
                    }
                ],
            ),

            # daq.BooleanSwitch(
            #     id='my-daq-booleanswitch',
            #     label=['Light', 'Dark'],
            #     on=False,
            #     style={'width': '50px', 'margin-left': '100px', 'margin-top' : '50px'}
            # )
        ],
        style=styles['MAIN-BLOCK']
    ),

    # FOOTER
    html.Div(
        children=[],
        style=styles['FOOTER']
    ),
], style=styles['MAIN_PAGE'])
