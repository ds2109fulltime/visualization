import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

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
