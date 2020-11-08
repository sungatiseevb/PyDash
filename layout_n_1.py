import dash_html_components as html

from left_bar import left_side
from styles_file import styles
from drawers import draw_pie
from analyser import data
import dash_core_components as dcc

data_for_pie_1 = data['Портфель'].value_counts()
data_for_pie_2 = data['Продукт'].value_counts()

fig_pie_1 = draw_pie(data_for_pie_1)
fig_pie_2 = draw_pie(data_for_pie_2)

page_1_layout = html.Div(children=[

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
            html.H3(children='Портфель', style=styles['pie_1_title']),
            dcc.Graph(  # Круг
                id='pie_graph_1',
                figure=fig_pie_1,
                style=styles['Pie1']
            ),
            html.H3(children='Продукт', style=styles['pie_2_title']),
            dcc.Graph(  # Круг
                id='pie_graph_2',
                figure=fig_pie_2,
                style=styles['Pie2']
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