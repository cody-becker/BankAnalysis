"""
Simple tests for the bank churn analysis modules.
Tests core functionality of each module.
"""

import pandas as pd
import numpy as np
from data_preprocessing import load_data, handle_missing_values, prepare_data_for_modeling
from feature_engineering import create_derived_features
from model_training import split_data, train_random_forest, evaluate_model


def test_data_preprocessing():
    """Test data preprocessing functions."""
    print("Testing data preprocessing...")
    
    # Load data
    df = load_data('bank_customer_data.csv')
    assert df is not None, "Data should be loaded successfully"
    assert df.shape[0] > 0, "Data should have rows"
    
    # Handle missing values
    df_clean = handle_missing_values(df)
    assert df_clean.isnull().sum().sum() == 0, "No missing values should remain"
    
    print("✓ Data preprocessing tests passed")


def test_feature_engineering():
    """Test feature engineering functions."""
    print("Testing feature engineering...")
    
    # Load data
    df = load_data('bank_customer_data.csv')
    
    # Create derived features
    df_features = create_derived_features(df)
    assert df_features.shape[1] > df.shape[1], "Should create additional features"
    
    print("✓ Feature engineering tests passed")


def test_model_training():
    """Test model training and evaluation."""
    print("Testing model training...")
    
    # Load and prepare data
    df = load_data('bank_customer_data.csv')
    df = df.drop(columns=['CustomerId', 'Surname'], errors='ignore')
    
    # Encode categorical variables
    df_encoded = df.copy()
    for col in ['Geography', 'Gender']:
        if col in df_encoded.columns:
            df_encoded[col] = df_encoded[col].astype('category').cat.codes
    
    # Prepare for modeling
    X, y = prepare_data_for_modeling(df_encoded, target_column='Exited')
    
    # Split data
    X_train, X_test, y_train, y_test = split_data(X, y, test_size=0.2, random_state=42)
    assert X_train.shape[0] > 0, "Training set should have data"
    assert X_test.shape[0] > 0, "Test set should have data"
    
    # Train model
    model = train_random_forest(X_train, y_train, n_estimators=10, random_state=42)
    assert model is not None, "Model should be trained"
    
    # Evaluate model
    metrics = evaluate_model(model, X_test, y_test, model_name="Test RF")
    assert 'accuracy' in metrics, "Should return metrics"
    assert metrics['accuracy'] > 0.5, "Accuracy should be better than random"
    
    print("✓ Model training tests passed")


def test_churn_rate():
    """Test that churn rate is reasonable."""
    print("Testing churn rate...")
    
    df = load_data('bank_customer_data.csv')
    churn_rate = df['Exited'].mean()
    
    assert 0.1 < churn_rate < 0.5, f"Churn rate {churn_rate:.2%} should be between 10% and 50%"
    
    print(f"✓ Churn rate test passed (rate: {churn_rate:.2%})")


def run_all_tests():
    """Run all tests."""
    print("\n" + "="*60)
    print("RUNNING TESTS FOR BANK CHURN ANALYSIS")
    print("="*60 + "\n")
    
    test_data_preprocessing()
    test_feature_engineering()
    test_model_training()
    test_churn_rate()
    
    print("\n" + "="*60)
    print("ALL TESTS PASSED!")
    print("="*60 + "\n")


if __name__ == '__main__':
    run_all_tests()
