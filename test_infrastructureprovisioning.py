# test_infrastructureprovisioning.py
"""
Tests for InfrastructureProvisioning module.
"""

import unittest
from infrastructureprovisioning import InfrastructureProvisioning

class TestInfrastructureProvisioning(unittest.TestCase):
    """Test cases for InfrastructureProvisioning class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfrastructureProvisioning()
        self.assertIsInstance(instance, InfrastructureProvisioning)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfrastructureProvisioning()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
