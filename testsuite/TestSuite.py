
# coding: utf-8

# In[1]:


import unittest

from tests.YogaTestPatient import TestPatient 
from tests.YogaTestExercise import TestExercise 
from tests.YogaTestFileio import TestFileio
from tests.YogaTestPlot import TestPlot
    
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPlot)) 
    suite.addTest(unittest.makeSuite(TestPatient))
    suite.addTest(unittest.makeSuite(TestExercise)) 
    suite.addTest(unittest.makeSuite(TestFileio)) 
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    print(result)
my_suite()

