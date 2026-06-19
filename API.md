# API Documentation

## Data Cleaning Module

### `load_data(filepath: str) -> pd.DataFrame`
Load CSV data from file.

**Parameters:**
- `filepath` (str): Path to CSV file

**Returns:**
- DataFrame with loaded data

**Example:**
```python
from src.data_cleaning import load_data
df = load_data('data/raw/student-grades.csv')
```

---

## Visualization Module

### `plot_distribution(data, column, bins=30, title=None, figsize=(12, 6))`
Plot distribution histogram.

**Parameters:**
- `data` (DataFrame/Series): Input data
- `column` (str): Column name
- `bins` (int): Number of bins (default: 30)
- `title` (str): Plot title
- `figsize` (tuple): Figure size

**Returns:**
- Matplotlib figure object

**Example:**
```python
from src.visualization import plot_distribution
fig = plot_distribution(df, 'G3', bins=25, title='Grade Distribution')
```

### `plot_correlation_matrix(data, figsize=(12, 10), annot=True, cmap='coolwarm')`
Plot correlation heatmap.

**Parameters:**
- `data` (DataFrame): Input dataframe
- `figsize` (tuple): Figure size
- `annot` (bool): Show values in heatmap
- `cmap` (str): Colormap name

**Returns:**
- Matplotlib figure object

---

## Statistical Analysis Module

### `correlation_analysis(data, target_col=None) -> pd.DataFrame`
Perform correlation analysis.

**Parameters:**
- `data` (DataFrame): Input dataframe
- `target_col` (str): Target column for analysis

**Returns:**
- DataFrame with correlation results

### `feature_statistics(data, numeric_cols=None) -> pd.DataFrame`
Get detailed statistics for numeric features.

**Parameters:**
- `data` (DataFrame): Input dataframe
- `numeric_cols` (list): List of numeric columns

**Returns:**
- DataFrame with statistics (Mean, Median, Std, Min, Max, Q1, Q3, IQR, Skewness, Kurtosis)

---

## ML Model Module

### `prepare_features(data, target_col='G3', drop_cols=None) -> tuple`
Prepare features and target for modeling.

**Parameters:**
- `data` (DataFrame): Input dataframe
- `target_col` (str): Target column name
- `drop_cols` (list): Columns to drop

**Returns:**
- Tuple of (X features, y target)

### `train_model(X_train, y_train, model_type='linear')`
Train ML model.

**Parameters:**
- `X_train` (DataFrame): Training features
- `y_train` (Series): Training target
- `model_type` (str): 'linear' or 'rf' (default: 'linear')

**Returns:**
- Trained model object

### `evaluate_model(model, X_test, y_test, y_pred=None) -> dict`
Evaluate model performance.

**Parameters:**
- `model`: Trained model
- `X_test` (DataFrame): Test features
- `y_test` (Series): Test target
- `y_pred` (array): Predictions (optional)

**Returns:**
- Dictionary with metrics: MSE, RMSE, MAE, R²

### `full_pipeline(data, target_col='G3', drop_cols=None, model_type='linear', test_size=0.2, random_state=42) -> dict`
Complete modeling pipeline.

**Parameters:**
- `data` (DataFrame): Input dataframe
- `target_col` (str): Target column
- `drop_cols` (list): Columns to drop
- `model_type` (str): Model type
- `test_size` (float): Test set proportion
- `random_state` (int): Random seed

**Returns:**
- Dictionary with pipeline results including model, data, metrics, and feature importance

**Example:**
```python
from src.model import full_pipeline

results = full_pipeline(
    df,
    target_col='G3',
    model_type='rf',
    test_size=0.2
)

print(f"Test R²: {results['test_metrics']['R2']:.4f}")
print(f"Test RMSE: {results['test_metrics']['RMSE']:.4f}")
```

---

## Streamlit Dashboard

**Run the dashboard:**
```bash
streamlit run app/streamlit_app.py
```

**Pages:**
1. **Overview** - Dataset summary and statistics
2. **Analysis** - Statistical analysis and comparisons
3. **Exploration** - Interactive feature exploration
4. **About** - Project information

---

## Error Handling

All functions include proper error handling:
- File not found errors
- Data type validation
- Missing value checks
- Shape validation

**Example:**
```python
try:
    df = load_data('nonexistent.csv')
except FileNotFoundError as e:
    print(f"Error: {e}")
```
