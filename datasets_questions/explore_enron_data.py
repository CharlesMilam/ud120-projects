#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("./final_project/final_project_dataset.pkl", "r"))

num_datapoints = len(enron_data)
print 'Number of data points:', num_datapoints

num_features = len(enron_data['SKILLING JEFFREY K'].keys())
print 'Number of features:', num_features
