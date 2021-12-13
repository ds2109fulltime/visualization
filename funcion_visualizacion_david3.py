def tres_countplot(data, column_ax0, column_ax1, column_ax2, column_hue0, column_hue1, column_hue2, title0, title1,
                     title2, palette1, palette2, palette3):
    '''Esta función realiza tres gráficos countplot verticales con leyenda incluída, títulos
    y etiquetas con rotación en 45 grados y paleta de colores a escoger. Cuando se llame a la función, se ha de realizar lo siguiente: en data se introduce el dataframe, 
    en column_ax0, column_ax1, column_ax2 se introducen las columnas o variables que se desea representar y column_hue0, column_hue1, column_hue2 se introduce el valor que se desea
    representar dentro de las gráficas de coutplot, title0, title1, title2 son los títulos de cada subplot, palette1, palette2 y palette3 son las paletas de color para cada subplot.
    '''
    import matplotlib.pyplot as plt
    import seaborn as sns 
    fig, axes = plt.subplots(1, 3,  figsize=(20, 8))
    a = sns.countplot(data[column_ax0], hue=data[column_hue0], ax=axes[0], palette= palette1)
    axes[0].set_title(title0)
    a.set_xticklabels(a.get_xticklabels(), rotation=45)
    b = sns.countplot(data[column_ax1], hue=data[column_hue1], palette=palette2, ax=axes[1])
    axes[1].set_title(title1)
    b.set_xticklabels(b.get_xticklabels(), rotation=45)
    c = sns.countplot(data[column_ax2], hue=data[column_hue2], palette=palette3, ax=axes[2])
    axes[2].set_title(title2)
    c.set_xticklabels(c.get_xticklabels(), rotation=45)
    plt.show()