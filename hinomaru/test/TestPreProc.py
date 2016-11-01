import os,sys, unittest
from os import path

#sys.path.append('..')
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#sys.path.append(os.path.join('..', 'utils'))

if __name__ != "__main__":
    """ We'll run ./runtest.py which imports these classes within
        the ./test/ directory and then runs the test. So imports
        are relative to root, not this file. """
    from utils.utils import SearchData
    from hino_test_stage import PreProc


class TestClass(unittest.TestCase):

    def setUp(self):
        self.SDobj = SearchData()
        
    def test_sdx(self):
        self.assertTrue(len(self.SDobj.x) == 0)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
        
    def test_upper3(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
        
    def testfunp2(self):
        self.assertEqual(1,1,'hey')
        

class PreprocTests(unittest.TestCase):

    def setUp(self):
        self.myclass = PreProc()
        
        self.myclass.perform_preproc()
    
    def test_valids_length(self):
        self.assertEqual( len(self.myclass.valids), 126)
        
    def test_valids_less_than_combos(self):
        self.assertTrue( len(self.myclass.valids) < len(self.myclass.combos) )


        """print so[:1]
        print so[1:2]
        outs = map(len,so)
        print '----'
        print outs
        print '----'
        print max(outs),min(outs)"""
        

        
if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(Cc)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    

def main():
    s  = SearchData()
    print s.x
    
    pp = PreProc()
    print 'ppcombos', str(pp.combos)
    
    if False:
        #unittest.main()
        pass
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=2).run(suite)
        
        suite = unittest.TestLoader().loadTestsFromTestCase(PreprocTests)
        unittest.TextTestRunner(verbosity=2).run(suite)
    return 1

