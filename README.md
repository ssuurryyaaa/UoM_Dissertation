# INTERACTION PATTERNS TO PREDICT THE USABILITY OF INTERACTIVE DASHBOARDS

## OBJECTIVE
The goal of this research was to extract the most common user interaction patterns on interactive dashboards and determine if they could be used to predict the usability of these dashboards. 

## DATASET

A secondary analysis was conducted on the dataset obtained  from a research on interactive dashboards [Alhamadi, M., Clinch, S. and Vigo, M., 2022, July. Modeling User Strategies on Interactive Information Dashboards. In Proceedings of the 30th ACM Conference on User Modeling, Adaptation and Personalization (pp. 191-201). https://doi.org/10.1145/3503252.3531296]  

## METHODOLOGY
The goal was achieved using two pipelines.

![Outline of the process of KDD from interaction patterns to determine usability](https://github.com/ssuurryyaaa/UoM_Dissertation/blob/main/images/METHOD.png)

The first pipeline involved:
1. Merging and pre-processing the user interaction logs
2. Finding unique representations of user interactions
3. Encoding these representations into numeric values to feed as input into the SPMF pattern mining tool

Pattern were retrieved the tool using VMSP algorithm.
Thematic analysis was done to understand the meaning of the interaction events.

The second pipeline involved:
1. The mapping of the extracted pattern with other usability factors
2. Analysing the correlation between the pattern frequencies and these usability metrics
3. Regression analysis to predict the usability of dashboards

## EVALUATION
1. The patterns mined from SPMF were benchmarked to identify the most suitable ones for further research by analysis the length of patterns and their support value.
2. Spearman correlation was used to determine the correlation between the frequency of patterns and usability results of the primary study.
3. MSE, R2, CV score were used for evaluation on the SVR analysis of patterns and usability factors.

## FINDINGS
1. Typical user behavior patterns were established across dashboards.
2. Comparable characteristics among users were witnessed based on their interaction.
3. Objective usability factors were explainable using interaction patterns.

