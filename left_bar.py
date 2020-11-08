import dash_core_components as dcc
import dash_html_components as html
from styles_file import styles

left_side = html.Div(
        children=[
            dcc.Link('Pie chart', href='/', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Простой график', href='/page-2', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Немножко DAQ', href='/page-3', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Пример дашборда', href='/page-4', style=styles['links_to_page'])
        ],
        style=styles['LEFT-BAR']
)