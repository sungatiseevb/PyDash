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
            dcc.Link('Таблица 1', href='/page-4', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Таблица 2', href='/page-5', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Возможности 3', href='/page-6', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Возможности 4', href='/page-7', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Возможности 5', href='/page-8', style=styles['links_to_page']),
            html.Br(),
            dcc.Link('Возможности 6', href='/page-9', style=styles['links_to_page'])
        ],
        style=styles['LEFT-BAR']
)