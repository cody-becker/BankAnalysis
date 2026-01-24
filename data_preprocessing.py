"""
Data preprocessing module for bank customer churn analysis.
Handles data loading, cleaning, and preparation.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder


def load_data(filepath):
    """
    Load customer data from CSV file.
    
    Args:
        filepath: Path to the CSV file
        
    Returns:
        DataFrame containing customer data
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found")
        return None
    except Exception as e:
        print(f"Error loading data: {e}")
        return None


def handle_missing_values(df):
    """
    Handle missing values in the dataset.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with missing values handled
    """
    df_clean = df.copy()
    
    # Check for missing values
    missing = df_clean.isnull().sum()
    if missing.sum() > 0:
        print("Missing values found:")
        print(missing[missing > 0])
        
        # Fill numerical columns with median
        num_cols = df_clean.select_dtypes(include=[np.number]).columns
        for col in num_cols:
            if df_clean[col].isnull().sum() > 0:
                df_clean[col] = df_clean[col].fillna(df_clean[col].median())
        
        # Fill categorical columns with mode
        cat_cols = df_clean.select_dtypes(include=['object']).columns
        for col in cat_cols:
            if df_clean[col].isnull().sum() > 0:
                df_clean[col] = df_clean[col].fillna(df_clean[col].mode()[0])
    
    return df_clean


def encode_categorical_features(df, categorical_columns):
    """
    Encode categorical features using Label Encoding.
    
    Args:
        df: Input DataFrame
        categorical_columns: List of categorical column names
        
    Returns:
        DataFrame with encoded categorical features
    """
    df_encoded = df.copy()
    label_encoders = {}
    
    for col in categorical_columns:
        if col in df_encoded.columns:
            le = LabelEncoder()
            df_encoded[col] = le.fit_transform(df_encoded[col].astype(str))
            label_encoders[col] = le
            print(f"Encoded column: {col}")
    
    return df_encoded, label_encoders


def scale_features(X_train, X_test):
    """
    Scale numerical features using StandardScaler.
    
    Args:
        X_train: Training features
        X_test: Test features
        
    Returns:
        Scaled training and test features, and the scaler object
    """
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, scaler


def prepare_data_for_modeling(df, target_column='Exited'):
    """
    Prepare data for machine learning modeling.
    
    Args:
        df: Input DataFrame
        target_column: Name of the target variable column
        
    Returns:
        Features (X) and target (y)
    """
    # Separate features and target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    print(f"Features shape: {X.shape}")
    print(f"Target distribution:\n{y.value_counts()}")
    
    return X, y
