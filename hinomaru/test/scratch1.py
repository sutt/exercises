import unittest, sys, os

c0 = 'FOO'
c1 = 'BAR'

class C:
    def __init__(self):
        self.x = None
        
c = C()
c.x = "hello"
print c.x

class C2(unittest.TestCase):

    def a(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')
    def b(self):
        self.assertEqual('foo'.upper(), 'FOO', 'this should never fail')


class PreprocTests(unittest.TestCase):

    def valids_length(self):
        self.assertEqual( len(valids), 126)
        
    def valids_less_than_combos(self):
        self.assertTrue( len(valids) < len(combos) )

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(C2)
    unittest.TextTestRunner(verbosity=2).run(suite)

    
