import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats


def draw_feat_importance(importance,columns,model_type, figsize=(10,8)):
    '''   
    This function shows a graph with feature importance values of a trained model.
    ------------------
    
    Args:
        importance: here we have to put the trained model with the feature importance function, we have to wrtie the model, followed by this sentence:  .feature_importances_
            (for example, if we have a trained random forest model, called "rf", the name will be this:  rf.feature_importances_ ).
    columns: here we put the name of the columns we want to show the feature importances of
            (usually, all the dataframe columns, except the target one).
    model_type: here we put the name of model we used to train our dataframe
            (for example random forest, xgboost, etc...)
    figsize: here we define the graph size, it has to be a tuple with 2 values.
    
    ------------------
    Result:
    the function shows a horizontal bar plot with all the feature importances, sorted by descending order
    
    '''
    
    #Create arrays from feature importance and feature names
    feature_importance = np.array(importance)
    feature_names = np.array(columns)

    #Create a DataFrame using a Dictionary, to store the feature names and their respective feature importances
    data={'feature_names':feature_names,'feature_importance':feature_importance}
    feat_imp_df = pd.DataFrame(data)

    #Sort the DataFrame in order decreasing feature importance
    feat_imp_df.sort_values(by=['feature_importance'], ascending=False,inplace=True)

   
    plt.figure(figsize=figsize)
    sns.barplot(x=feat_imp_df['feature_importance'], y=feat_imp_df['feature_names'])
    plt.title(model_type + ' FEATURE IMPORTANCE')
    plt.xlabel('FEATURE IMPORTANCE')
    plt.ylabel('FEATURE NAMES')


def missing_ratio(df, style = 'classic', figsize=(10,5), cmap='inferno', color = "lightgrey", lw=2,  title = None ,fontsize=18):
    ''' 
    This function shows a heatmap with missing values ratio of a dataframe.
    ----------------
    Args:
        df: here we define the dataframe we want to analize.
        style: here we define the graph style we want to use. 
                To see all the available styles, please type this:  print(plt.style.available).
        figsize: here we define the graph size, it has to be a tuple with 2 values.
        cmap: here we define the graph's color palette. To change it, please see the seaborn library.
        color: here we define the color of the separation bars.
        lw: here we define the thickness of the separation bars.
        title: here we define the graph's title, by default is set to None.
        fontsize: = here we define the title size, if there is a title.
    
    '''
    plt.style.use(style)

    plt.figure(figsize=figsize)

    ax = sns.heatmap(df.isna(),yticklabels=False,xticklabels=df.columns,cbar=False,cmap=cmap)

    ## para dibujar las líneas separadoras verticales
    for i in range(df.isna().shape[1]+1):
        ax.axvline(i,color = color, lw=lw);
        
    plt.title(title, fontsize=fontsize);
    plt.show()


def statistic_values(df, figsize=(10,8), palette="crest", s= 500, alpha=0.8,  title = None ,fontsize=18, loc_legend= "upper left"):
    """This function shows in a scatterplot the 5 most common statistic measures of each numeric column of the dataframe:
        mean: the average
        min= the minimum value
        max= the maximum value
        50%= the median
        std= the standard deviation
    
    ------------------------
    Args:
        df: the dataframe.
        figsize: here we define the graph size, it has to be a tuple with 2 values.
        palette: here we define the graph's color palette. To change it, please see the seaborn library.
        s: here we define the size of each symbol.
        alpha: here we define the transparency of the symbols.
        title: here we define th etitle of the graph. It's set to None by default.
        fontsize: here we define the title size, if there is a title.
        loc_legend: here we define the position of the legend.
    
    ------------------------
    Results:
        A scatterplot with these 5 statistic measures for each column of the dataframe.
        
    """ 
    
    fig = plt.figure(figsize=figsize)
    ax = plt.axes()

    ax.set_title(title);
    
    df_stats = df.describe().T
    df_stats = df_stats[["mean","min","max", "50%", "std"]]

    sns.scatterplot(data=df_stats, palette=palette, s= s, alpha=alpha );

    plt.legend(loc=loc_legend);


def target_transform(target, figsize=(15,5), color = "b"):
                
        ''' 
        This function shows the distribution of a dataframe specific column. 
        Usually, this column is the target (for example in a machine learning problem)
        but, actually, we could apply it to any column with NUMERICAL values.
        
        IMPORTANT: box cox transformation raise an error with 0 values or negative ones.
        
        
        This function is useful when, in a machine learning problem, we want to see if the distribution of the target column
        is a normal one, or if we have to apply some others transformation to obtain best results.
        
        ----------------
        
        Args:
            target: here we define the column we want to see the transformations of.
            figsize: here we define the graph size, it has to be a tuple with 2 values.
            color: here we define the bars color. Default value is blue ("b").
        
        ----------------
        
        Results:
            4 graphs: in the first one we'll see the original distribution, in the second one we'll see the logaritmic distribution,
            in the third one we'll see the boxcox distribution and in the last graph we'll see the power distribution.
        
        '''
        
        fig,axes = plt.subplots(1, 4, figsize=figsize, sharey=True)

        # Original target
        sns.histplot(target, kde=False, color= color, ax=axes[0])
        axes[0].set_title("Original target")

        # Logaritmic
        sns.histplot(np.log(target),kde=False, color= color, ax=axes[1])
        axes[1].set_title("Log")

        # Box-cox
        try:
            sns.histplot(stats.boxcox(target)[0],kde=False,color= color,  ax=axes[2])
            axes[2].set_title("Box-Cox");
        except:
            fig.delaxes(axes[2])
            print('Box-Cox is not plotted, data must be positive.')

        # Power 2
        sns.histplot(np.power(target, 2),kde=False, color= color, ax=axes[3])
        axes[3].set_title("Power 2");