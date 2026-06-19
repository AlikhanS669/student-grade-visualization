"""
Module for data cleaning and preprocessing
"""

import pandas as pd
import numpy as np
from scipy import stats


def load_data(filepath):
    """
    Load data from CSV file
    
    Parameters:
    -----------
    filepath : str
        Path to CSV file
        
    Returns:
    --------
    pd.DataFrame
        Loaded dataframe
    """
    df = pd.read_csv(filepath)
    print(f"✓ Data loaded: {df.shape}")
    return df


def check_duplicates(df):
    """
    Check and report duplicates
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    int
        Number of duplicates
    """
    duplicates = df.duplicated().sum()
    print(f"📌 Duplicates found: {duplicates}")
    return duplicates


def remove_duplicates(df):
    """
    Remove duplicate rows
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe without duplicates
    """
    initial_size = len(df)
    df = df.drop_duplicates()
    removed = initial_size - len(df)
    print(f"✓ Removed {removed} duplicate rows")
    return df


def check_missing_values(df):
    """
    Check missing values in the dataset
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Missing values report
    """
    missing = pd.DataFrame({
        'Column': df.columns,
        'Missing_Count': df.isnull().sum(),
        'Missing_Percent': (df.isnull().sum() / len(df) * 100).round(2)
    })
    missing = missing[missing['Missing_Count'] > 0].sort_values('Missing_Percent', ascending=False)
    print("\n📌 Missing values:")
    print(missing)
    return missing


def handle_missing_values(df, strategy='mean'):
    """
    Handle missing values
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    strategy : str
        Strategy for handling: 'mean', 'median', 'drop'
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with handled missing values
    """
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    if strategy == 'mean':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
    elif strategy == 'median':
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
    elif strategy == 'drop':
        df = df.dropna()
    
    print(f"✓ Missing values handled using '{strategy}' strategy")
    return df


def convert_data_types(df):
    """
    Convert data types to appropriate formats
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Dataframe with converted types
    """
    # Convert categorical columns
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        if df[col].dtype == 'object':
            df[col] = df[col].astype('category')
    
    print(f"✓ Data types converted")
    return df


def detect_outliers(df, column, method='iqr', threshold=1.5):
    """
    Detect outliers in a column
    
    Parameters:
    -----------
    df : pd.DataFrame
        Input dataframe
    column : str
        Column name
    method : str
        Method: 'iqr' or 'zscore'
    threshold : float
        Threshold for outliers
        
    Returns:
    --------
    pd.Series
        Boolean series indicating outliers
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        outliers = (df[column] < Q1 - threshold * IQR) | (df[column] > Q3 + threshold * IQR)
    elif method == 'zscore':
        z_scores = np.abs(stats.zscore(df[column].dropna()))
        outliers = (z_scores > threshold)
    
    return outliers


def clean_data(filepath, remove_dupes=True, handle_missing=True, 
               remove_outl=False, strategy='mean'):
    """
    Complete data cleaning pipeline
    
    Parameters:
    -----------
    filepath : str
        Path to CSV file
    remove_dupes : bool
        Whether to remove duplicates
    handle_missing : bool
        Whether to handle missing values
    remove_outl : bool
        Whether to remove outliers
    strategy : str
        Strategy for missing values: 'mean', 'median', 'drop'
        
    Returns:
    --------
    pd.DataFrame
        Clean dataframe
    """
    print("🧹 Starting data cleaning pipeline...\n")
    
    # Load data
    df = load_data(filepath)
    print(f"📊 Initial shape: {df.shape}\n")
    
    # Remove duplicates
    if remove_dupes:
        check_duplicates(df)
        df = remove_duplicates(df)
        print()
    
    # Handle missing values
    if handle_missing:
        check_missing_values(df)
        df = handle_missing_values(df, strategy=strategy)
        print()
    
    # Convert types
    df = convert_data_types(df)
    print()
    
    print(f"✅ Final shape: {df.shape}")
    print("✅ Data cleaning completed!")
    
    return df