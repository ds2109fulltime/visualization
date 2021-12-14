import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def draw_feat_importance(importance,columns,model_type, figsize=(10,8)):
    '''   
    This function shows a graph with feature importance values of a trained model
    ------------------
    
    Args:
    importance = here we have to put the trained model with the feature importance function, we have to wrtie the model, followed by this sentence:  .feature_importances_
        (for example, if we have a trained random forest model, called "rf", the name will be this:  rf.feature_importances_ )
    columns = here we put the name of the columns we want to show the feature importances of
        (usually, all the dataframe columns, except the target one)
    model_type = here we put the name of model we used to train our dataframe
        (for example random forest, xgboost, etc...)
    figsize = here we define the graph size, it has to be a tuple with 2 values
    
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