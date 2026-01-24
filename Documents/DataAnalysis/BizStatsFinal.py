import kagglehub
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import statsmodels.api as sm
import scipy.stats as stats
import pandas as pd
import os
from scipy import stats 
import statsmodels.stats.proportion as smp


# Download latest version of the dataset
path = kagglehub.dataset_download("mathchi/churn-for-bank-customers")
print("Path to dataset files:", path)

# Check what files are inside
print("Files in folder:", os.listdir(path))

# Load the CSV (the filename is usually 'Churn_Modelling.csv')
df = pd.read_csv(f"{path}/churn.csv")


# Optional: sample only 1000 rows for project
df = df.sample(n=1000, random_state=42)

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())

sns.countplot(x="Exited", data=df)
plt.title("Churned vs Retained Customers")
plt.show()

sns.boxplot(x="Exited", y="Age", data=df)
plt.title("Age Distribution by Churn Status")
plt.show()


sns.boxplot(x="Exited", y="Balance", data=df)
plt.title("Balance Distribution by Churn Status")
plt.show()

sns.barplot(x="Geography", y="Exited", data=df, estimator=lambda x: sum(x)/len(x))
plt.title("Churn Rate by Geography")
plt.show()

# Assuming your dataframe is called df
contingency_percent = pd.crosstab(
    df['Geography'], 
    df['Exited'], 
    normalize='index'   # gives row percentages
) * 100

# Split ages by churn status
age_churned = df[df['Exited'] == 1]['Age']
age_retained = df[df['Exited'] == 0]['Age']

# Independent samples t-test
t_stat, p_val = stats.ttest_ind(age_churned, age_retained)

print("T-statistic:", t_stat)
print("P-value:", p_val)

# Number of churned customers
churned = df['Exited'].sum()
total = len(df)

ci_low, ci_high = smp.proportion_confint(churned, total, alpha=0.05, method='wilson')

print("Churn rate:", churned/total)
print("95% CI:", (ci_low, ci_high))

# Logistic Regression

X = df[['CreditScore','Age','Balance','EstimatedSalary']]
y = df['Exited']

X = sm.add_constant(X)
logit_model = sm.Logit(y, X).fit()
print(logit_model.summary())

contingency = pd.crosstab(df['Geography'], df['Exited'], margins=True, normalize=False)

print(contingency_percent)



