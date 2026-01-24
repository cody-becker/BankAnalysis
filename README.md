Final Project: Bank Analysis of Customer Churn
By: Cody Becker
Introduction
Customer churning, or leaving, is one of the most important challenges that banks face today’s economic state, as retaining existing clients is often much cheaper than acquiring new ones. This report analyzes a dataset of 1,000 bank customers and their characteristics relating to their decision to leave or stay with the bank.  


This report aims to conduct a rigorous data analysis to:
	Investigate and quantify the disparities in churn rates among different groups of customers.
	Build a predictive model using logistic regression to classify whether a customer will churn or not based on their attributes.
By understanding these patterns, we can provide actionable insights into customer behavior and highlight which segments are most at risk of leaving. These findings can inform targeted retention strategies and improve overall customer loyalty.


Dataset Description
The dataset used is a example of a bank’s customer database with factors of each customer, tied directly to which stay and which churn or leave the bank. 
Variables Used: 
	Exited: Target variable indicating whether the customer churned (0 = stayed, 1 = left).
	Age: Continuous variable representing customer age.
	 Balance: Continuous variable representing account balance.
	Geography: Categorical variable indicating customer location (France, Spain, Germany).
	CreditScore: Continuous variable representing the customer’s credit score.


Data Organization:

Summary Statistics for selected variables:

 

Explanation: The mean estimated salary in this dataset is about $102,168, with values ranging from $142 to $200,000. The standard deviation indicates that most customers fall between roughly $45,000 and $159,000, suggesting that the bank primarily serves upper middle class clients. This provides important context for interpreting churn behavior, since the customer base is relatively affluent compared to the general population.




 Contingency table (grand total percentage):

 
 

   From these 2 x 2 contingency tables, we noticed that customers from France and Spain tend to stay with the bank at around an 85% rate, while customers from Germany only stay at a 68% rate, showing a clear geographic disparity in churn behavior.










Data Visualization: (at least 3)
 
Figure: Bar graph showing total customers staying vs churned.
From this bar graph we can see the overall churn rate for this bank. With this sample of 1,000 customers, around 800 of them stayed with the bank, and the other 200 decided to leave, or in this case churned. This sets a baseline of churn rate of about 20% amongst customers, which will further be tested.
 
Figure: Boxplot of age distribution of customers who both stayed and left the bank.
From this boxplot we can see that the customers that were retained within the bank on average were around their mid-30’s. While those who left, who overall at an average of around mid-40’s. The median age of churned customers is noticeably higher, and their age distribution skews older overall.
 



Figure: Boxplot of account balance for customers who were retained and churned.
This boxplot shows that customers who stayed with the bank had a much larger difference in account balance, ranging from nearly $0 to $200,000. While those who left had a much closer range of balance, mostly between $75k and $150k.


 

Figure: Bar graph of geography of customers who left the bank
From this bar chart we can clearly see that Germany has the highest churn rate among the three countries, followed by Spain and France. Customers from Germany almost twice as likely to leave compared to the other two countries.


Data Analysis
Hypothesis Testing
We want to conduct hypothesis testing to see whether there is a gender effect or age effect on the survival status.
	Investigate the age effect:
  H_0: μ_"churned" =μ_"retained"   
H_1: μ_"churned" ≠μ_"retained" 


We will conduct a two sample proportion z test to determine whether to reject H_0or not.


 

 


Since the test statistics (8.3) is much larger than the critical value (1.96), we reject the null hypothesis and conclude that age has a very significant effect on customers who are retained and those who churn, as those who do leave are older on average.










	Investigate the geographic effect:
       H_0: π_"Germany" =π_"France" =π_"Spain" 
 H_1: At least one churn rate differs

We will conduct a Chi-square to see whether there is a geographic effect on churn status.

We conduct a chi square test of independence to see whether geography affects churn status. From the contingency table shown earlier, Germany’s churn rate is higher than France and Spain. The chi square test gives a p value less than 0.05, so we reject the null hypothesis and conclude that geography has a significant effect on churn

Regression
Based on what we found in the previous part and previous knowledge, we model Exited (churn) as a function of Age, Balance, Credit Score, and Estimated Salary.


 



 



We found that Age and Balance are significant (p-value < 0.05) while Credit Score and Estimated Salary are not. Therefore, our final model is: 
logit (Exited)=−4.13+0.059⋅Age+7.13×10^−6⋅Balance

Interpretation: As a customer’s age goes up by a year, the odds of churn multiply by ≈ 1.06, or older customers are more likely to leave the bank. As a customer’s balance increases by $10,000, the odds of churn multiply by ≈1.07. And credit score and estimated salary had p values well above 0.05, so they do not show meaningful effects on churn in this dataset.
Conclusion
This analysis provides a clear, data-driven narrative of customer churn within a bank.
	Significant Disparities Confirmed: Clear disparities in customer churn were observed. Older customers and those with higher balances were significantly more likely to leave the bank, while younger customers with lower balances were less likely to leave.
	Primary Factors: The most critical factors determining churn were age and balance. While location has some effect it didn’t change enough to truly sway the data one way. Credit scores and estimated salary did not seem to have any meaningful effects. This shows us that customer churn isn’t random and is caused by customer’s characteristics.  
In summary, while customer churn at times can feel like it is unpredictable, the data shows a much different story. Older and higher balance customers were much more likely to choose to leave the bank. While younger and lower balance customers continuously seemed to stay with the bank a lot more. So, for target retention this bank should look to give incentives like family saving plans, college fund discounts, or early retirement starting. This will only continue to increase business by keeping the more valuable customers and even stealing competition from other banks.
