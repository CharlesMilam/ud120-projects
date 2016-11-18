#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
# plt.xlim(0.0, 1.0)
# plt.ylim(0.0, 1.0)
# plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
# plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
# plt.legend()
# plt.xlabel("bumpiness")
# plt.ylabel("grade")
# plt.show()
################################################################################
### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn import tree

dt = tree.DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 5, max_depth = 25, min_samples_leaf = 2)

ab_clf = AdaBoostClassifier(dt, n_estimators = 100, learning_rate = 0.99, algorithm = 'SAMME')

ab_clf.fit(features_train, labels_train)

ab_pred = ab_clf.predict(features_test)

ab_acc = ab_clf.score(features_test, labels_test)

print 'Adaboost Accuracy:', ab_acc

rf_clf = RandomForestClassifier(n_estimators = 500, criterion = 'gini',
                                max_depth = 2, min_samples_split = 2,
                                min_weight_fraction_leaf = 0.05,
                                max_leaf_nodes = 100,
                                min_impurity_split = 0.005,
                                class_weight = None,
                                n_jobs = -1)

rf_clf.fit(features_train, labels_train)

rf_pred = rf_clf.predict(features_test)

rf_acc = rf_clf.score(features_test, labels_test)

print 'Random Forest Accuracy:', rf_acc







try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
