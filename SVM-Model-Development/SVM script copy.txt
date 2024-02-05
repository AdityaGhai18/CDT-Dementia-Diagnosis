import numpy as np
import pandas as pd
import os 
import matplotlib.pyplot as plt
import cv2
import os
from tqdm import tqdm
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

DATA = "/Users/adityaghai/Desktop/Clock_Drawing/Images_Dataset"
CATEGORIES = ['0', '1', '2', '3', '4', '5']
IMG_SIZE = 50

for category in CATEGORIES:
    path = os.path.join(DATA, category)
    for img in os.listdir(path):
        img_array=cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
        
training_data = []
def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATA, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array=cv2.imread(os.path.join(path,img))
                new_array=cv2.resize(img_array,(IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
            
create_training_data()

#converting the 4D array into a 2D array for SVM
training_datalen = len(training_data)

X = [] #features
y = [] #labels

for categories, label in training_data:
    X.append(categories)
    y.append(label)

X = np.array(X).reshape(training_datalen, -1)
y = np.array(y)

os.chdir("/Users/adityaghai/Desktop/Clock_Drawing/SVM/SVM 4000")
pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

# Opening the files about data
X = pickle.load(open("X.pickle", "rb"))
y = pickle.load(open("y.pickle", "rb"))


X = X/255.0

#slightly different way of splitting data into training and testing
#here we simply import a library function that does an 80-20 training validation split for us
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.1) 
#imported the model and then did construction based on kernal
svc = SVC(kernel='rbf',gamma='auto')
svc.fit(X_train, y_train)

#prediction based on split
test = svc.predict(X_test)

#implementing a accuracy function for the predicition done in y2
print("Accuracy on unknown data is",accuracy_score(y_test,test))





