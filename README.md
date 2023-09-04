![license](https://img.shields.io/badge/License-MIT-green.svg)![python](https://img.shields.io/badge/python-3.10-blue)

# University Of Manchester MSc Data Science (CSDI Pathway) Dissertation Project
# Title - INTERACTION PATTERNS TO PREDICT THE USABILITY OF INTERACTIVE DASHBOARDS

## Installation
1. Upgrade python pip package manager. 
```bash
python3 -m pip install --user --upgrade pip
python3 -m pip --version
```
2. Create python virtual environment and activate install.
```bash
python3 -m venv uom_venv
.\uom_venv\Scripts\activate
```
3. Install required packages.
```bash
pip install -r requirements.txt
```

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

Patterns were retrieved by the tool using the VMSP algorithm.
Thematic analysis was done to understand the meaning of the interaction events.

The second pipeline involved:
1. The mapping of the extracted pattern with other usability factors
2. Analysing the correlation between the pattern frequencies and these usability metrics
3. Regression analysis to predict the usability of dashboards

## RESULTS
| Min Support (%) | Max Gap | Total Number of Patterns | Max Pattern Length (mxL) | Max Support Value at Max Length (mxS) | Net Score (mxL * mxS) | Number of Patterns Over Benchmark Score |
|-----------------|---------|--------------------------|---------------------------|----------------------------------------|-----------------------|--------------------------------------|
| 100             | 0       | 43                       | 7                         | 16                                     | 112                   | 0                                    |
| 90              | 0       | 79                       | 9                         | 15                                     | 135                   | 2                                    |
| 80              | 0       | 287                      | 10                        | 15                                     | 150                   | 2                                    |
| 70              | 0       | 584                      | 12                        | 12                                     | 144                   | 2                                    |
| 60              | 0       | 1596                     | 12                        | 12                                     | 144                   | 2                                    |
| 50              | 0       | 2677                     | 14                        | 8                                      | 112                   | 0                                    |


## EVALUATION
1. The patterns mined from SPMF were benchmarked to identify the most suitable ones for further research by analysis the length of patterns and their support value.
2. Spearman correlation was used to determine the correlation between the frequency of patterns and usability results of the primary study.
3. MSE, R2, CV score were used for evaluation on the SVR analysis of patterns and usability factors.

## FINDINGS
1. Typical user behavior patterns were established across dashboards.
2. Comparable characteristics among users were witnessed based on their interaction.
3. Objective usability factors were explainable using interaction patterns.

