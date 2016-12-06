#!/usr/bin/python
from operator import itemgetter

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    for idx, prediction in enumerate(predictions):
        cleaned_data.append((ages[idx], net_worths[idx], abs(prediction - net_worths[idx])))

    cleaned_data.sort(key = itemgetter(2))

    return cleaned_data[:81]
