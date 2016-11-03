import os,sys, unittest
from os import path

if __name__ != "__main__":
        # We'll run ./runtest.py which imports these classes within
        # the ./test/ directory and then runs the test. So imports
        # are relative to root, not this file. 
    from utils.utils import Solution
    from hino_test_stage import PreProc
else:
    # imports relative to /test/ here?
    #sys.path.append('..')
    #sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    #sys.path.append(os.path.join('..', 'utils'))
    pass

class ScratchDummyClass:
    def __init__(self):
        self.data = [0]
        self.data2 = range(10)
        print ' '
        print '>init Dummy...'
    def method(self):
        print '...laborious processing step. now setup: '
    def method2(self):
        from random import randint
        #self.data2 = randint(1,1000)
        print 'this is only called in head of ScratchTest class'
        
GLOBAL_DATA = range(10)
GLOBAL_DUMMY_INSTANCE = ScratchDummyClass()
GLOBAL_DUMMY_INSTANCE.method()
GLOBAL_DUMMY_INSTANCE.method2()

class ScratchTest(unittest.TestCase):
    
    SCRATCH_DATA = range(10)
    
    #Notice this forces an instance call before, and even 
    #if there is no instantiation of this class or call from TestLoader
    SCRATCH_DUMMY_INSTANCE = ScratchDummyClass()
    SCRATCH_DUMMY_INSTANCE.method()
    SCRATCH_DUMMY_INSTANCE.method2()
    
    def setUp(self):
        """ This shows how to import a class in an outside module 
            from within a test class. But as can be seen, instantiating the class calls it fully before each test. """
        
        self.outside_class = Solution()

        InstaniateEachTime = False
        if InstaniateEachTime:
            self.dummy_setup = ScratchDummyClass()
            self.dummy_setup.method()
        
        self.precalled_dummy = GLOBAL_DUMMY_INSTANCE
        # so the strategy is call method outside of test-class
        # but save the results into the class
        # then bring the class and its data into the test class here
        
        
    def test_1_outside_class(self):
        #tests must start with the word "test"
        #tests are run in alphabetic order 
        self.assertTrue(len(self.outside_class.s) == 0)
        self.assertEqual(self.outside_class._X, 0)

    def test_2_fail_if_incorrect_order(self):
        self.assertNotEqual([1,2,3],[3,2,1])
        
    def test_3_pass_if_incorrect_order(self):
        self.assertItemsEqual([1,2,3],[3,2,1])
        
    def test_4_using_local_data(self):
        
        from random import shuffle
        
        #its equal to itself
        local_data = self.precalled_dummy.data2[:]
        self.assertEqual(self.precalled_dummy.data2, local_data)

        #shuffling a copy 
        shuffle(local_data)
        self.assertNotEqual( range(10), local_data)
        self.assertItemsEqual( range(10), local_data)
        
        #reference to data is shuffled resulting in shuffling of 
        #class level
        local_data = self.precalled_dummy.data2
        shuffle(local_data)
        self.assertNotEqual(self.precalled_dummy.data2, range(10))
        
    def test_5_data_is_not_reset(self):
        
        # in test_4 we shuffled a ref to data2 which has not been undone
        self.assertNotEqual(self.precalled_dummy.data2, range(10))
        

class PreprocTests(unittest.TestCase):

    
    preproc1 = PreProc()
    preproc1.perform_preproc()

    def setUp(self,preprocobj=preproc1):
        
        #self.myclass = PreProc()
        #self.myclass.perform_preproc()
        self.myclass = preprocobj
        
        
        self.so_data = [28, 28, 28, 28, 28, 28, 28, 28, 27, 26, 27, 26, 28, 28, 28, 28, 28, 28, 28, 28, 33, 33, 30, 30, 30, 30, 30, 30, 30, 30, 23, 21, 21, 23, 19, 16, 16, 19, 17, 18, 17, 18, 28, 25, 25, 28, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 27, 25, 25, 27, 20, 20, 27, 26, 27, 26, 19, 17, 17, 19, 26, 27, 26, 27, 32, 32, 37, 37, 31, 31, 31, 31, 37, 37, 32, 32, 16, 15, 15, 16, 19, 19, 32, 32, 30, 30, 34, 34, 28, 28, 28, 28, 34, 34, 30, 30, 27, 27, 18, 18, 26, 26, 30, 30, 35, 35, 28, 28, 28, 28, 35, 35, 30, 30]
    
    
    def test_1_valids_length(self):
        self.assertEqual( len(self.myclass.valids), 126)
        
    def test_2_valids_less_than_combos(self):
        self.assertTrue( len(self.myclass.valids) < len(self.myclass.combos) )

    def test_3_so_length(self):
        so = self.myclass.strikeouts
        valids = self.myclass.valids

        self.assertEqual( len(so), len(valids) )
        
        
    def test_4_fail_order_specific_so(self):
        
        #by-value because one-preproc-method called for all tests
        #and so want eliminate the ability to mutate this data
        data = self.so_data[:]  
        
        from random import shuffle
        shuffle(data)
        
        so = self.myclass.strikeouts
        outs = map(len,so)
        
        self.assertNotEqual(outs, data)
        
    def test_5_non_order_specific_so(self):
        
        data = self.so_data[:]
        
        from random import shuffle
        shuffle(data)
        
        so = self.myclass.strikeouts
        outs = map(len,so)

        self.assertItemsEqual(outs, data)
        
    def test_6_pass_order_specific_so(self):
        
        data = self.so_data[:]
            
        so = self.myclass.strikeouts
        outs = map(len,so)

        self.assertEqual(outs, data)
        
    

        
if __name__ == "__main__":
    #suite = unittest.TestLoader().loadTestsFromTestCase(PreprocTests)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(Cc)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    pass
    

def main():
    #s  = SearchData()
    #print s.x
    
    #pp = PreProc()
    #print 'ppcombos', str(pp.combos)
    
    if False:
        unittest.main()
        #pass
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(ScratchTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
        
        suite = unittest.TestLoader().loadTestsFromTestCase(PreprocTests)
        unittest.TextTestRunner(verbosity=2).run(suite)
        
    return 1

