# Package: yoga
## Sub-Packages: patient and output

## Sub-Package `patient`
This sub-package has two modules. One for creating patients and the other for creating exercises
### Module `patient.py`
This module contains two classes. `user` is the superclass for storing the userid and passwords of all users. `patient` is inherited
from the `user` class and adds further attributes to the class as per the requirements. The `patient` class has various methods as required,
which are enumerated below.

`class user` has the following attributes:

`id`: to store the user id

`password`: to store the password for the user

`class user` has one method:

`__init__`: to initiate the object for this class

`class patient` has the following attributes:

`_registery`: this is an attribute of the class to store all the objects created so that it is easy to iterate through the objects

`id`: to store the user id of a patient object (mandatory)

'password`: to store the password of a patient object (mandatory)

`salution`: to store the salution of a patient object (mandatory)

`fName`: to store the First name of a patient object (mandatory)

`mName' to store the Last name of a patient object

`lName` to store the Last name of a patient object

`class patient` has the following methods:

`__init__`: to initialise a new object, which includes initiatilising the attributes `id` and `password` for the super class `user` and also append the new object to the list `_registery` for the class

`getfName`: Return the First name of the object

`getmName`: Return the Middle name of the object

`getlName`: Return the Last name of the object

`getRev`: Return the Revenue for the object

`setfName`: Set the First name of the object

`setmName`: Set the Middle name of the object

`setlName`: Set the Last name of the object

`addRev`: Add Revenue for the object

`display`: Display the details of the patient and the revenue

### Module `exercise.py`
This module contains one class `exercise`. There are two attributes and two methods which are enumerated below.

`class exercise` has the following attributes:

`name`: to store the name of the execise

`time`: to store the time of the exercise

`class exercise` has two methods:

`__init__`: to initiate the object for this class

`display`: to display the details of the object

## Sub-Package `output`
This sub-package has two modules. One for exporting the output to csv files and the other to plot the output
### Module `fileio.py`
This module contains the class `ExportUsers` to export the users and exercises to a csv file. This class does not have any attributes and has three methods as enumerated below.

`__init__`: to initiate the object for this class

`pcsv`: this method needs to be called with a `patient._registery` object as `pobject` and the required filename as `filename`. It then uses the `csv` library to write all the patient records to the filename specified by iterating through the `patient._registery` passed to it.

`ecsv`: this method needs to be called with a `exercise._registery` object as `pobject` and the required filename as `filename`. It then uses the `csv` library to write all the patient records to the filename specified by iterating through the `exercise._registery` passed to it.

### Module `plot.py`
This module contains the class `Plot` to plot the revenue by patient and the time by exercise. This class does not have any attributes and has three methods as enumerated below.

`__init__`: to initiate the object for this class

`revenue`: this method needs to be called with a `patient._registery` object as `pobject`. It then uses the `matplotlib` library to plot the revenue for each patient by iterating through the `patient._registery` passed to it.

`exercise`: this method needs to be called with a `exercise._registery` object as `pobject`. It then uses the `matplotlib` library to plot the time for each exercise by iterating through the `exercise._registery` passed to it.
