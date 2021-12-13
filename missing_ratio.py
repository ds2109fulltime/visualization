import matplotlib.pyplot as plt
import seaborn as sns

def missing_ratio(df, style = 'classic', figsize=(10,5), cmap='inferno', color = "lightgrey", lw=2,  title = None ,fontsize=18):
    ''' 
    This function shows a heatmap with missing values ratio of a dataframe
    ----------------
    Args:
    df = here we define the dataframe we want to analize
    style = here we define the graph style we want to use. 
            To see all the available styles, please type this:  print(plt.style.available)
    figsize = here we define the graph size, it has to be a tuple with 2 values
    cmap = here we define the graph's color palette. To change it, please see the seaborn library
    color = here we define the color of the separation bars
    lw = here we define the thickness of the separation bars
    title = here we define the graph's title, by default is set to None
    fontsize = here we define the title size, if there is a title
    
    '''
    plt.style.use(style)

    plt.figure(figsize=figsize)

    ax = sns.heatmap(df.isna(),yticklabels=False,xticklabels=df.columns,cbar=False,cmap=cmap)

    ## para dibujar las líneas separadoras verticales
    for i in range(df.isna().shape[1]+1):
        ax.axvline(i,color = color, lw=lw);
        
    plt.title(title, fontsize=fontsize);
    plt.show()