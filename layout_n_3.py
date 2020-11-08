import dash_daq as daq
import dash_html_components as html
import dash_table
from analyser import top_10_debtors
from left_bar import left_side
import dash_core_components as dcc

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
    left_side,

    # MAIN-BLOCK
    html.Div(
        children=[
            html.Div(
                id="dark-light-theme",
                children=[
                    html.Div(
                        [
                           # html.Div(
                           #      daq.Tank(
                           #          id="my-tank",
                           #          max=400,
                           #          value=197,
                           #          showCurrentValue=True,
                           #          units="gallons",
                           #          style={"margin-left": "50px", 'width' : '100px', 'height' : '100px'},
                           #      ),
                           #      className="three columns",
                           #  ),
                            html.Div(
                                daq.Gauge(
                                    id="my-daq-gauge1", min=0, max=10, value=6, label="Valve 1", style = styles['gauge1']
                                ),
                                className="four columns",
                            ),
                            html.Div(
                                daq.Gauge(
                                    id="my-daq-gauge2", min=0, max=10, value=9, label="Valve 2", style = styles['gauge2']
                                ),
                                className="four columns",
                            ),
                        ],
                        className="row",
                    ),
                    html.Div(
                        dcc.Graph(id="my-graph", figure={}, style = styles['random_graph']),
                        className="row",
                    ),
                    html.Div([
                        dash_table.DataTable(
                            id='table',
                            columns=[{"name": i, "id": i} for i in top_10_debtors.columns],
                            data=top_10_debtors.to_dict('records')
                        )
                    ], style = styles['table_top_10']),
                    dcc.Interval(id="timing", interval=1000, n_intervals=0)
                ])
        ],
        style=styles['MAIN-BLOCK']
    ),

    # FOOTER
    html.Div(
        children=[],
        style=styles['FOOTER']
    ),
], style=styles['MAIN_PAGE'])
