import pandas as pd



def sort(df, col):
    '''This function sorts a DataFrame according to the selected column. 
    You only have to indicate the columns that you want to make up the dataframe.
    my_dict: dictionary
    df: Pandas DataFrame
    col = column
    '''
    df = df.sort_values(by=col,ascending=False)
    return df


