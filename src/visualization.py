"""
Module for data visualization
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Set style
sns.set_style("whitegrid")
rcParams['figure.figsize'] = (12, 6)
rcParams['font.size'] = 10


def set_plotting_style(style='seaborn-v0_8-darkgrid', palette='husl'):
    """
    Set global plotting style
    
    Parameters:
    -----------
    style : str
        Matplotlib style
    palette : str
        Seaborn palette
    """
    try:
        plt.style.use(style)
    except:
        plt.style.use('default')
    sns.set_palette(palette)


def plot_distribution(data, column, bins=30, title=None, figsize=(12, 6)):
    """
    Plot distribution of a column
    
    Parameters:
    -----------
    data : pd.DataFrame or pd.Series
        Input data
    column : str
        Column name (if data is DataFrame)
    bins : int
        Number of bins
    title : str
        Plot title
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if isinstance(data, pd.DataFrame):
        data = data[column]
    
    ax.hist(data, bins=bins, color='steelblue', edgecolor='black', alpha=0.7)
    ax.set_xlabel(column, fontsize=12, fontweight='bold')
    ax.set_ylabel('Frequency', fontsize=12, fontweight='bold')
    ax.set_title(title or f'Distribution of {column}', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_correlation_matrix(data, figsize=(12, 10), annot=True, cmap='coolwarm'):
    """
    Plot correlation matrix
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    figsize : tuple
        Figure size
    annot : bool
        Whether to show values
    cmap : str
        Colormap
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    # Select only numeric columns
    numeric_data = data.select_dtypes(include=[np.number])
    corr_matrix = numeric_data.corr()
    
    sns.heatmap(corr_matrix, annot=annot, cmap=cmap, center=0, 
                square=True, linewidths=0.5, cbar_kws={"shrink": 0.8},
                ax=ax, fmt='.2f')
    ax.set_title('Correlation Matrix', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    return fig


def plot_boxplot(data, column, by=None, figsize=(12, 6)):
    """
    Plot boxplot
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    column : str
        Column to plot
    by : str
        Group by column
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if by:
        data.boxplot(column=column, by=by, ax=ax)
        ax.set_title(f'{column} by {by}', fontsize=14, fontweight='bold')
    else:
        ax.boxplot(data[column])
        ax.set_title(f'{column} Boxplot', fontsize=14, fontweight='bold')
    
    ax.set_ylabel(column, fontsize=12, fontweight='bold')
    plt.suptitle('')  # Remove automatic title
    plt.tight_layout()
    return fig


def plot_comparison_by_category(data, numeric_col, category_col, figsize=(12, 6)):
    """
    Compare numeric values across categories
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    numeric_col : str
        Numeric column
    category_col : str
        Category column
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    categories = data[category_col].unique()
    positions = range(len(categories))
    
    for i, cat in enumerate(categories):
        values = data[data[category_col] == cat][numeric_col]
        ax.scatter([i] * len(values), values, alpha=0.6, s=100, label=cat)
    
    ax.set_xticks(positions)
    ax.set_xticklabels(categories)
    ax.set_ylabel(numeric_col, fontsize=12, fontweight='bold')
    ax.set_xlabel(category_col, fontsize=12, fontweight='bold')
    ax.set_title(f'{numeric_col} by {category_col}', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_scatter(data, x_col, y_col, hue=None, figsize=(12, 6)):
    """
    Plot scatter plot
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    x_col : str
        X-axis column
    y_col : str
        Y-axis column
    hue : str
        Color by column
    figsize : tuple
        Figure size
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    if hue:
        for group in data[hue].unique():
            subset = data[data[hue] == group]
            ax.scatter(subset[x_col], subset[y_col], label=group, alpha=0.6, s=100)
        ax.legend()
    else:
        ax.scatter(data[x_col], data[y_col], alpha=0.6, s=100, color='steelblue')
    
    ax.set_xlabel(x_col, fontsize=12, fontweight='bold')
    ax.set_ylabel(y_col, fontsize=12, fontweight='bold')
    ax.set_title(f'{y_col} vs {x_col}', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig


def plot_bar(data, column, figsize=(12, 6), top_n=None):
    """
    Plot bar chart for categorical column
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    column : str
        Column to plot
    figsize : tuple
        Figure size
    top_n : int
        Show only top N categories
        
    Returns:
    --------
    matplotlib figure
    """
    fig, ax = plt.subplots(figsize=figsize)
    
    value_counts = data[column].value_counts()
    if top_n:
        value_counts = value_counts.head(top_n)
    
    value_counts.plot(kind='bar', ax=ax, color='steelblue', edgecolor='black')
    ax.set_title(f'Distribution of {column}', fontsize=14, fontweight='bold')
    ax.set_xlabel(column, fontsize=12, fontweight='bold')
    ax.set_ylabel('Count', fontsize=12, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    return fig