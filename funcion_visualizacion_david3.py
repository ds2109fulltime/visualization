def tres_countplot(data, column_ax0, column_ax1, column_ax2, column_hue0, column_hue1, column_hue2, title0, title1,
                     title2, palette1, palette2, palette3):
    '''This function performs three vertical countplot graphs with included legend, titles
    and labels with 45 degree rotation and color palette to choose from. When the function is called, the following must be done: 
    -data: the dataframe is entered,
    -column_ax0, column_ax1, column_ax2: you enter the columns or variables you want to represent
    -column_hue0, column_hue1, column_hue2: you enter the value you want to represent within the coutplot graphs, 
    -title0, title1, title2 are the titles of each subplot,
    -palette1, palette2 and palette3 are the color palettes for each subplot'''
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