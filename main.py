import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.graph_objs as go
import pandas as pd
from datetime import datetime as dt
from dash.dependencies import Input, Output
from openpyxl import load_workbook
import plotly.express as px
import dash_table

reader = pd.read_excel("Витрина.xlsx")
data = pd.DataFrame(reader.values[2:, 1:])
data.columns = reader.values[0][1:]

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'LARGE'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Портфель']] = 'Корпы'

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'MIDDLEBIS'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Портфель']] = 'СБ'

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'SMALL') | (data['Бизнес - направление'] == 'MICRO'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Портфель']] = 'МБ'

data.loc[
        (data['Тип клиента'] == 'ИП')
        &
        (data['Индекс кредита'] == 3.0),
        ['Портфель']] = 'ИП'

data.loc[
        (data['Тип клиента'] == 'ИП')
        &
        (data['Индекс кредита'].isin([5.0, 6.0, 7.0, 8.0]))
        &
        (data['Источник финансирования'].isin([2, 3, 5])),
        ['Портфель']] = 'ФЛ ЕБРР'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        data['Индекс кредита'].isin([5.0, 6.0, 7.0, 8.0])
        &
        ~(data['Источник финансирования'].isin([2, 3, 9]))
        ,
        ['Портфель']] = 'Розница'

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'LARGE'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Продукт']] = 'Корпы'

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'MIDDLEBIS'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Продукт']] = 'СБ'

data.loc[
        (data['Тип клиента'] == 'ЮЛ')
        &
        ((data['Бизнес - направление'] == 'SMALL') | (data['Бизнес - направление'] == 'MICRO'))
        &
        (data['Индекс кредита'].isin([1.0, 2.0, 9.0])),
        ['Продукт']] = 'МБ'

data.loc[
        (data['Тип клиента'] == 'ИП')
        &
        (data['Индекс кредита'] == 3.0),
        ['Продукт']] = 'ИП'

data.loc[
        (data['Тип клиента'] == 'ИП')
        &
        (data['Индекс кредита'] >= 5.0)
        &
        (data['Индекс кредита'] <= 8.0)
        &
        data['Источник финансирования'].isin([2, 3, 5])
        ,
        ['Продукт']] = 'ФЛ ЕБРР'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        (data['Индекс кредита'] >= 6.0)
        &
        (data['Индекс кредита'] <= 8.0)
        &
        ~(data['Источник финансирования'].isin([2, 3, 5])),
        ['Продукт']] = 'Ипотека'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        (data['Индекс кредита'] == 5.0)
        &
        ~(data['Источник финансирования'].isin([2, 3, 5]))
        &
        (data['Шифр объекта кредитования'] == 152),
        ['Продукт']] = 'Авто'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        (data['Индекс кредита'] == 5.0)
        &
        ~(data['Источник финансирования'].isin([2, 3, 5]))
        &
        (data['Шифр объекта кредитования'] != 152)
        &
        data['Программа кредитования'].isin(['0.210.2.0271', '0.201.1.0105', '0.201.1.0301', '0.201.1.0302', '0.201.1.0303', '0.201.1.0304'])
        ,['Продукт']] = 'Беззалоговые'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        (data['Индекс кредита'] == 5.0)
        &
        ~(data['Источник финансирования'].isin([2, 3, 5]))
        &
        (data['Программа кредитования'].str.startswith('0.208.'))
        ,['Продукт']] = 'Кредитные карты'

data.loc[
        (data['Тип клиента'] == 'ФЛ')
        &
        (data['Индекс кредита'] == 5.0)
        &
        ~(data['Источник финансирования'].isin([2, 3, 5]))
        &
        (data['Шифр объекта кредитования'] != 152)
        &
        ~(data['Продукт'].isin(['Кредитные карты', 'Программа кредитования']))
        ,['Продукт']] = 'Потребительские'

arr_by_row = [
    ['Корпы'],
    ['СБ'],
    ['МБ'],
    ['ИП', 'ФЛ ЕБРР'],
    ['Ипотека'],
    ['Авто'],
    ['Беззалоговые'],
    ['Потребительские'],
    ['Кредитные карты']
]

