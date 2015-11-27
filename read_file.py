# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:54:56 2015

@author: jonbruno
"""
import os
import csv
from datetime import datetime


#==============================================================================
# Importing the data
#==============================================================================
# change to the directory where the csv is stored (assuming it is not part of
# the path)
file_dir = '/Users/jonbruno/Documents/Python/dividend'
os.chdir(file_dir)

# note this is just a test
filename = 'BBEP Dividends Only.csv'
filename = 'BBEP Historical Stock Prices.csv'
with open(filename, 'rb') as source:
    file_in = csv.reader(source, dialect=csv.excel_tab)
    for line in file_in:
        print line

# since excels csv formatting is throwing an error
# we will just use the tab delimited version from a nice old text file
filename = 'Breitburn.txt'
with open(filename, 'rb') as source:
    file_in = csv.reader(source, delimiter="\t")
    for line in file_in:
        print line

#==============================================================================
# Working with Dates
#==============================================================================
# we might want to think about grabbing the dates and converting their format
# a nice time tutorial is here:
# https://pymotw.com/2/datetime/

# lets use an example line from Breitburn.txt
x = ['2/1/2007', 'Cash', '0.399', '1/22/2007', '2/5/2007', '2/14/2007']

date_object = datetime.strptime(x[0], '%m/%d/%Y')

type(date_object) # datetime produces an object
print(date_object) # this prints the raw datetime.datetime object
print(datetime.date(date_object)) # this prints only the date (not time) part of the object
print(date_object.strftime('%B %d, %Y')) # this is some formatting on the object

# we may want date instead of datetime since we dont need the hour min sec args

# we can look at the 
t1 = datetime.strptime(x[0], '%m/%d/%Y')
t2 = datetime.strptime(x[3], '%m/%d/%Y')
print t1-t2 # this produces a timedelta in days which can be added to other dates

#==============================================================================
# Now... What od we want to look at - how do we need to structure our data?
#==============================================================================
# this is a question for David
