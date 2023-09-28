import unittest 

class TestName(unittest.TestCase):
    def test_name_equal_pedro(self):
        name = "AMIEL"
        self.assertEqual(name, "PEDRO")

if __name__ == "__main__":
    unittest.main()