date_interval = [
                 ['2020-01-01', '2020-02-01'],
                 ['2020-02-01', '2020-02-15'],
                 ['2020-02-15', '2020-02-22'],
                 ['2020-02-22', '2020-03-01'],
                ]

date_y = [i[0] for i in date_interval]
names_of_product = [i[0] for i in arr_by_row]

count = np.zeros((9, 4))

for i in range(len(arr_by_row)):
    for j in range(len(date_interval)):
        data1 = date_interval[j][0]
        data2 = date_interval[j][1]
        count[i][j] = len(data[
                        (data['Дата портфеля'] >= data1) & (data['Дата портфеля'] < data2)
                        &
                        data['Продукт'].isin(arr_by_row[i])
                     ])

top_10_debtors = data.sort_values(by=['Сумма основного долга'], ascending=False)[:10]
top_10_debtors = top_10_debtors.loc[:, ('Наименование клиента-дебитора', 'Сумма основного долга')]

data_for_pie_1 = data['Портфель'].value_counts()
data_for_pie_2 = data['Продукт'].value_counts()

def draw_pie(data_for_pie) :
    pie = px.pie(labels=list(data_for_pie.index), values=list(data_for_pie), names=list(data_for_pie.index))
    pie.update_traces(
        textposition='outside',
        textinfo='percent+label',
        #title = 'Портфель',
        marker=dict(line=dict(color='#000000',
                            width=4)),
        pull=[0.05, 0, 0.03],
        opacity=0.9,
        # rotation=180
    )
    return pie

fig_pie_1 = draw_pie(data_for_pie_1)
fig_pie_2 = draw_pie(data_for_pie_2)

#STYLES
styles = {}

styles['MAIN_PAGE'] = {
    'margin' : '0',
    'padding' : '0'
}

styles['Header'] = {
    'width' : '98%',
    'height' : '10vh',
    'text-align' : 'center',
    'margin-top' : '3vh',
    'font-size' : '20px',
    'font-family' : 'Geneva, Arial, Helvetica, sans-serif'
}

styles['LEFT-BAR'] = {
    'width' : '10%',
    'height' : '80vh',
    'position' : 'absolute',
}

styles['MAIN-BLOCK'] = {
    'width' : '78%',
    'height' : '80vh',
    'position' : 'absolute',
    'left' : '10%'
}

styles['FOOTER'] = {
    'width' : '98%',
    'height' : '10vh',
    'background-color' : 'black',
    'position' : 'absolute',
    'top' : '90vh',
}

styles['Pie1'] = {
    'width': '45%',
    'position' : 'absolute',
    'left' : '5%',
    'top' : '100px'
}

styles['pie_1_title'] = {
    'position' : 'absolute',
    'left' : '20%',
}

styles['Pie2'] = {
    'width': '45%',
    'position' : 'absolute',
    'left' : '55%',
    'top' : '100px'
}

styles['pie_2_title'] = {
    'position' : 'absolute',
    'left' : '70%',
}

styles['links_to_page'] = {
    'color' : 'white',
    'background-color' : 'black',
    'font-size' : '18px',
    'border' : '2px solid black',
    'text-decoration': 'none',
    'padding': '7px 10px',
    'display' : 'block'
}

styles['DROPDOWN_PRODUCTS'] = {
    'position' : 'absolute',
    'width' : '60%',
    'left' : '10%',
}

styles['graph_product'] = {
    'width' : '50%',
    'position' : 'absolute',
    'left' : '150px',
    'top' : '50px'
}

page_1_layout = html.Div(children=[

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

# 2 #
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

# 3 #
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

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


# Update the index
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return page_1_layout
    elif pathname == '/page-2':
        return page_2_layout
    elif pathname == '/page-3':
        return page_3_layout
    else:
        return 404
    # You could also return a 404 "URL not found" page here


@app.callback(
    Output('products_d', 'figure'),
    Input('products_dd_id', 'value'))
def update_time_srez(val):
    try:
        return {'data': [
            {'y': count[names_of_product.index(val)]},
        ]}
    except ValueError:
        return {'data': [
            {'y': count[2]},
        ]}

if __name__ == '__main__':
    app.run_server(debug = True)

