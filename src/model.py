"""
Module for ML modeling
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error


def prepare_features(data, target_col='G3', drop_cols=None):
    """
    Prepare features and target for modeling
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    target_col : str
        Target column name
    drop_cols : list
        Columns to drop
        
    Returns:
    --------
    tuple
        X (features), y (target)
    """
    X = data.copy()
    y = X.pop(target_col)
    
    if drop_cols:
        X = X.drop(columns=drop_cols, errors='ignore')
    
    # Encode categorical variables
    categorical_cols = X.select_dtypes(include=['object', 'category']).columns
    le_dict = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        le_dict[col] = le
    
    return X, y


def train_model(X_train, y_train, model_type='linear'):
    """
    Train ML model
    
    Parameters:
    -----------
    X_train : pd.DataFrame
        Training features
    y_train : pd.Series
        Training target
    model_type : str
        Model type: 'linear' or 'rf'
        
    Returns:
    --------
    object
        Trained model
    """
    if model_type == 'linear':
        model = LinearRegression()
    elif model_type == 'rf':
        model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    
    model.fit(X_train, y_train)
    return model


def evaluate_model(model, X_test, y_test, y_pred=None):
    """
    Evaluate model performance
    
    Parameters:
    -----------
    model : object
        Trained model
    X_test : pd.DataFrame
        Test features
    y_test : pd.Series
        Test target
    y_pred : np.array
        Predictions (optional)
        
    Returns:
    --------
    dict
        Evaluation metrics
    """
    if y_pred is None:
        y_pred = model.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    rmse = np.sqrt(mse)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        'MSE': mse,
        'RMSE': rmse,
        'MAE': mae,
        'R2': r2
    }
    
    return metrics


def full_pipeline(data, target_col='G3', drop_cols=None, model_type='linear', 
                  test_size=0.2, random_state=42):
    """
    Complete modeling pipeline
    
    Parameters:
    -----------
    data : pd.DataFrame
        Input dataframe
    target_col : str
        Target column name
    drop_cols : list
        Columns to drop
    model_type : str
        Model type
    test_size : float
        Test set proportion
    random_state : int
        Random seed
        
    Returns:
    --------
    dict
        Pipeline results
    """
    print("🤖 Starting ML pipeline...\n")
    
    # Prepare features
    print("1️⃣  Preparing features...")
    X, y = prepare_features(data, target_col=target_col, drop_cols=drop_cols)
    print(f"   Features shape: {X.shape}")
    print(f"   Target shape: {y.shape}\n")
    
    # Train/test split
    print("2️⃣  Splitting data...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    print(f"   Train set: {X_train.shape}")
    print(f"   Test set: {X_test.shape}\n")
    
    # Train model
    print(f"3️⃣  Training {model_type} model...")
    model = train_model(X_train, y_train, model_type=model_type)
    print("   ✓ Model trained\n")
    
    # Evaluate
    print("4️⃣  Evaluating model...")
    y_pred_train = model.predict(X_train)
    y_pred_test = model.predict(X_test)
    
    train_metrics = evaluate_model(model, X_train, y_train, y_pred_train)
    test_metrics = evaluate_model(model, X_test, y_test, y_pred_test)
    
    print("   Train metrics:")
    for k, v in train_metrics.items():
        print(f"   - {k}: {v:.4f}")
    print("\n   Test metrics:")
    for k, v in test_metrics.items():
        print(f"   - {k}: {v:.4f}")
    print()
    
    # Get feature importance
    feature_importance = None
    if model_type == 'rf':
        print("5️⃣  Feature importance:")
        feature_importance = pd.DataFrame({
            'Feature': X.columns,
            'Importance': model.feature_importances_
        }).sort_values('Importance', ascending=False)
        print(feature_importance.head(10))
    
    print("\n✅ ML pipeline completed!")
    
    return {
        'model': model,
        'X_train': X_train,
        'X_test': X_test,
        'y_train': y_train,
        'y_test': y_test,
        'y_pred_train': y_pred_train,
        'y_pred_test': y_pred_test,
        'train_metrics': train_metrics,
        'test_metrics': test_metrics,
        'feature_importance': feature_importance
    }