import unittest

from primes import is_prime
   
from functionalities.functionailites import *

import sys
    

class PrimesTestCase(unittest.TestCase):
    """
        test for primes.py
    """
    def test_is_five_prime(self):
        """
            is five successfully determined to be a prime?
        """
        self.assertTrue(is_prime(5))
        
    def test_prime_float(self):
        self.assertTrue(is_prime(sys.argve[1]))
    

if __name__=="__main__":
    unittest.main()
