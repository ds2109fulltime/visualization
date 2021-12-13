import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, r2_score, mean_absolute_error, mean_squared_error, accuracy_score, f1_score, precision_score, recall_score,\
                            roc_auc_score, roc_curve

def get_roc_curve(y, y_pred, ax=None, **plt_kwargs):
# def get_roc_curve(y, y_pred, ax=None):
    if ax is None:
        ax = plt.gca()
    fpr, tpr, thresholds = roc_curve(y, y_pred)
    ax.plot(fpr, tpr, **plt_kwargs)
    # ax.plot(fpr, tpr)
    ax.set(xlim = [0.0, 1.0],
           ylim = [0.0, 1.0],
           title = 'ROC curve for titanic classifier',
           xlabel = 'False Positive Rate (1 - Specificity)',
           ylabel = 'True Positive Rate (Sensitivity)',
        #    grid = True
    )
    return(ax)


def print_regress_metrics(y, y_pred):
    print("R^2 score:", round(r2_score(y_pred, y), 4))
    print("MAE score:", round(mean_absolute_error(y_pred, y), 4))
    print("MSE score:", round(mean_squared_error(y_pred, y), 4))
    print("RMSE score:", round(np.sqrt(mean_squared_error(y_pred, y)), 4))
    y_array, y_pred_array = np.array(y), np.array(y_pred)
    mape = np.mean(np.abs((y_array - y_pred_array) / y_array)) * 100
    print(f'MAPE score: {round(mape, 4)} %')


def print_classif_metrics(y, y_pred):
    print(f'Accuracy score: {round(accuracy_score(y_pred, y), 3)} %')
    print(f'Recall score: {round(recall_score(y_pred, y), 3)} %')
    print(f'Precision score: {round(precision_score(y_pred, y), 3)} %')
    print(f'F1 score: {round(f1_score(y_pred, y), 3)} %')
    print(f'AUC: {round(roc_auc_score(y_pred, y), 3)} %')