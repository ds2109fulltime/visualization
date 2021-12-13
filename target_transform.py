import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
import seaborn as sns


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
        target = here we define the column we want to see the transformations of 
        figsize = here we define the graph size, it has to be a tuple with 2 values
        color = here we define the bars color. Default value is blue ("b")
        
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
        sns.histplot(stats.boxcox(target)[0],kde=False,color= color,  ax=axes[2])
        axes[2].set_title("Box-Cox");

        # Power 2
        sns.histplot(np.power(target, 2),kde=False, color= color, ax=axes[3])
        axes[3].set_title("Power 2");