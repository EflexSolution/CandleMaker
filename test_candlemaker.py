# test_candlemaker.py
"""
Tests for CandleMaker module.
"""

import unittest
from candlemaker import CandleMaker

class TestCandleMaker(unittest.TestCase):
    """Test cases for CandleMaker class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CandleMaker()
        self.assertIsInstance(instance, CandleMaker)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CandleMaker()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
