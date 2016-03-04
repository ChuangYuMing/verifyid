import unittest
from verifyid import verifyid

verify = verifyid.IdentyNumber()

class TestMainMethod(unittest.TestCase):
	def setUP(self):
		pass

	def test_number_isvalid(self):
		self.assertTrue(verify._IdentyNumber__isValid("A123456789"))
		self.assertFalse(verify._IdentyNumber__isValid("A12345678910"))
		self.assertFalse(verify._IdentyNumber__isValid("BB12345678"))
		self.assertFalse(verify._IdentyNumber__isValid("%123456789"))

	def test_check_identy_number(self):
		self.assertTrue(verify._IdentyNumber__isValid("A123456789"))
		self.assertFalse(verify._IdentyNumber__isValid("A12345678910"))
		self.assertFalse(verify._IdentyNumber__isValid("BB12345678"))
		self.assertFalse(verify._IdentyNumber__isValid("%123456789"))


	def test_get_city_name(self):
		self.assertEqual(verify.get_city("G245983256"), "宜蘭縣")


if __name__ == '__main__':
    unittest.main()