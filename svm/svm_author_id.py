#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("./tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
import numpy as np
from sklearn.svm import SVC

# reduce training set size
# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clf = SVC(kernel = 'rbf', C = 10000.0)

t0 = time()
clf.fit(features_train, labels_train)
print
print "training time:", round(time()-t0, 3), "s"
print

t1 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t1, 3), "s"
print

acc = clf.score(features_test, labels_test)
unique, counts = np.unique(pred, return_counts = True)
event_counts = dict(zip(unique, counts))

print 'Accuracy score:', acc
print
print 'Class for 10:', pred[10]
print 'Class for 26:', pred[26]
print 'Class for 50:', pred[50]
print
print 'Event counts:', event_counts
#########################################################
