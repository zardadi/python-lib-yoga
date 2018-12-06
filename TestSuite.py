import unittest

from YogaTestFileio import TestFileio
from YogaTestPlot import TestPlot
from YogaTestPatient import TestPatient 
from YogaTestExercise import TestExercise 
    
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPlot)) 
    suite.addTest(unittest.makeSuite(TestFileio)) 
    suite.addTest(unittest.makeSuite(TestPatient))
    suite.addTest(unittest.makeSuite(TestExercise)) 

    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    print(result)
