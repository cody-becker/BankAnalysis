Bank Analysis of Customer Churn
By Cody Becker

Overview
Customer churn — customers leaving a bank — is one of the most costly challenges financial institutions face, as retaining existing clients is far cheaper than acquiring new ones. This project analyzes a dataset of 1,000 bank customers to identify which characteristics predict churn, and builds a logistic regression model to classify whether a customer will leave or stay.
Goals:

Quantify churn rate disparities across customer segments
Identify the most significant predictors of churn
Build a logistic regression model to classify churn likelihood
Provide actionable retention insights based on the findings


Dataset
A simulated bank customer database of 1,000 records with the following key variables:
VariableTypeDescriptionExitedBinary (target)1 = churned, 0 = stayedAgeContinuousCustomer ageBalanceContinuousAccount balanceGeographyCategoricalFrance, Spain, or GermanyCreditScoreContinuousCustomer credit scoreEstimatedSalaryContinuousEstimated annual salary
Context: Mean estimated salary was ~$102,168 (range: $142–$200,000), indicating the bank primarily serves upper-middle-class clients.

Exploratory Analysis
Overall Churn Rate
Of 1,000 customers, approximately 800 stayed and 200 churned — a 20% baseline churn rate.
Key Patterns Found
Age: Retained customers averaged mid-30s; churned customers averaged mid-40s. The age distribution of churned customers skews noticeably older.
Account Balance: Retained customers showed wide balance variation ($0–$200k). Churned customers clustered between $75k–$150k, suggesting mid-to-high balance customers are most at risk.
Geography: Germany had nearly twice the churn rate of France and Spain. France and Spain both retained customers at ~85%, while Germany's retention rate was only ~68%.

Hypothesis Testing
Age Effect

H₀: Mean age of churned = mean age of retained
H₁: Mean ages differ
Test: Two-sample z-test
Result: Test statistic (8.3) >> critical value (1.96) → Reject H₀. Age has a highly significant effect on churn.

Geographic Effect

H₀: Churn rate is equal across France, Spain, and Germany
H₁: At least one churn rate differs
Test: Chi-square test of independence
Result: p-value < 0.05 → Reject H₀. Geography significantly affects churn behavior.


Logistic Regression Model
Modeled Exited as a function of Age, Balance, CreditScore, and EstimatedSalary.
Significant predictors (p < 0.05): Age, Balance
Non-significant: CreditScore, EstimatedSalary
Final Model
logit(Exited) = −4.13 + 0.059·Age + 7.13×10⁻⁶·Balance
Interpretation

Every additional year of age multiplies churn odds by ~1.06
Every $10,000 increase in balance multiplies churn odds by ~1.07
Credit score and salary showed no meaningful effect in this dataset


Conclusions

Age and balance are the primary churn drivers. Older, higher-balance customers are significantly more likely to leave.
Geography matters. German customers churn at nearly double the rate of French and Spanish customers.
Churn is not random. Customer characteristics reliably predict departure behavior.

Retention recommendation: Target older, higher-balance customers with incentives such as family savings plans, college fund products, or early retirement accounts — the segments most likely to leave and most valuable to keep.

Tech Stack

Language: Python
Libraries: Pandas, NumPy, Matplotlib, Statsmodels
Methods: Logistic regression, chi-square testing, two-sample z-test, exploratory data analysis
