# Binary Classification with Sonar Dataset: Standardized
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from keras.utils import np_utils
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
import numpy as np
import pandas as pd
from sklearn import preprocessing
import matplotlib.pyplot as plt
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import numpy
from keras.models import Model
from keras.layers import Input, Dense

seed = 7
np.random.seed(7)
numpy.random.seed(seed)
#numpy.random.seed(seed)
# load dataset
dataframe = read_csv("KDDTrain+.csv", header=None)
dataset = dataframe.values
A = dataset[:,0:41]
Y = dataset[:,41]

for i in range (1,4) :
    encoder = LabelEncoder()
    encoder.fit(dataset[:,i])
    
    A[:,i]=encoder.transform(dataset[:,i])

#std = StandardScaler()
#std.B = std.fit_transform(A) 
#scaler = MinMaxScaler(feature_range=(0, 1))
#B = scaler.fit_transform(A)

for i in range(len(dataset[:,41])):
    if Y[i] == 'normal':
        Y[i] = 'Normal'
    if Y[i] == 'back' or Y[i] == 'neptune' or Y[i] == 'pod' or Y[i] == 'smurf' or Y[i] == 'teardrop' or Y[i] == 'land':
        Y[i] = 'DoS'
    if Y[i] == 'ipsweep' or Y[i] == 'nmap' or Y[i] == 'portsweep' or Y[i] == 'satan':
        Y[i] = 'Probe'
    if Y[i] == 'warezclient' or Y[i] == 'ftp_write' or Y[i] == 'guess_passwd' or Y[i] == 'multihop' or Y[i] == 'phf'  or Y[i] == 'spy' or Y[i] == 'warezmaster':
        Y[i] = 'R2L'
    if Y[i] == 'buffer_overflow' or Y[i] == 'loadmodule' or Y[i] == 'perl' or Y[i] == 'rootkit':
        Y[i] = 'U2R'
    if Y[i] == 'unknown':
        Y[i] = 'Unknown'

# encode class values as integers
encoderY = LabelEncoder()
encoderY.fit(dataset[:,41])
dataset[:,41] = encoderY.transform(dataset[:,41])
dummy_y = np_utils.to_categorical(Y)
#onehotencoded   1000000

print(A)
print(dummy_y)






dataframe_Test = read_csv("KDDTest+.csv", header=None)
dataset_Test = dataframe_Test.values
A_Test = dataset_Test[:,0:41]
Y_Test = dataset_Test[:,41]

# encoded data

for i in range (1,4) :
    encoder = LabelEncoder()
    encoder.fit(dataset_Test[:,i])
    
    A_Test[:,i]=encoder.transform(dataset_Test[:,i])

for i in range(len(dataset_Test[:,41])):
    if Y_Test[i] == 'normal':
        Y_Test[i] = 'Normal'
    elif Y_Test[i] == 'back' or Y_Test[i] == 'neptune' or Y_Test[i] == 'pod' or Y_Test[i] == 'smurf' or Y_Test[i] == 'teardrop' or Y_Test[i] == 'land':
        Y_Test[i] = 'DoS'
    elif Y_Test[i] == 'ipsweep' or Y_Test[i] == 'nmap' or Y_Test[i] == 'portsweep' or Y_Test[i] == 'satan':
        Y_Test[i] = 'Probe'
    elif Y_Test[i] == 'warezclient' or Y_Test[i] == 'ftp_write' or Y_Test[i] == 'guess_passwd' or Y_Test[i] == 'multihop' or Y_Test[i] == 'phf'  or Y_Test[i] == 'spy' or Y[i] == 'warezmaster':
        Y_Test[i] = 'R2L'
    elif Y_Test[i] == 'buffer_overflow' or Y_Test[i] == 'loadmodule' or Y_Test[i] == 'perl' or Y_Test[i] == 'rootkit':
        Y_Test[i] = 'U2R'
    else:
        Y_Test[i] = 'Unknown'    

encoderY_Test = LabelEncoder()
encoderY_Test.fit(dataset_Test[:,41])
dataset_Test[:,41] = encoderY_Test.transform(dataset_Test[:,41])
dummy_Ny = np_utils.to_categorical(Y_Test)
#print('Y_Test=\n',Y_Test)
print(A_Test)
print(dummy_Ny)


scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_A_train = scaler.fit_transform(A)
scaler = MinMaxScaler(feature_range=(0, 1))
rescaled_A_Test_train = scaler.fit_transform(A_Test)


model = Sequential()
model.add(Dense(41, input_dim=41, kernel_initializer='normal', activation='relu'))
model.add(Dense(6, kernel_initializer='normal', activation='softmax'))
# Compile model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
history = model.fit(rescaled_A_train, dummy_y, epochs=100, batch_size=50)

scores = model.evaluate(rescaled_A_Test_train, dummy_Ny, batch_size=50, verbose=1)
# Returns the loss value & metrics values for the model in test mode.
print(scores)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

print(history.history.keys())
plt.figure(1) 
# summarize history for accuracy
plt.subplot(2,1,1)  
plt.plot(history.history['acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left') 

# summarize history for loss
plt.subplot(2,1,2)  
plt.plot(history.history['loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()








##def KDD_model():
    	# create model
#	model = Sequential()
#	model.add(Dense(100, input_dim=41, kernel_initializer='normal', activation='relu'))
#	model.add(Dense(6, kernel_initializer='normal', activation='softmax'))
#	# Compile model
#	model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
#	return model
#estimator = KerasClassifier(build_fn=KDD_model, epochs=1, batch_size=1000000, verbose=1)
#kfold = KFold(n_splits=10, shuffle=True, random_state=seed)
#results = cross_val_score(estimator, A, dummy_y, cv=kfold)
#print("Accuracy: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

#score = KDD_model.evaluate(A_Test, dummy_Ny,epochs=1, batch_size=1000000, verbose=1)
#print('test lose:%.2f%%  test acc:%.2f%% ',score[0],score[1])



