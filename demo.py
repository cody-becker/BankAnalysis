"""
Quick demo script to showcase the bank churn analysis system.
This demonstrates how to use the system with minimal code.
"""

import warnings
warnings.filterwarnings('ignore')

print("="*70)
print("BANK CUSTOMER CHURN ANALYSIS - QUICK DEMO")
print("="*70)
print()

# Import and run the main analysis
from churn_analysis import main

# Run the complete analysis
main()

print("\n")
print("="*70)
print("DEMO COMPLETE!")
print("="*70)
print("\nGenerated files:")
print("  - bank_customer_data.csv (sample dataset)")
print("  - churn_distribution.png (churn rate visualization)")
print("  - numerical_features_distribution.png (feature analysis)")
print("  - categorical_features_churn.png (categorical analysis)")
print("  - confusion_matrix_*.png (model confusion matrices)")
print("  - roc_curve_*.png (model ROC curves)")
print("\nFor more details, see README.md")
