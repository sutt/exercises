import unittest, sys, os

c0 = 'FOO'
c1 = 'BAR'



class C2(unittest.TestCase):

    def a(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
    def b(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(C2)
    unittest.TextTestRunner(verbosity=2).run(suite)

    
