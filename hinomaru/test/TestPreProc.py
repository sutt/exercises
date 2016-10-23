import os,sys, unittest
from os import path

#sys.path.append('..')
#sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
#sys.path.append(os.path.join('..', 'utils'))

if __name__ != "__main__":
    from utils.utils import SearchData


class TestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
        
    def test_upper3(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
        
    def testfunp2(self):
        self.assertEqual(1,1,'hey')
        
        

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner(verbosity=2).run(suite)
    #suite = unittest.TestLoader().loadTestsFromTestCase(Cc)
    #unittest.TextTestRunner(verbosity=2).run(suite)
    

def main():
    s  = SearchData()
    print s.x
    
    if True:
        unittest.main()
    else:
        suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
        unittest.TextTestRunner(verbosity=2).run(suite)
    return 1

