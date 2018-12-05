#file fileio.py
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 14:27:07 2018

@author: rajeevroy

export the customer details to a file
"""

#import csv module
import csv
class ExportUsers:
    def __init__(self):
        pass
    def pcsv(pobject,filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                uwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in pobject:
                    uwriter.writerow([i.id, i.password, i.salution, i.getfName(),i.getmName(), i.getlName(), i.getRev()])
        except:
            print("Error while exporting patiient file")
    def ecsv(pobject,filename):
        try:
            with open(filename, 'w', newline='') as csvfile:
                uwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                for i in pobject:
                    uwriter.writerow([i.name, i.time])
        except:
            print("Error while exporting exercise file")
