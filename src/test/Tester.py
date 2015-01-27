'''
Created on Jan 27, 2015

@author: besil
'''
import unittest
from main.matcher import StringMatcher

class Test(unittest.TestCase):
    
    def setUp(self):
        self.sm = StringMatcher()
    def tearDown(self):
        pass

    def testName(self):
        self.assertEquals(self.sm.match("ciao", "ciao"), 0, "Abbiamo usato una misura sbagliata")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()