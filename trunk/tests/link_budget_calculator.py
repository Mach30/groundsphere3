import pint
import math

class LinkBudgetCalculator():
	"""Calculator for link budgets	"""

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
		self._receive_antenna_gain =   0.0                    # dB
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
		# constants
		c = 2.9979*pow(10,8) * ureg.meter / ureg.second	# Speed of Light
		Re = 6371 * ureg.kilometers	# Average Earth Radius
		pi = math.pi # pi
	
	# ---------------- altitude_ground_station ----------------
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
		
	# ---------------- altitude_satellite ----------------
	@property
	def altitude_satellite(self):
		"""Get the average altitude of the satellite
		ret: average altitude of satellite relative to sea level
		"""
		return self._altitude_satellite
	
	@altitude_satellite.setter
	def altitude_satellite(self, value):
		"""Change the altitude of the satellite
		arg1: value -- altitude of satellite relative to sea level
		"""
		self._ureg.check('[length]')(value)
		self._altitude_satellite = value

	# ---------------- orbit_elevation_angle ----------------
	@property
	def orbit_elevation_angle(self):
		"""Get the elevation angle of the satellite relative to gs
		ret: orbit_elevation_angle of satellite relative to gs
		"""
		return self._orbit_elevation_angle
	
	@orbit_elevation_angle.setter
	def orbit_elevation_angle(self, value):
		"""Change the elevation angle of satellite relative to gs
		arg1: value -- elevation angle of satellite
		"""
		self._ureg.check('[angle]')(value)
		self._orbit_elevation_angle = value
		
	# ---------------- downlink_frequency ----------------
	@property
	def downlink_frequency(self):
		"""Get the downlink frequency in Hertz
		ret: frequency of downlink signal in Hertz
		"""
		return self._downlink_frequency
	
	@downlink_frequency.setter
	def downlink_frequency(self, value):
		"""Change the downlink signal frequency in Hertz
		arg1: value -- desired downlink signal frequency in Hertz
		"""
		self._ureg.check('[frequency]')(value)
		self._downlink_frequency = value
		
	# ---------------- target_energy_noise_ratio ----------------
	@property
	def target_energy_noise_ratio(self):
		"""Get the target eb/no in dB
		ret: target eb/no in dB
		"""
		return self._target_energy_noise_ratio
	
	@target_energy_noise_ratio.setter
	def target_energy_noise_ratio(self, value):
		"""Change the target eb/no in dB
		arg1: value -- desired target eb/no in dB
		"""
		self._target_energy_noise_ratio = value
		
	# ---------------- implementation_loss ----------------
	@property
	def implementation_loss(self):
		"""Get the implementation_loss in dB
		ret: implementation_loss in dB
		"""
		return self._implementation_loss
	
	@implementation_loss.setter
	def implementation_loss(self, value):
		"""Change the implementation_loss in dB
		arg1: value -- desired implementation_loss in dB
		"""
		self._implementation_loss = value
		
	# ---------------- transmit_power ----------------
	@property
	def transmit_power(self):
		"""Get the transmit power in Watts
		ret: transmit power in Watts
		"""
		return self._transmit_power
	
	@transmit_power.setter
	def transmit_power(self, value):
		"""Change the transmit power in Watts
		arg1: value -- desired transmit power in Watts
		"""
		self._ureg.check('[power]')(value)
		self._transmit_power = value
		
	# ---------------- transmit_losses ----------------
	@property
	def transmit_losses(self):
		"""Get the transmit_losses in dB
		ret: transmit_losses in dB
		"""
		return self._transmit_losses
	
	@transmit_losses.setter
	def transmit_losses(self, value):
		"""Change the transmit_losses in dB
		arg1: value -- desired transmit_losses in dB
		"""
		self._transmit_losses = value
		
	# ---------------- transmit_antenna_gain ----------------
	@property
	def transmit_antenna_gain(self):
		"""Get the transmit_antenna_gain in dB
		ret: transmit_antenna_gain in dB
		"""
		return self._transmit_antenna_gain
	
	@transmit_antenna_gain.setter
	def transmit_antenna_gain(self, value):
		"""Change the transmit_antenna_gain in dB
		arg1: value -- desired transmit_antenna_gain in dB
		"""
		self._transmit_losses = value
		
	# ---------------- transmit_pointing_loss ----------------
	@property
	def transmit_pointing_loss(self):
		"""Get the transmit_pointing_loss in dB
		ret: transmit_pointing_loss in dB
		"""
		return self._transmit_pointing_loss
	
	@transmit_pointing_loss.setter
	def transmit_pointing_loss(self, value):
		"""Change the transmit_pointing_loss in dB
		arg1: value -- desired transmit_pointing_loss in dB
		"""
		self._transmit_pointing_loss = value
		
	# ---------------- polarization_losses ----------------
	@property
	def polarization_losses(self):
		"""Get the polarization_losses in dB
		ret: polarization_losses in dB
		"""
		return self._polarization_losses
	
	@polarization_losses.setter
	def polarization_losses(self, value):
		"""Change the polarization_losses in dB
		arg1: value -- desired polarization_losses in dB
		"""
		self._polarization_losses = value
		
	# ---------------- atmospheric_loss ----------------
	@property
	def atmospheric_loss(self):
		"""Get the atmospheric_loss in dB
		ret: atmospheric_loss in dB
		"""
		return self._atmospheric_loss
	
	@atmospheric_loss.setter
	def atmospheric_loss(self, value):
		"""Change the atmospheric_loss in dB
		arg1: value -- desired atmospheric_loss in dB
		"""
		self._atmospheric_loss = value
		
	# ---------------- receive_antenna_gain ----------------
	@property
	def receive_antenna_gain(self):
		"""Get the receive_antenna_gain in dB
		ret: receive_antenna_gain in dB
		"""
		return self._receive_antenna_gain
	
	@receive_antenna_gain.setter
	def receive_antenna_gain(self, value):
		"""Change the receive_antenna_gain in dB
		arg1: value -- desired receive_antenna_gain in dB
		"""
		self._receive_antenna_gain = value
		
	# ---------------- receiving_pointing_loss ----------------
	@property
	def receiving_pointing_loss(self):
		"""Get the receiving_pointing_loss in dB
		ret: receiving_pointing_loss in dB
		"""
		return self._receiving_pointing_loss
	
	@receiving_pointing_loss.setter
	def receiving_pointing_loss(self, value):
		"""Change the receiving_pointing_loss in dB
		arg1: value -- desired receiving_pointing_loss in dB
		"""
		self._receiving_pointing_loss = value
		
	# ---------------- system_noise_figure ----------------
	@property
	def system_noise_figure(self):
		"""Get the system_noise_figure in dB
		ret: system_noise_figure in dB
		"""
		return self._system_noise_figure
	
	@system_noise_figure.setter
	def system_noise_figure(self, value):
		"""Change the system_noise_figure in dB
		arg1: value -- desired system_noise_figure in dB
		"""
		self._system_noise_figure = value
		
	# ---------------- noise_bandwidth ----------------
	@property
	def noise_bandwidth(self):
		"""Get the noise_bandwidth in Hertz
		ret: noise_bandwidth in Hertz
		"""
		return self._noise_bandwidth
	
	@noise_bandwidth.setter
	def noise_bandwidth(self, value):
		"""Change the noise_bandwidth in Hertz
		arg1: value -- desired noise_bandwidth in Hertz
		"""
		self._ureg.check('[frequency]')(value)
		self._noise_bandwidth = value
	
	def run(self):
		"""Calculate Link Budget
	`	"""
		# Downlink Wavelength m
		_downlink_wavelength = (c/_downlink_frequency).to('m')
		
		# Link Distance m 
		_orbit_elevation_angle_rad = math.radians(_orbit_elevation_angle)
		beta = _orbit_elevation_angle_rad+(pi/2)
		alpha = math.asin((_altitude_satellite/(_altitude_satellite+Re))*math.sin(beta))
		theta = (pi/2)-alpha-beta
		_link_distance = math.sin(theta)*(_altitude_satellite+Re)/math.sin(beta)
		
		# Transmit Power dBm
		_transmit_power_dBm = power_to_dBm(ureg, _transmit_power)
		
		# Transmit EIRP dBm
		_transmit_eirp = add_dBm_power(ureg, _transmit_power_dBm, _transmit_losses + _transmit_antenna_gain + _transmit_pointing_loss)
	
		# Downlink Path Loss dB
		_downlink_path_loss = -20*math.log10(4*pi*_link_distance/_downlink_wavelength)
		
		# Required En/N0 dB)
		_required_ebno = _target_energy_noise_ratio + _implementation_loss
		
		# Recieved Power dBm
		_received_power = add_dBm_power(ureg, _transmit_eirp, _transmit_antenna_gain + _downlink_path_loss + _polarization_losses + _atmospheric_loss +_receive_antenna_gain + _receiving_pointing_loss)
		
		# MDS dBm
		_minimum_detectable_signal = dBm_to_string(-174+10*math.log10(_noise_bandwidth)+_system_noise_figure)
		
		# Eb/N0 Receieved dB
		_energy_noise_ratio = add_dBm_power(ureg, _received_power, -_minimum_detectable_signal)
	
		# Link Margin dB
		_link_margin = add_dBm_power(ureg, dBm_to_string(_required_ebno), - _energy_noise_ratio)
	
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




