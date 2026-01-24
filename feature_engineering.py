"""
Feature engineering module for bank customer churn analysis.
Creates derived features to improve model performance.
"""

import pandas as pd
import numpy as np

# Constants
DIVISION_EPSILON = 1  # Small value to avoid division by zero


def create_derived_features(df):
    """
    Create derived features from existing customer data.
    
    Args:
        df: Input DataFrame
        
    Returns:
        DataFrame with additional derived features
    """
    df_features = df.copy()
    
    # Balance per product ratio
    if 'Balance' in df_features.columns and 'NumOfProducts' in df_features.columns:
        df_features['BalancePerProduct'] = df_features['Balance'] / (df_features['NumOfProducts'] + DIVISION_EPSILON)
    
    # Credit score category
    if 'CreditScore' in df_features.columns:
        df_features['CreditScoreCategory'] = pd.cut(
            df_features['CreditScore'],
            bins=[0, 600, 650, 700, 850],
            labels=['Poor', 'Fair', 'Good', 'Excellent']
        )
    
    # Age group
    if 'Age' in df_features.columns:
        df_features['AgeGroup'] = pd.cut(
            df_features['Age'],
            bins=[0, 30, 40, 50, 100],
            labels=['Young', 'Middle', 'Senior', 'Elderly']
        )
    
    # Tenure category
    if 'Tenure' in df_features.columns:
        df_features['TenureCategory'] = pd.cut(
            df_features['Tenure'],
            bins=[0, 3, 6, 10],
            labels=['New', 'Intermediate', 'Long-term']
        )
    
    # Balance category
    if 'Balance' in df_features.columns:
        df_features['HasBalance'] = (df_features['Balance'] > 0).astype(int)
        df_features['BalanceCategory'] = pd.cut(
            df_features['Balance'],
            bins=[0, 1, 50000, 100000, 300000],
            labels=['Zero', 'Low', 'Medium', 'High']
        )
    
    # Salary to balance ratio
    if 'EstimatedSalary' in df_features.columns and 'Balance' in df_features.columns:
        df_features['SalaryToBalanceRatio'] = df_features['EstimatedSalary'] / (df_features['Balance'] + DIVISION_EPSILON)
    
    # Product engagement score
    if 'NumOfProducts' in df_features.columns and 'IsActiveMember' in df_features.columns:
        df_features['EngagementScore'] = df_features['NumOfProducts'] * df_features['IsActiveMember']
    
    print(f"Created {len(df_features.columns) - len(df.columns)} new features")
    
    return df_features


def select_important_features(df, feature_list=None):
    """
    Select important features for modeling.
    
    Args:
        df: Input DataFrame
        feature_list: Optional list of features to select
        
    Returns:
        DataFrame with selected features
    """
    if feature_list is None:
        # Default important features
        feature_list = [
            'CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts',
            'HasCrCard', 'IsActiveMember', 'EstimatedSalary', 'Geography',
            'Gender', 'BalancePerProduct', 'HasBalance', 'EngagementScore'
        ]
    
    # Select only features that exist in the dataframe
    available_features = [f for f in feature_list if f in df.columns]
    
    if len(available_features) < len(feature_list):
        missing = set(feature_list) - set(available_features)
        print(f"Warning: Features not found in dataframe: {missing}")
    
    return df[available_features]


def get_feature_statistics(df):
    """
    Get statistical summary of features.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Statistical summary
    """
    print("\n=== Numerical Features Statistics ===")
    print(df.describe())
    
    print("\n=== Categorical Features Distribution ===")
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    for col in categorical_cols:
        print(f"\n{col}:")
        print(df[col].value_counts())
    
    return df.describe()
