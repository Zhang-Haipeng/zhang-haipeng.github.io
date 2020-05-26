---
layout: post
title: Writing Sample
tags: [other]
excerpt_separator: <!--more-->
---

**This is the `introduction` part that I wrote for my current group project's proposal. The company's name is anonymized for confidentiality.** <br>
<!--more-->
<br>
## Introduction

### Business Background
* At the core of Company_Name's business is balancing risk with profit. The ability to predict the likelihood and impact of a client not paying back a loan is of up-most importance. <br>
* As a competitive fintech company, Company_Name needs tools to estimate the credit risk of its potential loan clients in a fast, quantified, accurate and objective manner. 

### Importance of the project
The "Golden Rule" in evaluating a financing business is to always consider `profit` and `risk` together. Looking at `profit` only could be misleading.<br>
Traditionally, lenders assess the risk of a potential loan client by manually checking the client's background, financial status, financing history, and so on. But such an approach has many disadvantages:<br>
1. The manual approach is slow, increasing the risk of losing the good clients. <br>
2. It is qualitative, meaning the lender can not know how much riskier one client is over another.<br> 
3. It is subjective. The result is given based on people's judgment which may not reliable. <br>
4. The person assessing the risk might be giving fake reports (operational risk). <br>
Compared with the manual approach, machine learning models are fast, quantitative, objective, and transparent (either in terms of interpretability or methodology). Properly built, they can also be accurate. 

### Two targets
In order to quantify the risk, we aim to predict two targets, the Probability of Default (PD) and the Percentage of Loss Given Default (Loss_Pct).<br> 
* **The Probability of Default (PD)**<br>
![Travel]({{ "assets/img/temp/intro_1.png" | relative_url}})<br>
As is shown above, the prediction of `PD` would be a supervised machine learning model development task, where the `y` would be binary labels (default/not default). <br>
<br>
* **The Percentage of Loss Given Default (Loss_Pct)** <br>
![Travel]({{ "assets/img/temp/intro_2.png" | relative_url}})<br>
`Loss_Pct` means given the merchants can't repay the money, what percentage of the money we will lose. As is shown above, this task will be a regression task, where `y` would be numeric values. <br>
<br>
_PD * Loss_Pct = Expected Loss % (EL)_<br>
Multiplying the two parameters will yield the `Expected Loss % (EL)`, allowing us to assess the clients' risk levels before doing business with them. 

### Data Product
![Travel]({{ "assets/img/temp/intro_3.png" | relative_url}})<br>
The major data product of this project will be the two models (`PD` and `Loss_Pct`). With those two models, having the client's data as input, we'll be able to assess the risk levels as needed, which brings valuable insights for making key business decisions. <br>
The team will also provide documentation on the model development process. Make relevant analysis reports and use proper visualizations where necessary. <br>
