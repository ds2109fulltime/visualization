def draw_sunburst(data_frame, path, color):
    '''This function performs a sunburst, when it is called, in 
    -"data_frame":the dataframe is entered,
    -"path": introduce with a list, the two columns or variables to be represented
    -"color": enter the column or main variable, which will be the value that the graph adopts'''
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
    