"""
Machine learning models for bank customer churn prediction.
Implements classification models and evaluation metrics.
"""

import numpy as np
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report, roc_auc_score, roc_curve
)
import matplotlib.pyplot as plt
import seaborn as sns


def split_data(X, y, test_size=0.2, random_state=42):
    """
    Split data into training and testing sets.
    
    Args:
        X: Features
        y: Target variable
        test_size: Proportion of data for testing
        random_state: Random seed for reproducibility
        
    Returns:
        X_train, X_test, y_train, y_test
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    
    print(f"Training set size: {X_train.shape[0]}")
    print(f"Test set size: {X_test.shape[0]}")
    print(f"Training set churn rate: {y_train.mean():.2%}")
    print(f"Test set churn rate: {y_test.mean():.2%}")
    
    return X_train, X_test, y_train, y_test


def train_logistic_regression(X_train, y_train, random_state=42):
    """
    Train a Logistic Regression model.
    
    Args:
        X_train: Training features
        y_train: Training target
        random_state: Random seed
        
    Returns:
        Trained model
    """
    model = LogisticRegression(random_state=random_state, max_iter=1000)
    model.fit(X_train, y_train)
    print("Logistic Regression model trained successfully")
    return model


def train_random_forest(X_train, y_train, n_estimators=100, random_state=42):
    """
    Train a Random Forest model.
    
    Args:
        X_train: Training features
        y_train: Training target
        n_estimators: Number of trees
        random_state: Random seed
        
    Returns:
        Trained model
    """
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        random_state=random_state,
        n_jobs=-1
    )
    model.fit(X_train, y_train)
    print("Random Forest model trained successfully")
    return model


def train_gradient_boosting(X_train, y_train, n_estimators=100, random_state=42):
    """
    Train a Gradient Boosting model.
    
    Args:
        X_train: Training features
        y_train: Training target
        n_estimators: Number of boosting stages
        random_state: Random seed
        
    Returns:
        Trained model
    """
    model = GradientBoostingClassifier(
        n_estimators=n_estimators,
        random_state=random_state
    )
    model.fit(X_train, y_train)
    print("Gradient Boosting model trained successfully")
    return model


def evaluate_model(model, X_test, y_test, model_name="Model"):
    """
    Evaluate model performance on test data.
    
    Args:
        model: Trained model
        X_test: Test features
        y_test: Test target
        model_name: Name of the model for display
        
    Returns:
        Dictionary of evaluation metrics
    """
    # Make predictions
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)[:, 1]
    
    # Calculate metrics
    metrics = {
        'accuracy': accuracy_score(y_test, y_pred),
        'precision': precision_score(y_test, y_pred),
        'recall': recall_score(y_test, y_pred),
        'f1_score': f1_score(y_test, y_pred),
        'roc_auc': roc_auc_score(y_test, y_pred_proba)
    }
    
    print(f"\n=== {model_name} Performance ===")
    print(f"Accuracy:  {metrics['accuracy']:.4f}")
    print(f"Precision: {metrics['precision']:.4f}")
    print(f"Recall:    {metrics['recall']:.4f}")
    print(f"F1-Score:  {metrics['f1_score']:.4f}")
    print(f"ROC-AUC:   {metrics['roc_auc']:.4f}")
    
    print(f"\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
    
    print(f"\nClassification Report:")
    print(classification_report(y_test, y_pred))
    
    return metrics


def get_feature_importance(model, feature_names, top_n=10):
    """
    Get feature importance from tree-based models.
    
    Args:
        model: Trained model (must have feature_importances_)
        feature_names: List of feature names
        top_n: Number of top features to display
        
    Returns:
        DataFrame with feature importance
    """
    if hasattr(model, 'feature_importances_'):
        importance_df = pd.DataFrame({
            'feature': feature_names,
            'importance': model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        print(f"\n=== Top {top_n} Important Features ===")
        print(importance_df.head(top_n))
        
        return importance_df
    else:
        print("Model does not support feature importance")
        return None


def plot_confusion_matrix(y_test, y_pred, model_name="Model"):
    """
    Plot confusion matrix heatmap.
    
    Args:
        y_test: True labels
        y_pred: Predicted labels
        model_name: Name of the model
    """
    cm = confusion_matrix(y_test, y_pred)
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                xticklabels=['Retained', 'Churned'],
                yticklabels=['Retained', 'Churned'])
    plt.title(f'{model_name} - Confusion Matrix')
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.tight_layout()
    plt.savefig(f'confusion_matrix_{model_name.lower().replace(" ", "_")}.png', dpi=150)
    print(f"Confusion matrix saved as confusion_matrix_{model_name.lower().replace(' ', '_')}.png")
    plt.close()


def plot_roc_curve(y_test, y_pred_proba, model_name="Model"):
    """
    Plot ROC curve.
    
    Args:
        y_test: True labels
        y_pred_proba: Predicted probabilities
        model_name: Name of the model
    """
    fpr, tpr, _ = roc_curve(y_test, y_pred_proba)
    roc_auc = roc_auc_score(y_test, y_pred_proba)
    
    plt.figure(figsize=(8, 6))
    plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
    plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random Classifier')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title(f'{model_name} - ROC Curve')
    plt.legend(loc="lower right")
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(f'roc_curve_{model_name.lower().replace(" ", "_")}.png', dpi=150)
    print(f"ROC curve saved as roc_curve_{model_name.lower().replace(' ', '_')}.png")
    plt.close()


# Import pandas for feature importance display
import pandas as pd
