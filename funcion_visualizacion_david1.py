def draw_sunburst(data_frame, path, color):
    '''Esta función realiza un sunburst, cuando se llame, en "data_frame" se introduce el dataframe, en "path", con una lista, se introducen las dos columnas o variables 
    que interesa representar, en "color" se introduce la columna o variable principal, que será el valor que adopta la gráfica'''
    import plotly.express as px
    fig = px.sunburst(
    data_frame = data_frame,
    path = path,
    color = color,
    color_discrete_sequence = ["red","green","blue","orange"],
    maxdepth = -1,
    )
    fig.update_traces(textinfo='label+percent entry')
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    fig.show()
    