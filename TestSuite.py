
# coding: utf-8

# In[1]:


import unittest
from YogaTestPatient import TestPatient 
from YogaTestExercise import TestExercise 

def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPatient))
    suite.addTest(unittest.makeSuite(TestExercise)) 

    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
my_suite()

