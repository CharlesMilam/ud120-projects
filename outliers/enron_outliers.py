#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("./tools/")
from feature_format import featureFormat, targetFeatureSplit
import numpy


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("./final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
max_bonus = 0
max_bonus_person = ''
big_bonuses = []
for key in data_dict:
    if data_dict[key]['bonus'] > max_bonus and data_dict[key]['bonus'] != 'NaN':
        max_bonus = data_dict[key]['bonus']
        max_bonus_person = key

    if data_dict[key]['bonus'] != 'NaN' and data_dict[key]['salary'] != 'NaN'and int(data_dict[key]['bonus']) > 5000000 and int(data_dict[key]['salary']) > 1000000 :
        big_bonuses.append(key)

print 'Big bonuses:', big_bonuses

data_dict.pop(max_bonus_person, 0)
data = featureFormat(data_dict, features)

### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
