import pint
from math import log10

def power_to_dBm(ureg, val_power):
	"""
	Output the dBm value of a pint power input
	arg1: 	ureg 	  -- unit registry to use for conversion
	arg2: 	val_power -- value to convert to raw dBm
						 throws an error if this value is not pint power
	ret:              -- result of conversion in dBm
	"""
	ureg.check('[power]')(val_power)
	val_mW = val_power.to(ureg.mW)
	val_power_dBm = 10 * log10(val_mW.magnitude)
	return val_power_dBm

def add_dBm_power(ureg, val_dBm, val_power):
	"""Output the addition of a dBm and pint power
	arg1: 	ureg 	  -- unit registry to use for conversion
	arg2: 	val_dBm   -- value to add in dBm
	arg3: 	val_power -- value to add in a pint unit of power
						 throws an error if this value is not pint power
	ret:              -- result of addition in dBm
	"""
	return val_dBm + power_to_dBm(ureg, val_power)

def dBm_to_string(val_dBm):
	"""Output a string with the dBm value
	arg1: 	val_dBm   -- value to add in dBm
	ret:              -- string representation of value in dBm
	"""
	return '{} dBm'.format(val_dBm)