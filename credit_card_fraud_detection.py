# -*- coding: utf-8 -*-
"""Credit Card Fraud Detection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15JhEF_Ik3WfJRGLUaZ_Cv2Nh_arXamPr

## **Credit Card Fraud Detection**
"""

#importing the dependencies
import numpy as np
import pandas as pd 
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#loading the dataset to a panda dataFrame
cc_data = pd.read_csv('/content/creditcard.csv')

#checking the information in the dataset
cc_data.info()

#finding the number of missing values
cc_data.isna().sum().sum()

#distribution of legit transaction and fraudelent transaction 
cc_data['Class'].value_counts()

#seperating the data for analysis
real = cc_data[cc_data.Class == 0]
unreal = cc_data[cc_data.Class == 1]

print(real.shape)
print(unreal.shape)

#stastical measures of the data
real.Amount.describe()
unreal.Amount.describe()

#comapre the values for the both the transaction
cc_data.groupby('Class').mean()

#taking samples from legit transaction to make an unbiased dataset
real_SubPart = real.sample(n=492) #random sampling 
#concatenating two DataFrames :
unbaised_set = pd.concat([real_SubPart,unreal], axis=0)

unbaised_set['Class'].value_counts()

unbaised_set.groupby('Class').mean()

#split the data into features and targets
a=unbaised_set.drop(columns='Class', axis=1)
b=unbaised_set['Class']
print(a)
print(b)

#scaling the data 
scaler = StandardScaler()
a_scaled = scaler.fit_transform(a)

#split the data into training data and testing data 
a_train, a_test, b_train, b_test = train_test_split(a_scaled, b, test_size=0.2, stratify=b, random_state=2)

#model training (logistic regression)
Model = LogisticRegression(max_iter=2000)
Model.fit(a_train, b_train)

#model evaluation
a_TrainPrediction = Model.predict(a_train)
TrainData_acc = accuracy_score(a_TrainPrediction, b_train)

print('Accuracy score is : ', TrainData_acc )

a_TestPrediction = Model.predict(a_test)
TestData_acc = accuracy_score(a_TestPrediction, b_test)

print('the accuracy score of the Test Data is : ', TestData_acc)