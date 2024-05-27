import sklearn.datasets
import sklearn.model_selection
import sklearn.tree
import sklearn.metrics
import random
import csv
import numpy
import pandas as pd
import sklearn.cluster
import sklearn.datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

text = pd.read_csv("WineDatabase.csv")
tempTrainingLabels = []
tempTrainingData = []
for i in range(1, len(text["quality"])):
    numbers = text.iloc[i][:-1]
    arr = []
    for j in range(len(numbers)):
        arr.append(numbers[j])
    quality = text.iloc[i][-1]
    tempTrainingData.append(arr)
    tempTrainingLabels.append(quality)

vTrainingData,vTestingData,vTrainingLabels,vTestingLabel=sklearn.model_selection.train_test_split(tempTrainingData,tempTrainingLabels,test_size=80,shuffle=True)

dict =  {
        "00": "standard scaler with decision tree", 
        "01": "standard scaler with linear discriminant analysis",
        "02": "standard scaler with guassian naive bayes",
        "03": "standard scaler with support vector machine",
        "04": "standard scaler with kmeans",
        "10": "MaxAbsScaler with decision tree",
        "11": "MaxAbsScaler with linear discriminant analysis",
        "12": "MaxAbsScaler with guassian naive bayes",
        "13": "MaxAbsScaler with support vector machine",
        "14": "MaxAbsScaler with kmeans",
        "20": "MinMaxScaler with decision tree",
        "21": "MinMaxScaler with linear discriminant analysis",
        "22": "MinMaxScaler with guassian naive bayes",
        "23": "MinMaxScaler with support vector machine",
        "24": "MinMaxScaler with kmeans",
        "30": "Normalizer with decision tree",
        "31": "Normalizer with linear discriminant analysis",
        "32": "Normalizer with guassian naive bayes",
        "33": "Normalizer with support vector machine",
        "34": "Normalizer with kmeans",
        "40": "RobustScaler with decision tree",
        "41": "RobustScaler with linear discriminant analysis",
        "42": "RobustScaler with guassian naive bayes",
        "43": "RobustScaler with support vector machine",
        "44": "RobustScaler with kmeans",
        "50": "no scaling with decision tree",
        "51": "no scaling with linear discriminant analysis",
        "52": "no scaling with guassian naive bayes",
        "53": "no scaling with support vector machine",
        "54": "no scaling with kmeans",
}

print("Wine Dataset:")
for i in range(6):
    if (i == 0):
        vScaler = sklearn.preprocessing.StandardScaler()
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)

    if (i == 1): 
        vScaler = sklearn.preprocessing.MaxAbsScaler()
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)

    if (i == 2):
        vScaler = sklearn.preprocessing.MinMaxScaler()
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)
       
    if (i == 3):
        vScaler = sklearn.preprocessing.Normalizer()
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)

    if (i == 4):
        vScaler = sklearn.preprocessing.RobustScaler()
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)

    if (i == 5):
        vTrainingData = vScaler.fit_transform(vTrainingData)
        vTestingData=vScaler.transform(vTestingData)

    for j in range(5):
        if (j == 0):
            vClassifier = sklearn.tree.DecisionTreeClassifier().fit(vTrainingData, vTrainingLabels)
            vPredictedLabels = vClassifier.predict(vTestingData)
        if (j == 1):
            vClassifier = sklearn.discriminant_analysis.LinearDiscriminantAnalysis().fit(vTrainingData, vTrainingLabels)
            vPredictedLabels = vClassifier.predict(vTestingData)
        if (j == 2):
            vClassifier = sklearn.svm.SVC(kernel='rbf').fit(vTrainingData, vTrainingLabels)
            vPredictedLabels = vClassifier.predict(vTestingData)
        if (j == 3):
            vClassifier=sklearn.svm.SVC(kernel="linear")
            vClassifier.fit(vTrainingData,vTrainingLabels)
            vPredictedLabels = vClassifier.predict(vTestingData)
        if (j == 4):
            vClassifier=sklearn.cluster.KMeans(n_clusters=10,init='k-means++', max_iter=300, n_init=10, random_state=0)
            vPredictedLabels=vClassifier.fit_predict(vTrainingData)
        value = dict[str(i) + str(j)]
        vNumberOfCorrectResults=0
        for vResultIndex in range(len(vTestingLabel)):
            if(vTestingLabel[vResultIndex]==vPredictedLabels[vResultIndex]):
                vNumberOfCorrectResults=vNumberOfCorrectResults+1
        print(dict[str(i) + str(j)], end="")
        print("Accuracy: ",vNumberOfCorrectResults,"/",len(vTestingLabel))

