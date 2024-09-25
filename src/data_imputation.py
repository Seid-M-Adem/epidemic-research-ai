
def impute_missing_data(data, strategy='mean', columns=None):
    """
    Impute missing values in the specified columns using the given strategy.
    
    Args:
        data (pd.DataFrame): Data with missing values.
        strategy (str): Imputation strategy ('mean', 'median', or 'mode').
        columns (list): List of columns to impute.
        
    Returns:
        pd.DataFrame: Data with imputed values.
    """
    for col in columns:
        if strategy == 'mean':
            data[col].fillna(data[col].mean(), inplace=True)
        elif strategy == 'median':
            data[col].fillna(data[col].median(), inplace=True)
        elif strategy == 'mode':
            data[col].fillna(data[col].mode()[0], inplace=True)
    
    return data
