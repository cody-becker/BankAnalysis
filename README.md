# Bank Customer Churn Analysis

A Python program that analyzes banking customer data to predict which clients are most likely to "churn" (close their accounts or leave the bank). This tool uses data-processing techniques and machine-learning models to identify behavioral patterns associated with churn, helping banks understand risk factors and intervene before customers leave.

## Overview

Customer churn is a critical concern for banks, as retaining existing customers is typically more cost-effective than acquiring new ones. This analysis tool helps banks:

- **Identify at-risk customers** before they leave
- **Understand key drivers** of customer churn
- **Develop targeted retention strategies** based on data insights
- **Predict future churn** using machine learning models

## Features

### Data Processing
- Automated data loading and cleaning
- Missing value handling
- Feature scaling and encoding
- Train/test data splitting

### Exploratory Data Analysis (EDA)
- Churn rate distribution analysis
- Feature correlation analysis
- Visualization of key patterns
- Statistical summaries

### Feature Engineering
- Derived features creation (balance per product, engagement scores, etc.)
- Customer segmentation (age groups, tenure categories, etc.)
- Feature importance ranking

### Machine Learning Models
- **Logistic Regression** - Baseline interpretable model
- **Random Forest** - Ensemble method for robust predictions
- **Gradient Boosting** - Advanced boosting technique for high accuracy

### Model Evaluation
- Accuracy, Precision, Recall, F1-Score metrics
- ROC-AUC curves
- Confusion matrices
- Feature importance analysis

## Installation

1. Clone the repository:
```bash
git clone https://github.com/cody-becker/BankAnalysis.git
cd BankAnalysis
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start

Run the complete analysis pipeline:
```bash
python churn_analysis.py
```

This will:
1. Generate sample data (if not already present)
2. Perform exploratory data analysis
3. Engineer features
4. Train multiple machine learning models
5. Evaluate and compare models
6. Generate insights and visualizations

### Individual Modules

You can also use individual modules for specific tasks:

#### Generate Sample Data
```bash
python generate_data.py
```

#### Use Custom Data
Place your CSV file named `bank_customer_data.csv` in the project directory with the following columns:
- `CustomerId`: Unique customer identifier
- `Surname`: Customer surname
- `CreditScore`: Credit score (300-850)
- `Geography`: Customer's country
- `Gender`: Male/Female
- `Age`: Customer age
- `Tenure`: Years with the bank
- `Balance`: Account balance
- `NumOfProducts`: Number of bank products
- `HasCrCard`: Has credit card (0/1)
- `IsActiveMember`: Is active member (0/1)
- `EstimatedSalary`: Estimated salary
- `Exited`: Churned or not (0/1) - target variable

## Project Structure

```
BankAnalysis/
│
├── churn_analysis.py          # Main analysis script
├── data_preprocessing.py      # Data loading and cleaning
├── feature_engineering.py     # Feature creation and selection
├── eda.py                     # Exploratory data analysis
├── model_training.py          # ML model training and evaluation
├── generate_data.py           # Sample data generator
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Output

The analysis generates several outputs:

### Visualizations
- `churn_distribution.png` - Distribution of churned vs retained customers
- `numerical_features_distribution.png` - Box plots of numerical features
- `categorical_features_churn.png` - Churn rates by categorical features
- `correlation_matrix.png` - Feature correlation heatmap
- `confusion_matrix_*.png` - Confusion matrices for each model
- `roc_curve_*.png` - ROC curves for each model

### Console Output
- Dataset statistics and summary
- Churn analysis by key features
- Model performance metrics
- Feature importance rankings
- Key insights and recommendations

## Key Insights

Based on typical churn analysis, the program identifies:

1. **High-Risk Factors:**
   - Age (older customers tend to churn more)
   - Product complexity (customers with 3-4 products)
   - Inactivity (non-active members)
   - Geographic location (region-specific patterns)
   - Low tenure (newer customers are at higher risk)

2. **Protective Factors:**
   - Active membership
   - Moderate product usage (1-2 products)
   - Positive account balance
   - Longer tenure with the bank

## Model Performance

The program trains and compares three models:
- **Logistic Regression**: Fast, interpretable baseline
- **Random Forest**: Robust ensemble method
- **Gradient Boosting**: Typically highest accuracy

Models are evaluated on:
- Accuracy
- Precision (minimizing false positives)
- Recall (catching actual churners)
- F1-Score (balanced metric)
- ROC-AUC (overall discrimination ability)

## Requirements

- Python 3.7+
- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

See `requirements.txt` for specific versions.

## Use Cases

This tool is valuable for:
- **Bank Retention Teams**: Identify customers requiring intervention
- **Marketing Teams**: Design targeted retention campaigns
- **Customer Success**: Proactive customer engagement
- **Analytics Teams**: Understand churn patterns and trends
- **Executive Leadership**: Strategic decision-making on customer retention

## Future Enhancements

Potential improvements:
- Real-time churn prediction API
- Deep learning models (neural networks)
- Time-series analysis for churn trends
- Customer lifetime value (CLV) integration
- A/B testing framework for retention strategies
- Interactive dashboard with Plotly/Dash

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available for educational and commercial use.

## Contact

For questions or feedback, please open an issue on GitHub.