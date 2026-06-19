# Project Development Guidelines

## Code Organization

### Data Module (`src/data_cleaning.py`)
- Handles data loading and cleaning
- Missing value imputation
- Outlier detection and removal
- Type conversion

### Visualization Module (`src/visualization.py`)
- Statistical plots
- Distribution analysis
- Correlation matrices
- Comparative visualizations

### Analysis Module (`src/math_analysis.py`)
- Statistical tests
- Correlation analysis
- Outlier detection
- Feature statistics

### Model Module (`src/model.py`)
- ML model training
- Prediction generation
- Model evaluation
- Feature importance

## Best Practices

1. **Always use virtual environments**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Keep data in data/ directories**
   - Raw data: `data/raw/`
   - Processed data: `data/processed/`

3. **Use descriptive variable names**
   ```python
   # Good
   student_grades = df['G3']
   
   # Bad
   sg = df['G3']
   ```

4. **Add docstrings to functions**
   ```python
   def analyze_grades(df):
       """
       Analyze student grades and return statistics.
       
       Parameters:
       -----------
       df : pd.DataFrame
           Input dataframe
       
       Returns:
       --------
       dict
           Grade statistics
       """
   ```

5. **Use type hints** (Python 3.9+)
   ```python
   def load_data(filepath: str) -> pd.DataFrame:
       ...
   ```

## Git Workflow

1. Create feature branch
   ```bash
   git checkout -b feature/new-analysis
   ```

2. Make changes and commit
   ```bash
   git add .
   git commit -m "Add new analysis feature"
   ```

3. Push to remote
   ```bash
   git push origin feature/new-analysis
   ```

4. Create Pull Request

## Testing

Run tests before committing:
```bash
pytest tests/ -v
```

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Document assumptions and limitations
- Include usage examples

## Performance Optimization

- Use pandas vectorization instead of loops
- Cache expensive computations
- Use appropriate data types
- Monitor memory usage

## Error Handling

```python
try:
    data = pd.read_csv(filepath)
except FileNotFoundError:
    logger.error(f"File not found: {filepath}")
except pd.errors.ParserError:
    logger.error(f"Error parsing file: {filepath}")
```

## Logging

```python
import logging

logger = logging.getLogger(__name__)
logger.info("Processing started")
logger.warning("Potential issue detected")
logger.error("Error occurred")
```
