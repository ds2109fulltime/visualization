def boxplot(data, column, color, title, etiqueta_nombre_columna):
    '''
    This function makes a box plot for a specific column.
    
    data: dataframe
    column: column to be represented.
    color: color to be used.
    title: graph name.
    label_column_name: column to be graphed.
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns 
    plt.figure(figsize=(8,8))
    sns.boxplot(x=data[column], color=color)
    plt.title(title)
    plt.xlabel(etiqueta_nombre_columna)
    plt.show()
