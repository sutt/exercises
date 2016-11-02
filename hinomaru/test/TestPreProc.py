import os,sys, unittest
from os import path

#sys.path.append('..')
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#sys.path.append(os.path.join('..', 'utils'))

if __name__ != "__main__":
    """ We'll run ./runtest.py which imports these classes within
        the ./test/ directory and then runs the test. So imports
        are relative to root, not this file. """
    from utils.utils import Solution
    from hino_test_stage import PreProc

class ScratchDummyClass:
    def __init__(self):
        self.data = [0]
        print ' '
        print '>init Dummy...'
    def method(self):
        print '...laborious processing step. now setup:'

class ScratchTest(unittest.TestCase):

    def setUp(self):
        """ This shows how to import a class in an outside module 
            from within a test class. But as can be seen, instantiating the class calls it fully before each test. """
        
        self.outside_class = Solution()
        
        self.dummy_setup = ScratchDummyClass()
        self.dummy_setup.method()
        
        self.precalled_dummy = []
        
        
    def test_outside_class(self):
        self.assertTrue(len(self.outside_class.s) == 0)
        self.assertEqual(self.outside_class._X, 0)

    def test_fail_if_incorrect_order(self):
        self.assertNotEqual([1,2,3],[3,2,1])
        
    def test_pass_if_incorrect_order(self):
        self.assertItemsEqual([1,2,3],[3,2,1])
        

class PreprocTests(unittest.TestCase):

    def setUp(self):
        self.myclass = PreProc()
        
        self.myclass.perform_preproc()
    
    def test_valids_length(self):
        self.assertEqual( len(self.myclass.valids), 126)
        
    def test_valids_less_than_combos(self):
        self.assertTrue( len(self.myclass.valids) < len(self.myclass.combos) )

    def test_so_length(self):
        so = self.myclass.strikeouts
        valids = self.myclass.valids

        self.assertEqual( len(so), len(valids) )
        
        
    def test_fail_order_specific_so(self):
        
        data = [28, 28, 28, 28, 28, 28, 28, 28, 27, 26, 27, 26, 28, 28, 28, 28, 28, 28, 28, 28, 33, 33, 30, 30, 30, 30, 30, 30, 30, 30, 23, 21, 21, 23, 19, 16, 16, 19, 17, 18, 17, 18, 28, 25, 25, 28, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 27, 25, 25, 27, 20, 20, 27, 26, 27, 26, 19, 17, 17, 19, 26, 27, 26, 27, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 16, 15, 15, 16, 19, 19, 32, 32, 30, 30, 34, 34, 28, 28, 28, 28, 34, 34, 30, 30, 27, 27, 18, 18, 26, 26, 30, 30, 35, 35, 28, 28, 28, 28, 35, 35, 30, 30]
        
        from random import shuffle
        shuffle(data)
        
        so = self.myclass.strikeouts
        outs = map(len,so)
        
        self.assertNotEqual(outs, data)
        
    def test_non_order_specific_so(self):
        
        data = [28, 28, 28, 28, 28, 28, 28, 28, 27, 26, 27, 26, 28, 28, 28, 28, 28, 28, 28, 28, 33, 33, 30, 30, 30, 30, 30, 30, 30, 30, 23, 21, 21, 23, 19, 16, 16, 19, 17, 18, 17, 18, 28, 25, 25, 28, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 27, 25, 25, 27, 20, 20, 27, 26, 27, 26, 19, 17, 17, 19, 26, 27, 26, 27, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 16, 15, 15, 16, 19, 19, 32, 32, 30, 30, 34, 34, 28, 28, 28, 28, 34, 34, 30, 30, 27, 27, 18, 18, 26, 26, 30, 30, 35, 35, 28, 28, 28, 28, 35, 35, 30, 30]
        
        from random import shuffle
        shuffle(data)
        
        so = self.myclass.strikeouts
        outs = map(len,so)

        self.assertListEqual(outs, data)
        
    def test_pass_order_specific_so(self):
        
        data = [28, 28, 28, 28, 28, 28, 28, 28, 27, 26, 27, 26, 28, 28, 28, 28, 28, 28, 28, 28, 33, 33, 30, 30, 30, 30, 30, 30, 30, 30, 23, 21, 21, 23, 19, 16, 16, 19, 17, 18, 17, 18, 28, 25, 25, 28, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 27, 25, 25, 27, 20, 20, 27, 26, 27, 26, 19, 17, 17, 19, 26, 27, 26, 27, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 16, 15, 15, 16, 19, 19, 32, 32, 30, 30, 34, 34, 28, 28, 28, 28, 34, 34, 30, 30, 27, 27, 18, 18, 26, 26, 30, 30, 35, 35, 28, 28, 28, 28, 35, 35, 30, 30]
            
        so = self.myclass.strikeouts
        outs = map(len,so)

        self.assertEqual(outs, data)
        
    

        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(PreprocTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(Cc)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    

def main():
    #s  = SearchData()
    #print s.x
    
    pp = PreProc()
    print 'ppcombos', str(pp.combos)
    
    if False:
        unittest.main()
        #pass
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(ScratchTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
        
        suite = unittest.TestLoader().loadTestsFromTestCase(PreprocTests)
        unittest.TextTestRunner(verbosity=2).run(suite)
    return 1

