#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("./tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("./final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

clf = DecisionTreeClassifier()

clf.fit(features_train, labels_train)

score = clf.score(features_test, labels_test)

print 'Score: {:.3f}'.format(score)

# determine numer of POIs in test set
num_test_poi = 0
for poi in labels_test:
    if poi:
        num_test_poi += 1
print 'Number of test set POIs: {}'.format(num_test_poi)

# determine total number of people in test set
print 'Number of people in test set: {}'.format(len(labels_test))

# determine the accuracy if no POIs found
labels_test_no_poi = [0.0] * len(labels_test)
no_poi_score = clf.score(features_test, labels_test_no_poi)
print 'Accuracy with no POIs: {:.3f}'.format(no_poi_score)

# number of true positives
pred = clf.predict(features_test)
print 'Test labels'
print labels_test
print
print 'Predicted labels'
print pred
