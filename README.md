# python-lib-yoga


[![Build Status](https://travis-ci.org/rroygithub/data-533-lab4-mohsen-roy.svg?branch=master)](https://travis-ci.org/rroygithub/data-533-lab4-mohsen-roy)


# Yoga package

Yoga package was designed to be used for a yoga treatmet app (https://treatwithyoga.com/)

The package has two subpackages:

1. 'patient'

2. 'output'

The first subpackage includes two modules:

1. 'Patient': to keep information for each patient

Patient module includes two classes named User and Patient.

User and patient classes record all information for each patient including:
id, password, salution, fName, mName , and lName.

These information can be recorded as csv file and ploted through other modules in this package.

2. 'Exercise': to keep informaiton for each exercise

Exercise package records name of the exercise and length of the exercise in minute.

These information can be recorded as csv file and ploted through other modules in this package. 

The second package includes two modules: 

1. 'Plot': to visualize revenue by each customer and time by each exercise

This module uses mathplotlib for visualization. 

2. 'Fileio': to export information for all patient into and external csv file


