import pint
import Convert_dBm
import unittest

class ConvertTest(unittest.TestCase):

	def setUp(self):
		self.ureg = pint.UnitRegistry()

	def test_Conversion(self):
		x_1 = 1000 * self.ureg.mW
		x_2 = 1    * self.ureg.W
		y_1 = Convert_dBm.power_to_dBm(self.ureg, x_1)
		y_2 = Convert_dBm.power_to_dBm(self.ureg, x_2)
		self.assertEqual(y_1, 30)
		self.assertEqual(y_2, 30)
		self.assertEqual(y_1, y_2)

	def test_Addition(self):
		x = 1000 * self.ureg.mW
		r = 30 #dBm
		z = Convert_dBm.add_dBm_power(self.ureg, r, x)
		self.assertEqual(z, 60)

if __name__ == '__main__':
	unittest.main()