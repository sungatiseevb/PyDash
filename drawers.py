import plotly.express as px

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