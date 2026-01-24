"""
Generate sample banking customer data for churn analysis.
This creates a realistic dataset with various customer attributes.
"""

import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

def generate_customer_data(n_samples=10000):
    """
    Generate synthetic bank customer data.
    
    Args:
        n_samples: Number of customer records to generate
        
    Returns:
        DataFrame with customer data
    """
    
    # Customer ID
    customer_id = range(1, n_samples + 1)
    
    # Geography (Country)
    geography = np.random.choice(['France', 'Germany', 'Spain'], n_samples, p=[0.5, 0.25, 0.25])
    
    # Gender
    gender = np.random.choice(['Male', 'Female'], n_samples, p=[0.55, 0.45])
    
    # Age (18-92)
    age = np.random.normal(40, 12, n_samples).astype(int)
    age = np.clip(age, 18, 92)
    
    # Credit Score (350-850)
    credit_score = np.random.normal(650, 100, n_samples).astype(int)
    credit_score = np.clip(credit_score, 350, 850)
    
    # Tenure (0-10 years)
    tenure = np.random.choice(range(0, 11), n_samples, p=[0.05, 0.08, 0.1, 0.12, 0.13, 0.14, 0.13, 0.1, 0.08, 0.05, 0.02])
    
    # Account Balance
    balance = np.random.exponential(60000, n_samples)
    balance = np.clip(balance, 0, 250000)
    # Set some balances to exactly 0
    zero_balance_mask = np.random.random(n_samples) < 0.2
    balance[zero_balance_mask] = 0
    
    # Number of Products (1-4)
    # Distribution probabilities for different product counts
    PRODUCT_PROBABILITIES = [0.5, 0.46, 0.03, 0.01]
    num_products = np.random.choice([1, 2, 3, 4], n_samples, p=PRODUCT_PROBABILITIES)
    
    # Has Credit Card (0 or 1)
    has_cr_card = np.random.choice([0, 1], n_samples, p=[0.3, 0.7])
    
    # Is Active Member (0 or 1)
    is_active_member = np.random.choice([0, 1], n_samples, p=[0.48, 0.52])
    
    # Estimated Salary
    estimated_salary = np.random.normal(100000, 50000, n_samples)
    estimated_salary = np.clip(estimated_salary, 10000, 200000)
    
    # Generate churn based on multiple factors (realistic churn patterns)
    churn_probability = np.zeros(n_samples)
    
    # Base churn rate
    churn_probability += 0.15
    
    # Age effect (higher churn for older customers)
    churn_probability += (age - 40) / 200
    
    # Geography effect (Germany has higher churn)
    churn_probability[geography == 'Germany'] += 0.1
    
    # Product effect (customers with 3-4 products have higher churn - unusual products)
    churn_probability[num_products > 2] += 0.15
    
    # Active member effect (inactive members more likely to churn)
    churn_probability[is_active_member == 0] += 0.1
    
    # Balance effect (zero balance = higher churn)
    churn_probability[balance == 0] += 0.05
    
    # Tenure effect (lower tenure = higher churn)
    churn_probability += (5 - tenure) / 100
    
    # Credit score effect (lower score = slightly higher churn)
    churn_probability += (650 - credit_score) / 5000
    
    # Clip probabilities
    churn_probability = np.clip(churn_probability, 0, 0.8)
    
    # Generate actual churn based on probabilities
    exited = (np.random.random(n_samples) < churn_probability).astype(int)
    
    # Create DataFrame
    data = pd.DataFrame({
        'CustomerId': customer_id,
        'Surname': [f'Customer_{i}' for i in customer_id],
        'CreditScore': credit_score,
        'Geography': geography,
        'Gender': gender,
        'Age': age,
        'Tenure': tenure,
        'Balance': balance.round(2),
        'NumOfProducts': num_products,
        'HasCrCard': has_cr_card,
        'IsActiveMember': is_active_member,
        'EstimatedSalary': estimated_salary.round(2),
        'Exited': exited
    })
    
    return data


if __name__ == '__main__':
    # Generate data
    print("Generating bank customer data...")
    data = generate_customer_data(10000)
    
    # Save to CSV
    data.to_csv('bank_customer_data.csv', index=False)
    print(f"Dataset created: {data.shape[0]} rows, {data.shape[1]} columns")
    print(f"Churn rate: {data['Exited'].mean():.2%}")
    print(f"\nData saved to 'bank_customer_data.csv'")
    
    # Display sample
    print("\nSample data (first 5 rows):")
    print(data.head())
