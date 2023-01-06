import numpy as np
import pandas as pd
from load_dataset import ld
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

df = ld("car_price.csv")
#dividing dataset into train , valiadate and test data set
#df.sample to shuffle data set , first slice upto 60%, second 60-80%, rest
train, valid, test = np.split(df.sample(frac=1), [int(0.6 * len(df)), int(0.8 * len(df))])

#scaling dataset to reduce too much skewness
def scale_dataset(df, oversample=False):
    x = df[df.columns[:-1]].values
    y = df[df.columns[-1]].values

    lab = LabelEncoder()
    y = lab.fit_transform(y)
    
    scaler = StandardScaler()
    x = scaler.fit_transform(x)
    
    if oversample:
        ros = RandomOverSampler()
        x, y = ros.fit_resample(x, y)
    
    data = np.hstack((x, np.reshape(y, (-1, 1))))
    
    return data, x, y

train, x_train, y_train = scale_dataset(train, oversample=True)
valid, x_valid, y_valid = scale_dataset(valid)
test, x_test, y_test = scale_dataset(test)


#KNN 
knn_model = KNeighborsClassifier(n_neighbors=20)
knn_model.fit(x_train, y_train)

y_pred = knn_model.predict(x_test)

print(classification_report(y_pred, y_test))

