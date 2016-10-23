import unittest 
import sys
class TestClass(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')

    def test_upper_wrong(self):
        self.assertEqual('foo'.upper(), 'FOOL', 'this is suppoed to be wrong')
        
    def test_right_vs_wrong(self):
        self.assertTrue('FOO' == c0, 'Foo should always equal c0')
        self.assertFalse(c1 == c0, 'c1 and c0 should always be distinct')
        
    def test_upper2(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
        
        
if len(sys.argv) < 2:
    if __name__ == "__main__":
        unittest.main()
else:
    suite = unittest.TestLoader().loadTestsFromTestCase(TestClass)
    unittest.TextTestRunner(verbosity=2).run(suite)