import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sns


def draw_target_transformation(column, figsize=(15,5), color = "b"):
                
        ''' 
        This function shows the distribution of a dataframe specific column. 
        Usually, this column is the target (for example in a machine learning problem)
        but, actually, we could apply it to any column with NUMERICAL values.
        
        IMPORTANT: box cox transformation raise an error with 0 values or negative ones.
        
        
        This function is useful when, in a machine learning problem, we want to see if the distribution of the target column
        is a normal one, or if we have to apply some others transformation to obtain best results.
        
        ----------------
        
        Args:
        column = here we define the column we want to see the transformations of. Value must be inserted as Pandas Series
        figsize = here we define the graph size, it has to be a tuple with 2 values
        color = here we define the bars color. Default value is blue ("b")
        
        ----------------
        
        Results:
        4 graphs: in the first one we'll see the original distribution, in the second one we'll see the logaritmic distribution,
        in the third one we'll see the boxcox distribution and in the last graph we'll see the power distribution.
        
        '''
        
        fig,axes = plt.subplots(1, 4, figsize=figsize, sharey=True)

        # Original target
        sns.histplot(column, kde=False, color= color, ax=axes[0])
        axes[0].set_title("Original target")

        # Logaritmic
        sns.histplot(np.log(column),kde=False, color= color, ax=axes[1])
        axes[1].set_title("Log")

        # Box-cox
        #here we define a try/except to manage some critical values
        try:
                sns.histplot(stats.boxcox(column)[0],kde=False,color= color,  ax=axes[2])
                axes[2].set_title("Box-Cox");
        except:
                print("To visualize the boxcox graphs, values must be positive and different from zero.")

        # Power 2
        sns.histplot(np.power(column, 2),kde=False, color= color, ax=axes[3])
        axes[3].set_title("Power 2");