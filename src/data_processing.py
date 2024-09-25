
import pandas as pd

def load_data(filepath):
    """
    Load epidemic data from a CSV file.
    
    Args:
        filepath (str): Path to the CSV file.
        
    Returns:
        pd.DataFrame: Loaded data.
    """
    data = pd.read_csv(filepath)
    return data
