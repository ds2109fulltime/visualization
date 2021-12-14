import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import roc_curve, r2_score, mean_absolute_error, mean_squared_error, accuracy_score, f1_score, precision_score, recall_score,\
                            roc_auc_score, roc_curve

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


def print_regress_metrics(y, y_pred):
    ''' 
    This function print the plot the R^2, MAE, MSE, RMSE and MAPE score of a regression model

    Args:
        y (pandas.Series): The real target values.
        y_pred (pandas.Series): The target values predicted by the model.
    
    Returns:
        None

    '''

    print("R^2 score:", round(r2_score(y_pred, y), 4))
    print("MAE score:", round(mean_absolute_error(y_pred, y), 4))
    print("MSE score:", round(mean_squared_error(y_pred, y), 4))
    print("RMSE score:", round(np.sqrt(mean_squared_error(y_pred, y)), 4))
    y_array, y_pred_array = np.array(y), np.array(y_pred)
    mape = np.mean(np.abs((y_array - y_pred_array) / y_array)) * 100
    print(f'MAPE score: {round(mape, 4)} %')


def print_classif_metrics(y, y_pred):
    ''' 
    This function print the plot the accuracy, recall, precision, F1 score and AUC
        of a classification model

    Args:
        y (pandas.Series): The real target values.
        y_pred (pandas.Series): The target values predicted by the model.
    
    Returns:
        None

    '''

    print(f'Accuracy score: {round(accuracy_score(y_pred, y), 3)} %')
    print(f'Recall score: {round(recall_score(y_pred, y), 3)} %')
    print(f'Precision score: {round(precision_score(y_pred, y), 3)} %')
    print(f'F1 score: {round(f1_score(y_pred, y), 3)} %')
    print(f'AUC: {round(roc_auc_score(y_pred, y), 3)} %')