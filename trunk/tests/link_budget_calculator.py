import pint
import math
from Convert_dBm import power_to_dBm
from Convert_dBm import add_dBm_power

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
		self._receive_antenna_gain =    0.0                   # dB
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
		
		self._is_valid =                  False               # bool
		
		# constants
		self.c = 2.9979*pow(10,8) * ureg.meter / ureg.second	# Speed of Light
		self.Re = 6371 * ureg.kilometers	# Average Earth Radius
	
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
		self._ureg.check('degree')(value)
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
		self._transmit_antenna_gain = value
		
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
		
	# ------------------------------------------------
	# ----------------    outputs     ----------------
	# ------------------------------------------------
	
	# ---------------- downlink_wavelength ----------------
	@property
	def downlink_wavelength(self):
		"""Get the downlink_wavelength in meters
		ret: downlink_wavelength in meters
		"""
		return self._downlink_wavelength
		
	# ---------------- link_distance ----------------
	@property
	def link_distance(self):
		"""Get the link_distance in meters
		ret: link_distance in meters
		"""
		return self._link_distance
		
	# ---------------- required_ebno ----------------
	@property
	def required_ebno(self):
		"""Get the required_ebno in dB
		ret: required_ebno in dB
		"""
		return self._required_ebno
		
	# ---------------- transmit_power_dBm ----------------
	@property
	def transmit_power_dBm(self):
		"""Get the transmit_power_dBm in dBm
		ret: transmit_power_dBm in dBm
		"""
		return self._transmit_power_dBm
		
	# ---------------- transmit_eirp ----------------
	@property
	def transmit_eirp(self):
		"""Get the transmit_eirp in dBm
		ret: transmit_eirp in dBm
		"""
		return self._transmit_eirp
		
	# ---------------- downlink_path_loss ----------------
	@property
	def downlink_path_loss(self):
		"""Get the downlink_path_loss in dB
		ret: downlink_path_loss in dB
		"""
		return self._downlink_path_loss
		
	# ---------------- received_power ----------------
	@property
	def received_power(self):
		"""Get the received_power in dBm
		ret: received_power in dBm
		"""
		return self._received_power
		
	# ---------------- minimum_detectable_signal ----------------
	@property
	def minimum_detectable_signal(self):
		"""Get the mds in dBm
		ret: mds in dBm
		"""
		return self._minimum_detectable_signal
		
	# ---------------- energy_noise_ratio ----------------
	@property
	def energy_noise_ratio(self):
		"""Get the energy_noise_ratio in dB
		ret: energy_noise_ratio in dB
		"""
		return self._energy_noise_ratio
		
	# ---------------- link_margin ----------------
	@property
	def link_margin(self):
		"""Get the link_margin in dB
		ret: link_margin in dB
		"""
		return self._link_margin
	
	@property
	def is_valid(self):
		"""Get the is_valid flag to determine if the run() function
		successfully calculated a link margin
		"""
		return self._is_valid
	
	def run(self):
		"""Run function to perform calculations necessary to determine outputs
		of link budget calculation
		is_valid will result in True if calculations were successful
	`	"""
		# set is_valid to false every time a run is initiated
		self._is_valid = False
	
		# Downlink Wavelength m
		self._downlink_wavelength = self.c / self._downlink_frequency.to('1 / second')
		
		# DEBUG
		#print('wavelength: {}'.format(self._downlink_wavelength))
		
		# Link Distance m
		orbit_elevation_angle_rad = math.radians(self._orbit_elevation_angle.magnitude)
		beta = orbit_elevation_angle_rad + (math.pi / 2)
		alpha = math.asin(((self._altitude_ground_station + self.Re) / (self._altitude_satellite + self.Re)) * math.sin(beta))
		theta = math.pi - alpha - beta
		self._link_distance = math.sin(theta) * (self._altitude_satellite + self.Re) / math.sin(beta)
		
		# DEBUG
		#print('link_distance: {}'.format(self._link_distance))
		
		# Transmit Power dBm
		self._transmit_power_dBm = power_to_dBm(self._ureg, self._transmit_power)
		
		# DEBUG
		#print('Tx power dBm: {}'.format(self._transmit_power_dBm))
		
		# Transmit EIRP dBm
		self._transmit_eirp = self._transmit_power_dBm + self._transmit_losses + self._transmit_antenna_gain + self._transmit_pointing_loss
		
		# DEBUG
		#print('Tx EIRP: {}'.format(self._transmit_eirp))
	
		# Downlink Path Loss dB
		self._downlink_path_loss = -20 * math.log10(4 * math.pi * self._link_distance / self._downlink_wavelength)
		
		# DEBUG
		#print('Path Loss : {}'.format(self._downlink_path_loss))
		
		# Required Eb/N0 dB)
		self._required_ebno = self._target_energy_noise_ratio - self._implementation_loss
		
		# DEBUG
		#print('Req Eb/N0 : {}'.format(self._required_ebno))
		
		# Recieved Power dBm
		self._received_power = self._transmit_eirp + self._downlink_path_loss + self._polarization_losses + self._atmospheric_loss + self._receive_antenna_gain + self._receiving_pointing_loss
		
		# DEBUG
		#print('Rx Power : {}'.format(self._received_power))
		
		# MDS dBm
		self._minimum_detectable_signal = -174 + 10 * math.log10(self._noise_bandwidth.to('hertz').magnitude) + self._system_noise_figure
		
		# DEBUG
		#print('MDS : {}'.format(self._minimum_detectable_signal))
		
		# Eb/N0 Receieved dB
		self._energy_noise_ratio = self._received_power - self._minimum_detectable_signal
		
		# DEBUG
		#print('Eb/N0 : {}'.format(self._energy_noise_ratio))
	
		# Link Margin dB
		self._link_margin = self._energy_noise_ratio - self._required_ebno
		
		# DEBUG
		#print('Margin : {}'.format(self._link_margin))
		
		self._is_valid = True
	
		
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	




