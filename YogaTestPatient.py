
import os,sys, unittest

from yoga.patient import patient

class TestPatient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        print('setupClass')
        cls.p1=patient.Patient(1, 'pass1', 'Mr.','Rajeev', 'Ranjan', 'Roy')                    
        #cls.p1.display()
        cls.p2=patient.Patient(2, 'pass2', 'Mr.','Mohsen', '', 'Zardadi')
        #cls.p2.display()
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        del cls.p1
        del cls.p2
    def setUp(self):
        self.p3=patient.Patient(3, 'pass3', 'Mr.','Mohan', 'Singh','Agashe')
        self.p4=patient.Patient(4, 'pass4', 'Mr.','Ramesh', 'Mohan','Agashe')
        self.p5=patient.Patient(5, 'pass5', 'Mr.','Amit', 'Ramlal','Ganeriwalla')
        self.p6=patient.Patient(6, 'pass6', 'Mr.','Shree', 'Narayan','Roy')
        self.p7=patient.Patient(7, 'pass7', 'Mr.','Shailesh', 'Nandan','Singh')
        print('Setup')
    def tearDown(self):
        print('Teardown')
        del self.p3
        del self.p4
        del self.p5
        del self.p6
        del self.p7
    def test_getfName(self):
        self.assertEqual(patient.Patient.getfName(self.p3),'Mohan')
        self.p3.setfName('Suresh')
        self.assertEqual(patient.Patient.getfName(self.p3),'Suresh')
        self.p3.setfName('Karan')
        self.assertEqual(patient.Patient.getfName(self.p3),'Karan')
        self.p3.setfName('Lila Ramesh')
        self.assertEqual(patient.Patient.getfName(self.p3),'Lila Ramesh')
        self.p3.setfName('Arjun')
        self.assertEqual(patient.Patient.getfName(self.p3),'Arjun')
    def test_setfName(self):
        self.p3.setfName('Kareem')
        self.p4.setfName('Ram')
        self.p5.setfName('Mohan')
        self.p6.setfName('Amit')
        self.p7.setfName('Shree')
        self.assertEqual(self.p3._Patient__fName,'Kareem')
        self.assertEqual(self.p4._Patient__fName,'Ram')
        self.assertEqual(self.p5._Patient__fName,'Mohan')
        self.assertEqual(self.p6._Patient__fName,'Amit')
        self.assertEqual(self.p7._Patient__fName,'Shree')
    def test_AddRev(self):
        self.p1.addRev(100)
        self.assertEqual(self.p1.getRev(),100)
        self.assertEqual(self.p1.addRev('ab'), 'Invalid')
    def test_getlName(self):
        self.p3.setlName("Mohan")
        self.assertEqual(patient.Patient.getlName(self.p3),'Mohan')
        self.p3.setlName('Suresh')
        self.assertEqual(patient.Patient.getlName(self.p3),'Suresh')
    def test_setlName(self):
        self.p3.setlName("Mohan")
        self.assertEqual(patient.Patient.getlName(self.p3),'Mohan')
        self.p3.setlName('Suresh')
        self.assertEqual(patient.Patient.getlName(self.p3),'Suresh')
    def test_getmName(self):
        self.p3.setmName("Mohan")
        self.assertEqual(patient.Patient.getmName(self.p3),'Mohan')
        self.p3.setmName('Suresh')
        self.assertEqual(patient.Patient.getmName(self.p3),'Suresh')
    def test_setmName(self):
        self.p3.setmName("Mohan")
        self.assertEqual(patient.Patient.getmName(self.p3),'Mohan')
        self.p3.setmName('Mohsen')
        self.assertEqual(patient.Patient.getmName(self.p3),'Mohsen')
    def test_display(self):
        rtn1=self.p3.display()
        self.assertEqual(rtn1,0)
        rtn1=self.p1.display()
        self.assertEqual(rtn1,0)
    def test_User(self):
        p1 = patient.Patient('12e', 'pass1', 'Mr.','Rajeev', 'Ranjan', 'Roy')
        self.assertNotIsInstance(p1.id, int)
        
        
#unittest.main(argv=[''], verbosity=2, exit=False)
              

