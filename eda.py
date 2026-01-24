"""
Exploratory Data Analysis (EDA) module for bank customer churn analysis.
Provides visualization and statistical analysis functions.
"""

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np


def plot_target_distribution(df, target_column='Exited'):
    """
    Plot the distribution of the target variable (churn).
    
    Args:
        df: Input DataFrame
        target_column: Name of the target column
    """
    plt.figure(figsize=(8, 6))
    
    # Count plot
    counts = df[target_column].value_counts()
    percentages = df[target_column].value_counts(normalize=True) * 100
    
    plt.subplot(1, 2, 1)
    sns.countplot(data=df, x=target_column)
    plt.title('Customer Churn Distribution')
    plt.xlabel('Churned (0=No, 1=Yes)')
    plt.ylabel('Count')
    
    # Add percentage labels
    for i, (count, pct) in enumerate(zip(counts, percentages)):
        plt.text(i, count, f'{count}\n({pct:.1f}%)', ha='center', va='bottom')
    
    # Pie chart
    plt.subplot(1, 2, 2)
    plt.pie(counts, labels=['Retained', 'Churned'], autopct='%1.1f%%', startangle=90)
    plt.title('Churn Rate')
    
    plt.tight_layout()
    plt.savefig('churn_distribution.png', dpi=150)
    print("Churn distribution plot saved as churn_distribution.png")
    plt.close()


def plot_numerical_features(df, numerical_cols, target_column='Exited'):
    """
    Plot distributions of numerical features by churn status.
    
    Args:
        df: Input DataFrame
        numerical_cols: List of numerical column names
        target_column: Name of the target column
    """
    n_cols = len(numerical_cols)
    n_rows = (n_cols + 2) // 3
    
    fig, axes = plt.subplots(n_rows, 3, figsize=(15, 5 * n_rows))
    axes = axes.flatten() if n_cols > 1 else [axes]
    
    for idx, col in enumerate(numerical_cols):
        if idx < len(axes):
            df.boxplot(column=col, by=target_column, ax=axes[idx])
            axes[idx].set_title(f'{col} by Churn Status')
            axes[idx].set_xlabel('Churned (0=No, 1=Yes)')
            axes[idx].set_ylabel(col)
            plt.sca(axes[idx])
            plt.xticks([1, 2], ['Retained', 'Churned'])
    
    # Hide extra subplots
    for idx in range(n_cols, len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('numerical_features_distribution.png', dpi=150)
    print("Numerical features distribution plot saved as numerical_features_distribution.png")
    plt.close()


def plot_categorical_features(df, categorical_cols, target_column='Exited'):
    """
    Plot distributions of categorical features by churn status.
    
    Args:
        df: Input DataFrame
        categorical_cols: List of categorical column names
        target_column: Name of the target column
    """
    n_cols = len(categorical_cols)
    n_rows = (n_cols + 1) // 2
    
    fig, axes = plt.subplots(n_rows, 2, figsize=(14, 5 * n_rows))
    if n_rows == 1:
        axes = axes.reshape(1, -1)
    axes = axes.flatten()
    
    for idx, col in enumerate(categorical_cols):
        if idx < len(axes) and col in df.columns:
            # Create crosstab for churn by category
            ct = pd.crosstab(df[col], df[target_column], normalize='index') * 100
            ct.plot(kind='bar', ax=axes[idx], stacked=False)
            axes[idx].set_title(f'Churn Rate by {col}')
            axes[idx].set_xlabel(col)
            axes[idx].set_ylabel('Percentage (%)')
            axes[idx].legend(['Retained', 'Churned'])
            axes[idx].tick_params(axis='x', rotation=45)
    
    # Hide extra subplots
    for idx in range(n_cols, len(axes)):
        axes[idx].set_visible(False)
    
    plt.tight_layout()
    plt.savefig('categorical_features_churn.png', dpi=150)
    print("Categorical features churn plot saved as categorical_features_churn.png")
    plt.close()


def plot_correlation_matrix(df, numerical_cols):
    """
    Plot correlation matrix of numerical features.
    
    Args:
        df: Input DataFrame
        numerical_cols: List of numerical column names
    """
    plt.figure(figsize=(12, 10))
    
    # Select only numerical columns that exist
    available_cols = [col for col in numerical_cols if col in df.columns]
    corr_matrix = df[available_cols].corr()
    
    sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm', 
                center=0, square=True, linewidths=1)
    plt.title('Feature Correlation Matrix')
    plt.tight_layout()
    plt.savefig('correlation_matrix.png', dpi=150)
    print("Correlation matrix saved as correlation_matrix.png")
    plt.close()


def analyze_churn_by_feature(df, feature, target_column='Exited'):
    """
    Analyze churn rate by a specific feature.
    
    Args:
        df: Input DataFrame
        feature: Feature name to analyze
        target_column: Name of the target column
    """
    print(f"\n=== Churn Analysis by {feature} ===")
    
    if feature in df.columns:
        churn_by_feature = df.groupby(feature)[target_column].agg(['mean', 'count'])
        churn_by_feature.columns = ['Churn_Rate', 'Count']
        churn_by_feature['Churn_Rate'] = churn_by_feature['Churn_Rate'] * 100
        print(churn_by_feature.sort_values('Churn_Rate', ascending=False))
    else:
        print(f"Feature '{feature}' not found in dataframe")


def generate_eda_summary(df, target_column='Exited'):
    """
    Generate a comprehensive EDA summary.
    
    Args:
        df: Input DataFrame
        target_column: Name of the target column
    """
    print("\n" + "="*60)
    print("EXPLORATORY DATA ANALYSIS SUMMARY")
    print("="*60)
    
    # Dataset overview
    print(f"\nDataset shape: {df.shape[0]} rows, {df.shape[1]} columns")
    print(f"\nOverall churn rate: {df[target_column].mean():.2%}")
    
    # Missing values
    missing = df.isnull().sum()
    if missing.sum() > 0:
        print(f"\nMissing values:")
        print(missing[missing > 0])
    else:
        print("\nNo missing values detected")
    
    # Data types
    print(f"\nData types:")
    print(df.dtypes.value_counts())
    
    # Key statistics
    numerical_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if target_column in numerical_cols:
        numerical_cols.remove(target_column)
    
    if numerical_cols:
        print(f"\n=== Numerical Features Summary ===")
        print(df[numerical_cols].describe())
    
    # Categorical features
    categorical_cols = df.select_dtypes(include=['object']).columns.tolist()
    if categorical_cols:
        print(f"\n=== Categorical Features ===")
        for col in categorical_cols:
            print(f"\n{col}: {df[col].nunique()} unique values")
            print(df[col].value_counts().head())
