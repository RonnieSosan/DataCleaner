import pandas as pd
import numpy as np
from datetime import datetime
import csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import *

#Learning curve
from sklearn.metrics import precision_recall_fscore_support
from sklearn.metrics import f1_score
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import validation_curve

# Import Classifiers
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

def CorrelationMatrix(Feature, DataFrame):
    DataFrame_Correlation_matrix = DataFrame.corr()
    print(DataFrame_Correlation_matrix[Feature].sort_values(ascending=False))

def ApplyModel(X, y_train, model):
    
    model.fit(X, y_train)
    y_pred  = model.predict(X)

    Accuracy = round(np.median(cross_val_score(model, X, y_train, cv = 5)),2)*100
 
    Error   = 1 - Accuracy
    
    precision = precision_score(y_train, y_pred) * 100
    recall = recall_score(y_train, y_pred) * 100
    f1score = f1_score(y_train, y_pred) * 100
    
    return (model, y_pred, Accuracy, Error, precision, recall, f1score)

