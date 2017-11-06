import pint

class LinkBudgetCalculator():
	"""Calculator for link budgets
	"""

	def __init__(self, ureg):
		"""Constructor
		arg1: ureg -- pint Unit Registry
		"""
		# set the unit registry to given pint registry
		self._ureg = ureg

		# inputs
		self._altitude_ground_station = 0 * ureg.meter        # m
		self._altitude_satellite =      0 * ureg.meter        # m
		self._orbit_elevation_angle =   0 * ureg.degree       # deg
		self._downlink_frequency =      0 * ureg.hertz        # Hz
		self._target_energy_noise_ratio = 0.0                 # dB
		self._implementation_loss =       0.0                 # dB
		self._transmit_power =          0 * ureg.watt         # Watt
		self._transmit_losses =         0.0                   # dB 
		self._transmit_antenna_gain =   0.0                   # dB
		self._transmit_pointing_loss =  0.0                   # dB
		self._polarization_losses =     0.0                   # dB
		self._atmospheric_loss =        0.0                   # dB
		self._receiver_gain =           0.0                   # dB
		self._receiving_pointing_loss = 0.0                   # dB 
		self._system_noise_figure =     0.0                   # dB
		self._noise_bandwidth =         0 * ureg.hertz        # Hz
		# intermediates
		self._downlink_wavelength =     0 * ureg.meter        # m
		self._link_distance =           0 * ureg.meter        # m
		self._required_ebno =           0.0                   # dB
		self._transmit_power_dBm =      0.0                   # dBm
		self._transmit_eirp =           0.0                   # dBm
		self._downlink_path_loss =      0                     # dB
		# outputs
		self._received_power =            0.0                 # dBm
		self._minimum_detectable_signal = 0.0                 # dBm
		self._energy_noise_ratio =        0.0                 # dB
		self._link_margin =               0.0                 # dB
	
	@property
	def altitude_ground_station(self):
		"""Get the altitude of the ground station
		ret: altitude of ground station relative to sea level
		"""
		return self._altitude_ground_station
	
	@altitude_ground_station.setter
	def altitude_ground_station(self, value):
		"""Change the altitude of the ground station
		arg1: value -- altitude of ground station relative to sea level
		"""
		self._ureg.check('[length]')(value)
		self._altitude_ground_station = value
		
	# TODO -- add all methods for each variable




