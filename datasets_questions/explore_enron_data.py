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

num_poi = len([data for data in enron_data if enron_data[data]['poi']])
print 'Number of POI', num_poi

with open('./final_project/poi_names.txt', 'r') as f:
    num_poi_exist = len([line for line in f if line[0] == '('])

print 'Number of existing poi:', num_poi_exist

# print enron_data['PRENTICE JAMES']
jp_stock_val = enron_data['PRENTICE JAMES']['total_stock_value']
print 'Total stock for Jame Prentice:', jp_stock_val

wc_email_to_poi = enron_data['COLWELL WESLEY']['from_this_person_to_poi']
print 'Number of emails to poi from Wesley Colwell:', wc_email_to_poi

js_stock_options = enron_data['SKILLING JEFFREY K']['exercised_stock_options']
print 'Exercised stock options by Skilling:', js_stock_options

scum_salaries = {}
skilling = 'SKILLING JEFFREY K'
lay = 'LAY KENNETH L'
fastow = 'FASTOW ANDREW S'

scum_salaries[skilling] = enron_data[skilling]['total_payments']
scum_salaries[lay] = enron_data[lay]['total_payments']
scum_salaries[fastow] = enron_data[fastow]['total_payments']

print 'Biggest scum:', max(scum_salaries.iterkeys(), key = lambda key: scum_salaries[key]), scum_salaries[str(max(scum_salaries.iterkeys(), key = lambda key: scum_salaries[key]))]

num_salaries = 0
num_emails = 0

for person in enron_data:
    if enron_data[person]['salary'] != 'NaN':
        num_salaries += 1

    if enron_data[person]['email_address'] != 'NaN':
        num_emails += 1

print 'Number salaried: {}, Number emails: {}'.format(num_salaries, num_emails)

num_no_tot_payments = 0.0

for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN':
        num_no_tot_payments += 1

print 'Percentage of no total payments: {:.2f}'.format((num_no_tot_payments / num_datapoints) * 100)

num_poi_no_tot_payments = 0.0

for person in enron_data:
    if enron_data[person]['total_payments'] == 'NaN' and enron_data[person]['poi']:
        num_poi_no_tot_payments += 1

print 'Percentage of poi no total payments: {:.2f}'.format((num_poi_no_tot_payments / num_datapoints) * 100)

print 'Number of no total payments:', num_no_tot_payments

print 'Number of poi no total payments:', num_poi_no_tot_payments
