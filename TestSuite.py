import unittest

from YogaTestFileio import TestFileio
from YogaTestPlot import TestPlot
    
def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestPlot)) 
    suite.addTest(unittest.makeSuite(TestFileio)) 
    runner = unittest.TextTestRunner() 
    print(runner.run(suite))
    print(result)
my_suite()

