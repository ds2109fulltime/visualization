
def draw_circle(data, column, title):
    '''Esta función realiza un pie chart con el círculo de dentro en blanco. Cuando se vaya a llamar, en el atributo "data" se introduce el dataframe, en el atributo column se introduce 
    la columna cuyos dos valores se desea representar, te dará como resultado el conteo'''
    import matplotlib.pyplot as plt
    total = data[column].value_counts()
    my_circle=plt.Circle( (0,0), 0.7, color='white') 
    plt.figure(figsize=(10,10))
    plt.pie(total.values,
            labels = total.index,
            autopct='%1.2f%%')
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.title(title)
    plt.show()
