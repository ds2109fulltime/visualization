import matplotlib.pyplot as plt
import seaborn as sns 

def draw_boxplot(df, column, color = "b", figsize=(8,8), title = None, label_column_name = None):
    '''
    This function makes a box plot for a specific column.
    
    df: dataframe
    column: column to be represented.
    color: color to be used.
    figsize = here we define the graph size, it has to be a tuple with 2 values
    title: graph name.
    label_column_name: column to be graphed.
    '''
    
    plt.figure(figsize=figsize)
    sns.boxplot(x=df[column], color=color)
    plt.title(title)
    plt.xlabel(label_column_name)
    plt.show()