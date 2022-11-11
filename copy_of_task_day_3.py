# -*- coding: utf-8 -*-
"""Copy of task day 3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J-Cf8bvHvjMYSgdSNDEtSDSneKkfTKH_
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow
import glob

from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D,Flatten,Dense,MaxPool2D
from tensorflow.keras.losses import SparseCategoricalCrossentropy
from tensorflow.keras.optimizers import Adam
import sklearn
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

import pathlib

pic_path=pathlib.Path("/content/drive/MyDrive/mask")

mask_list=list(pic_path.glob("with mask/*"))
without_list=list(pic_path.glob("without mask/*"))

len(mask_list)

len(without_list)

pic_dict={"with mask":mask_list,"without mask":without_list}

pic_class={'with mask':0,"without mask":1}

x=[]
y=[]

for i in pic_dict:
  pic_name=i
  pic_path_list=pic_dict[pic_name]
  for path in pic_path_list:
    img=cv2.imread(str(path))
    img = cv2.resize(img,(100,100))
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img = img/255
    x.append(img)
    y.append(pic_class[i])

len(x) ,len(y)

import numpy as np
x=np.array(x)
y=np.array(y)

x.shape

y.shape

xtrain,xtest,ytrain,ytest = train_test_split(x,y, test_size = .30, random_state =1)

len(xtrain),len(xtest),len(ytrain),len(ytest)

model = Sequential()

model.add(Conv2D(filters=100, kernel_size=(3,3),input_shape=(100,100,3),padding='valid',strides=1,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters=80, kernel_size=(3,3),padding='valid',strides=1,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Conv2D(filters=30, kernel_size=(3,3),padding='valid',strides=1,activation='relu'))
model.add(MaxPool2D(pool_size=(2,2)))

model.add(Flatten())

model.add(Dense(100,activation='relu'))
model.add(Dense(100,activation='relu'))
model.add(Dense(50,activation='relu'))

model.add(Dense(2,activation='softmax'))

model.summary()

model.compile(optimizer=Adam(),loss=SparseCategoricalCrossentropy(),metrics=['accuracy'])

hist = model.fit(xtrain,ytrain,batch_size=500,epochs=5,validation_data=(xtest,ytest))

history=hist.history

plt.title('Learning Curve')
plt.xlabel('epochs')
plt.ylabel('Accuracy')
plt.plot(history['accuracy'],label=('Accuracy'))
plt.plot(history['val_accuracy'],label=('Validation Accuracy'))
plt.grid(True)
plt.style.use('seaborn-paper')
# plt.show()
plt.legend()

plt.title('Learning Curve')
plt.xlabel('epochs')
plt.ylabel('Accuracy')
plt.plot(history['loss'],label=('loss'))
plt.plot(history['val_loss'],label=('Validation Loss'))
plt.grid(True)
plt.style.use('seaborn-paper')
# plt.show()
plt.legend()

ypred =model.predict(xtest)

type(ypred)

type(ytest)

cf = confusion_matrix(ytest,ypred)

import cv2
import tensorflow
import numpy as np
# model = tensorflow.keras.models.load_model('Mammooty.h5')

img= cv2.imread("with_mask_101.jpg")
# img = cv2.rotate(img,rotateCode=0)
hcc = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# img = cv2.resize(img, (800, 500))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
res = hcc.detectMultiScale(gray)

for(x,y,w,h) in res:
    cv2.rectangle(img, (x,y),(x+w, y+h),(255,255,255),2)
    
img = cv2.resize(img,(600,500))
img = np.array(img, dtype = 'uint8')
img = cv2.resize(img, (100,100)) 

actors = {'withmask':0,"without mask":1}

pred_img = img.reshape(1,100,100,3)

face = model.predict_classes(pred_img)

img = cv2.resize(img,(600,500))
for i in actors:
    if face == actors[i]:
        name =i
        cv2.putText(img, name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, .7, (0,255,0), 2)
        

cv2.imshow('a',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
