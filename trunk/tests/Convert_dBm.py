import pint
from math import log10

def add_dBm_power(ureg, val_dBm, val_power):
	"""Output the addition of a dBm and pint power
	arg1: 	ureg 	       -- unit registry to use for conversion
	arg2: 	val_dBm        -- value to add in dBm
	arg3: 	val_power      -- value to add in a pint unit of power
	return:	val_power_out  -- result of addition in dBm
	"""
	val_mW = val_power.to(ureg.mW)
	val_power_dBm = 10 * log10(val_mW.magnitude)
	return val_power_dBm + val_dBm

def power_to_dBm(ureg, val_power):
	"""Output the dBm value of a pint power input
	arg1: 	ureg 	      -- unit registry to use for conversion
	arg2: 	val_dBm       -- value to convert in a pint unit of power
	return:	val_power_dBm -- result of conversion in dBm
	"""
	val_mW = val_power.to(ureg.mW)
	val_power_dBm = 10 * log10(val_mW.magnitude)
	return val_power_dBm
