
# coding: utf-8

# In[4]:


import unittest, sys, os

parent_dir = os.path.normpath(os.path.join(os.getcwd(),'../..'))
if parent_dir not in sys.path:
    sys.path.insert(0, parent_dir)

from yoga.output import plot
from yoga.patient import patient
from yoga.patient import exercise

class TestPlot(unittest.TestCase): # test class
    print("testing enviroment")
    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self): 
        print('setup...')
        self.p1=patient.Patient("rroy","pass","Mr.","Rajeev","","Roy")
        self.p2=patient.Patient("mzardadi", "pass", "Mr.", "Mohsen", "","Zardadi")
        self.p3=patient.Patient("mroberto", "pass", "Mr.", "Maziar", "","Roberto")
        self.ex1 = exercise.Exercise("Surya Namaskar", 30)
        self.ex2 = exercise.Exercise("Savasana", 10)
        
    def tearDown(self):
        print('tear down ...')
        del self.p1
        del self.p2
        del self.p3
        del self.ex1
        del self.ex2

    def test_revenue(self):
        a=b=c=d=e=True
        self.p1.addRev(100)
        self.p2.addRev(200)
        self.p3.addRev(300)
        a = plot.Plot.revenue(patient.Patient._registery)
        self.assertTrue(a)
        self.p1.addRev(400)
        b = plot.Plot.revenue(patient.Patient._registery)
        self.assertTrue(b)
        self.p2.addRev(-200)
        self.p1.addRev(-400)
        c = plot.Plot.revenue(patient.Patient._registery)
        self.assertTrue(c)
        self.p3.addRev(100)
        d = plot.Plot.revenue(patient.Patient._registery)
        self.assertTrue(d)
        self.p3.addRev(-200)
        e = plot.Plot.revenue(patient.Patient._registery)
        self.assertTrue(e)
        
        
    def test_exercis(self):
        
        a=b=c=d=e=True
        a = plot.Plot.exercise(exercise.Exercise._registery)
        self.assertTrue(a)
        self.ex2.time = 100
        b = plot.Plot.exercise(exercise.Exercise._registery)
        self.assertTrue(b)
        c = plot.Plot.exercise(exercise.Exercise._registery)
        self.assertTrue(c)
        self.ex2.time = 200
        d = plot.Plot.exercise(exercise.Exercise._registery)
        self.assertTrue(d)
        self.ex1.time = 150
        e = plot.Plot.exercise(exercise.Exercise._registery)
        self.assertTrue(e)

#unittest.main(argv=[''], verbosity=2, exit=False)

