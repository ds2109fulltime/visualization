import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve

def show_roc_curve(y, y_pred, style = 'seaborn', figsize=(10,5), extra_title = ''):
    ''' 
    This function plot the ROC curve for a classification model predicts
        
    Args:
        y (pandas.Series): The real target values.
        y_pred (pandas.Series): The target values predicted by the model.
        style (str): Here we define the graph style we want to use. 
            To see all the available styles, please type this: print(plt.style.available)
        figsize (tuple): Here we define the graph size, it has to be a tuple with 2 values
        extra_title (str): An extra text added to the title
    
    Returns:
        None

    '''

    fpr, tpr, thresholds = roc_curve(y, y_pred, )

    plt.style.use(style)
    plt.figure(figsize=figsize)

    ax = sns.lineplot(fpr, tpr)
    ax.set(xlim = [0.0, 1.0],
           ylim = [0.0, 1.0],
           title = 'ROC curve ' + extra_title,
           xlabel = 'False Positive Rate (1 - Specificity)',
           ylabel = 'True Positive Rate (Sensitivity)',
    )
    plt.show()
