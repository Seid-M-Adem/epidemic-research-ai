import pandas as pd

def load_data(filepath='/workspaces/epidemic-research-ai/data/raw/real_epidemic_data.csv'):
    """
    Load epidemic data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    data = pd.read_csv(filepath, parse_dates=['date'])
    return data

def preprocess_data(data):
    """
    Preprocess the epidemic data (sorting, handling datatypes).
    
    Args:
        data (pd.DataFrame): Raw data
    
    Returns:
        pd.DataFrame: Preprocessed data
    """
    data.sort_values(by=['country', 'date'], inplace=True)
    return data
