"""
Module for statistical analysis
"""

import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import pearsonr, spearmanr


def correlation_analysis(data, target_col=None):
    """
    Perform correlation analysis
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    target_col : str
        Target column for correlation analysis
        
    Returns:
    --------
    pd.DataFrame
        Correlation results
    """
    numeric_data = data.select_dtypes(include=[np.number])
    
    if target_col and target_col in numeric_data.columns:
        correlations = numeric_data.corr()[target_col].sort_values(ascending=False)
        return pd.DataFrame({
            'Feature': correlations.index,
            'Correlation': correlations.values
        })
    else:
        return numeric_data.corr()


def statistical_summary(data):
    """
    Get detailed statistical summary
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
        
    Returns:
    --------
    pd.DataFrame
        Statistical summary
    """
    return data.describe()


def feature_statistics(data, numeric_cols=None):
    """
    Get detailed statistics for each numeric feature
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    numeric_cols : list
        List of numeric columns
        
    Returns:
    --------
    pd.DataFrame
        Detailed statistics
    """
    if numeric_cols is None:
        numeric_cols = data.select_dtypes(include=[np.number]).columns
    
    stats_dict = {
        'Mean': data[numeric_cols].mean(),
        'Median': data[numeric_cols].median(),
        'Std': data[numeric_cols].std(),
        'Min': data[numeric_cols].min(),
        'Max': data[numeric_cols].max(),
        'Q1': data[numeric_cols].quantile(0.25),
        'Q3': data[numeric_cols].quantile(0.75),
        'IQR': data[numeric_cols].quantile(0.75) - data[numeric_cols].quantile(0.25),
        'Skewness': data[numeric_cols].skew(),
        'Kurtosis': data[numeric_cols].kurtosis(),
    }
    
    return pd.DataFrame(stats_dict)


def print_statistical_report(data):
    """
    Print comprehensive statistical report
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    """
    print("=" * 80)
    print("STATISTICAL REPORT")
    print("=" * 80)
    print(f"\nDataset shape: {data.shape}")
    print(f"Number of features: {len(data.columns)}")
    print(f"Number of samples: {len(data)}")
    
    # Numeric features
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    print(f"\nNumeric features: {len(numeric_cols)}")
    print(numeric_cols.tolist())
    
    # Categorical features
    categorical_cols = data.select_dtypes(exclude=[np.number]).columns
    print(f"\nCategorical features: {len(categorical_cols)}")
    print(categorical_cols.tolist())
    
    # Missing values
    missing = data.isnull().sum()
    if missing.sum() > 0:
        print(f"\nMissing values:")
        print(missing[missing > 0])
    else:
        print("\nNo missing values")
    
    # Duplicates
    print(f"\nDuplicate rows: {data.duplicated().sum()}")
    
    # Descriptive statistics
    print("\n" + "=" * 80)
    print("DESCRIPTIVE STATISTICS")
    print("=" * 80)
    print(data.describe())