import pandas as pd
from reader3 import Table, convertor, test_convertor
from sklearn import preprocessing
import numpy as np

import matplotlib.pyplot as plt
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFECV
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection.tests.test_split import train_test_split
from sklearn import model_selection
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.feature_selection import RFECV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import seaborn as sns
from sklearn.metrics import confusion_matrix


pd.set_option('max_columns', None)


tb = Table(["01_all_users.csv","02_events_log.csv","03_lk_events_log.csv","04_is_blocked.csv","test.csv"])
hr = convertor(tb.get_all_users())
col_names = hr.columns.tolist()
print("Пример данных:")
