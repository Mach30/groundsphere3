import pint
import Convert_dBm
import unittest

class ConvertTest(unittest.TestCase):

	def setUp(self):
		self.ureg = pint.UnitRegistry()

	def test_Conversion(self):
		"""Test if power_to_dBm function can convert values of power
		in W or mw to correct values of dBm
		"""
		x_1 = 1000 * self.ureg.mW
		x_2 = 1    * self.ureg.W
		y_1 = Convert_dBm.power_to_dBm(self.ureg, x_1)
		y_2 = Convert_dBm.power_to_dBm(self.ureg, x_2)
		self.assertEqual(y_1, 30)
		self.assertEqual(y_2, 30)
		self.assertEqual(y_1, y_2)

	def test_Addition(self):
		"""Test if addition between power and dBm type is successful
		"""
		x = 1000 * self.ureg.mW
		r = 30 #dBm
		z = Convert_dBm.add_dBm_power(self.ureg, r, x)
		self.assertEqual(z, 60)

	def test_Error_Convert(self):
		"""Test if attempt at conversion with incorrect unit
		dimension results in exception
		"""
		x = 10 * self.ureg.meter
		with self.assertRaises(Exception) as context:
			Convert_dBm.power_to_dBm(self.ureg, x)
		self.assertTrue('Cannot convert' in str(context.exception))
		
	def test_Error_Addition(self):
		"""Test if attempt at conversion with incorrect unit
		dimension results in exception
		"""
		x = 10 * self.ureg.meter
		with self.assertRaises(Exception) as context:
			Convert_dBm.add_dBm_power(self.ureg, 30, x)
		self.assertTrue('Cannot convert' in str(context.exception))
	
	def test_Negative_Conversion(self):
		"""Test if powers below 0 dBm successfully convert to
		negative dBm values
		"""
		x = 10 * self.ureg.uW
		y = Convert_dBm.power_to_dBm(self.ureg, x)
		self.assertEqual(y, -20)

	def test_Negative_Addition(self):
		"""Test if addition with powers below 0 dBm successfully add
		"""
		x_1 = -20 #dBm
		x_2 = 10 * self.ureg.uW
		y = Convert_dBm.add_dBm_power(self.ureg, x_1, x_2)
		self.assertEqual(y, -40)
	
	def test_To_String(self):
		"""Test if conversion to string is successful
		"""
		x = 10 * self.ureg.W
		y = Convert_dBm.dBm_to_string(Convert_dBm.power_to_dBm(self.ureg, x))
		self.assertEqual(y, '40.0 dBm')
		
if __name__ == '__main__':
	unittest.main()