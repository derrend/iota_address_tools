import unittest
import seed_manager as f

class TestSubSeedAddressGenerator(unittest.TestCase):
    def test_seed_generate(self):
        self.assertRaises(ValueError, next, f.seed_generate('secret_string', -1))


if __name__ == '__main__':
    unittest.main()
