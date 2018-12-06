import unittest

from yoga.output import plot
from yoga.patient.patient import Patient
from yoga.patient.exercise import Exercise

class TestPlot(unittest.TestCase): # test class
    print("YogaTestPlot")
    @classmethod
    def setUpClass(cls):
        print('Test Plot setupClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        
    def setUp(self): 
        print('setup...')
        Patient._registery=[]
        Exercise._registery=[]
        self.p1=Patient("rroy","pass","Mr.","Rajeev","","Roy")
        self.p2=Patient("mzardadi", "pass", "Mr.", "Mohsen", "","Zardadi")
        self.p3=Patient("mroberto", "pass", "Mr.", "Maziar", "","Roberto")
        self.ex1 = Exercise("Surya Namaskar", 30)
        self.ex2 = Exercise("Savasana", 10)
        print("Setup completed")
        
    def tearDown(self):
        print('tear down ...')
        del self.p1
        del self.p2
        del self.p3
        del self.ex1
        del self.ex2

    def test_revenue(self):
        print("In test Revenue")
        self.p1.addRev(100)
        self.p2.addRev(200)
        self.p3.addRev(300)
        a = plot.Plot.revenue(Patient._registery)
        self.assertTrue(a)
        self.p1.addRev(400)
        b = plot.Plot.revenue(1)
        self.assertFalse(b)
        self.p2.addRev(-200)
        self.p1.addRev(-400)
        c = plot.Plot.revenue("Test")
        self.assertFalse(c)
        self.p3.addRev(100)
        d = plot.Plot.revenue(Patient._registery)
        self.assertTrue(d)
        self.p3.addRev(-200)
        e = plot.Plot.revenue(Patient._registery)
        self.assertTrue(e)
        a=plot.Plot()
        
    def test_exercis(self):
        print("In test Exercise")
        a = plot.Plot.exercise(Exercise._registery)
        self.assertTrue(a)
        self.ex2.time = 100
        b = plot.Plot.exercise(1)
        self.assertFalse(b)
        c = plot.Plot.exercise("Test")
        self.assertFalse(c)
        self.ex2.time = 200
        d = plot.Plot.exercise(Exercise._registery)
        self.assertTrue(d)
        self.ex1.time = 150
        e = plot.Plot.exercise(Exercise._registery)
        self.assertTrue(e)

unittest.main()

