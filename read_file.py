# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 23:54:56 2015

@author: jonbruno
"""
import os
import csv

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
        
# we might want to think about grabbing the dates and converting their format