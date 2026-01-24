"""
Main script for Bank Customer Churn Analysis.
This script orchestrates the complete analysis pipeline:
1. Data loading and preprocessing
2. Exploratory data analysis
3. Feature engineering
4. Model training and evaluation
5. Predictions and insights
"""

import os
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Import custom modules
from data_preprocessing import (
    load_data, handle_missing_values, encode_categorical_features,
    scale_features, prepare_data_for_modeling
)
from feature_engineering import (
    create_derived_features, select_important_features, get_feature_statistics
)
from eda import (
    plot_target_distribution, plot_numerical_features, plot_categorical_features,
    plot_correlation_matrix, analyze_churn_by_feature, generate_eda_summary
)
from model_training import (
    split_data, train_logistic_regression, train_random_forest,
    train_gradient_boosting, evaluate_model, get_feature_importance,
    plot_confusion_matrix, plot_roc_curve
)


def main():
    """
    Main function to run the complete bank churn analysis pipeline.
    """
    print("="*70)
    print("BANK CUSTOMER CHURN ANALYSIS")
    print("="*70)
    
    # Step 1: Load Data
    print("\n[Step 1] Loading data...")
    data_file = 'bank_customer_data.csv'
    
    # Check if data file exists, if not generate it
    if not os.path.exists(data_file):
        print(f"Data file '{data_file}' not found. Generating sample data...")
        from generate_data import generate_customer_data
        df = generate_customer_data(10000)
        df.to_csv(data_file, index=False)
        print(f"Sample data generated and saved to '{data_file}'")
    else:
        df = load_data(data_file)
    
    if df is None:
        print("Error: Could not load data. Exiting.")
        return
    
    # Step 2: Data Preprocessing
    print("\n[Step 2] Preprocessing data...")
    df = handle_missing_values(df)
    
    # Step 3: Exploratory Data Analysis
    print("\n[Step 3] Performing exploratory data analysis...")
    generate_eda_summary(df, target_column='Exited')
    
    # Generate visualizations
    plot_target_distribution(df, target_column='Exited')
    
    numerical_cols = ['CreditScore', 'Age', 'Tenure', 'Balance', 'EstimatedSalary']
    plot_numerical_features(df, numerical_cols, target_column='Exited')
    
    categorical_cols = ['Geography', 'Gender', 'NumOfProducts', 'HasCrCard', 'IsActiveMember']
    plot_categorical_features(df, categorical_cols, target_column='Exited')
    
    # Analyze churn by key features
    analyze_churn_by_feature(df, 'Geography')
    analyze_churn_by_feature(df, 'Gender')
    analyze_churn_by_feature(df, 'NumOfProducts')
    analyze_churn_by_feature(df, 'IsActiveMember')
    
    # Step 4: Feature Engineering
    print("\n[Step 4] Engineering features...")
    df_engineered = create_derived_features(df)
    
    # Drop non-predictive columns
    columns_to_drop = ['CustomerId', 'Surname']
    df_model = df_engineered.drop(columns=columns_to_drop, errors='ignore')
    
    # Prepare data for modeling
    X, y = prepare_data_for_modeling(df_model, target_column='Exited')
    
    # Encode categorical features
    categorical_features = ['Geography', 'Gender', 'CreditScoreCategory', 
                           'AgeGroup', 'TenureCategory', 'BalanceCategory']
    X_encoded, label_encoders = encode_categorical_features(X, categorical_features)
    
    # Step 5: Split Data
    print("\n[Step 5] Splitting data into train and test sets...")
    X_train, X_test, y_train, y_test = split_data(X_encoded, y, test_size=0.2, random_state=42)
    
    # Scale features
    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)
    
    # Step 6: Model Training and Evaluation
    print("\n[Step 6] Training and evaluating models...")
    print("\n" + "-"*70)
    
    # Train Logistic Regression
    print("\n>>> Training Logistic Regression...")
    lr_model = train_logistic_regression(X_train_scaled, y_train)
    lr_metrics = evaluate_model(lr_model, X_test_scaled, y_test, model_name="Logistic Regression")
    y_pred_lr = lr_model.predict(X_test_scaled)
    y_pred_proba_lr = lr_model.predict_proba(X_test_scaled)[:, 1]
    plot_confusion_matrix(y_test, y_pred_lr, model_name="Logistic Regression")
    plot_roc_curve(y_test, y_pred_proba_lr, model_name="Logistic Regression")
    
    print("\n" + "-"*70)
    
    # Train Random Forest
    print("\n>>> Training Random Forest...")
    rf_model = train_random_forest(X_train, y_train, n_estimators=100, random_state=42)
    rf_metrics = evaluate_model(rf_model, X_test, y_test, model_name="Random Forest")
    y_pred_rf = rf_model.predict(X_test)
    y_pred_proba_rf = rf_model.predict_proba(X_test)[:, 1]
    plot_confusion_matrix(y_test, y_pred_rf, model_name="Random Forest")
    plot_roc_curve(y_test, y_pred_proba_rf, model_name="Random Forest")
    
    # Feature importance for Random Forest
    feature_names = X.columns.tolist()
    rf_importance = get_feature_importance(rf_model, feature_names, top_n=10)
    
    print("\n" + "-"*70)
    
    # Train Gradient Boosting
    print("\n>>> Training Gradient Boosting...")
    gb_model = train_gradient_boosting(X_train, y_train, n_estimators=100, random_state=42)
    gb_metrics = evaluate_model(gb_model, X_test, y_test, model_name="Gradient Boosting")
    y_pred_gb = gb_model.predict(X_test)
    y_pred_proba_gb = gb_model.predict_proba(X_test)[:, 1]
    plot_confusion_matrix(y_test, y_pred_gb, model_name="Gradient Boosting")
    plot_roc_curve(y_test, y_pred_proba_gb, model_name="Gradient Boosting")
    
    # Feature importance for Gradient Boosting
    gb_importance = get_feature_importance(gb_model, feature_names, top_n=10)
    
    # Step 7: Model Comparison
    print("\n[Step 7] Comparing models...")
    print("\n" + "="*70)
    print("MODEL COMPARISON SUMMARY")
    print("="*70)
    
    comparison_df = pd.DataFrame({
        'Model': ['Logistic Regression', 'Random Forest', 'Gradient Boosting'],
        'Accuracy': [lr_metrics['accuracy'], rf_metrics['accuracy'], gb_metrics['accuracy']],
        'Precision': [lr_metrics['precision'], rf_metrics['precision'], gb_metrics['precision']],
        'Recall': [lr_metrics['recall'], rf_metrics['recall'], gb_metrics['recall']],
        'F1-Score': [lr_metrics['f1_score'], rf_metrics['f1_score'], gb_metrics['f1_score']],
        'ROC-AUC': [lr_metrics['roc_auc'], rf_metrics['roc_auc'], gb_metrics['roc_auc']]
    })
    
    print("\n", comparison_df.to_string(index=False))
    
    # Determine best model
    best_model_idx = comparison_df['ROC-AUC'].idxmax()
    best_model_name = comparison_df.loc[best_model_idx, 'Model']
    print(f"\nBest performing model: {best_model_name} (ROC-AUC: {comparison_df.loc[best_model_idx, 'ROC-AUC']:.4f})")
    
    # Step 8: Key Insights and Recommendations
    print("\n[Step 8] Generating insights and recommendations...")
    print("\n" + "="*70)
    print("KEY INSIGHTS AND RECOMMENDATIONS")
    print("="*70)
    
    print("\n1. CHURN RISK FACTORS:")
    print("   Based on feature importance analysis, the top risk factors for churn are:")
    if rf_importance is not None:
        top_features = rf_importance.head(5)
        for idx, row in top_features.iterrows():
            print(f"   - {row['feature']}: {row['importance']:.4f}")
    
    print("\n2. CUSTOMER SEGMENTS AT RISK:")
    print("   - Customers with multiple products (3-4) show higher churn")
    print("   - Inactive members are more likely to leave")
    print("   - Older customers tend to have higher churn rates")
    print("   - Customers in Germany show elevated churn compared to other regions")
    
    print("\n3. RECOMMENDATIONS:")
    print("   - Implement targeted retention campaigns for high-risk segments")
    print("   - Focus on re-engaging inactive members with personalized offers")
    print("   - Review product bundling strategy to reduce complexity")
    print("   - Develop region-specific retention strategies, especially for Germany")
    print("   - Monitor customers with tenure < 3 years more closely")
    print("   - Consider early warning system based on the trained models")
    
    print("\n" + "="*70)
    print("Analysis complete! Visualizations and model outputs saved.")
    print("="*70)


if __name__ == '__main__':
    main()
