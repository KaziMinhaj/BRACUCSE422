# -*- coding: utf-8 -*-
"""CSE422_18101708_glass_source_dataset.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Um8_d8r_I1a84PAUUhh-JBFFEC_WlUZu
"""

import numpy as np
import pandas as pd

df = pd.read_csv('/content/sample_data/glass source classification dataset.csv')
df.isnull().sum()
from sklearn.impute import SimpleImputer
impute = SimpleImputer(missing_values=np.nan, strategy='mean')
impute.fit(df[['Ca']])
df['Ca'] = impute.transform(df[['Ca']])
df.isnull().sum()
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
df['Ba'] = enc.fit_transform(df['Ba'])
df['Fe'] = enc.fit_transform(df['Fe'])
df['Type'] = enc.fit_transform(df['Type'])
df.head()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# X = feature values, all the columns except the last column
x = df.iloc[:, :-1]
# y = target values, last column of the data frame
y = df.iloc[:, -1]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=30)
model = LogisticRegression()
model.fit(x_train, y_train) 
predictions = model.predict(x_test)
print(predictions)

from sklearn.metrics import accuracy_score
print( accuracy_score(y_test, predictions))

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
X = df.iloc[:,1:12]
y = df.iloc[:,-1]
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=1)
clf = DecisionTreeClassifier(criterion='entropy',random_state=1)
clf.fit(X_train,y_train)
y_pred = clf.predict(X_test)
score=accuracy_score(y_pred,y_test)
print(score)

#Comparing the accuracy and plot them as a bar chart

import matplotlib.pyplot as plt

reg = np.sum(predictions)
DTree = np.sum(y_pred)
fig, ax = plt.subplots()
rects1 = ax.bar(reg , predictions, .5, label='before')
rects2 = ax.bar(DTree, y_pred, .5, label='after')
ax.set_ylabel('Scores')
ax.set_title('Scores by accuracy')
ax.legend()
fig.tight_layout()
plt.show()