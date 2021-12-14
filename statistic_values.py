import matplotlib.pyplot as plt
import seaborn as sns

def draw_statistic_values(df, figsize=(10,8), palette="crest", s= 500, alpha=0.8,  title = None ,fontsize=18, loc_legend= "upper left"):
    ''' 
    This function shows in a scatterplot the 5 most common statistic measures of each numeric column of the dataframe:
        mean: the average
        min= the minimum value
        max= the maximum value
        50%= the median
        std= the standard deviation
        
    ------------------------
    Args:
    
    df= the dataframe
    figsize = here we define the graph size, it has to be a tuple with 2 values
    palette= here we define the graph's color palette. To change it, please see the seaborn library
    s= here we define the size of each symbol
    alpha= here we define the transparency of the symbols
    title= here we define th etitle of the graph. It's set to None by default
    fontsize= here we define the title size, if there is a title
    loc_legend= here we define the position of the legend
    
    ------------------------
    Result:
    
    a scatterplot with these 5 statistic measures for each column of the dataframe
        
    '''
    
    fig = plt.figure(figsize=figsize)
    ax = plt.axes()

    ax.set_title(title);
    
    df_stats = df.describe().T
    df_stats = df_stats[["mean","min","max", "50%", "std"]]

    sns.scatterplot(data=df_stats, palette=palette, s= s, alpha=alpha );

    plt.legend(loc=loc_legend);