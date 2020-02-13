import unittest
import vanity_address_manager as f

class TestSubSeedAddressGenerator(unittest.TestCase):
    def test_vanity_address_generate(self):
        self.assertRaises(ValueError, f.vanity_address_generator, '&#')
        self.assertRaises(ValueError, f.vanity_address_generator, 'X', -1)


if __name__ == '__main__':
    unittest.main()
