from pint import UnitRegistry

class LinkBudgetTestCaseDataset():

    def __init__(self, ureg):
        """
        Constructor for GS Mk3 link budget test case dataset
        
        The constructor will initialize values of multiple test cases described
        in the documentation.
        
        """
        self._ureg = ureg
        
        ## populatng data without using the LinkBudget class so that any errors with the class,
        ## or any of its methods, will be uncovered during test execution and not during dataset
        ## initialization

        self._datatable = []

        # first test case
        data = self._Data()
        data.name = 'NOAA Weather Satellite'
        data.description = 'Standard link budget for the groundsphere Mk 3 setup. Includes      ' \
            'values for eggbeater antenna, NOAA 19 weather satellite, inclined orbit, and ' \
            '137.5 MHz APT data. Used as target link budget calculation.' \
            'Developed by Mach 30 team using known, researched system values. '
        data.reference = 'https://www.wmo-sat.info/oscar/satellites/view/341'
        # inputs
        data.altitude_ground_station = 400 * ureg.meter     # m
        data.altitude_satellite = 860 * ureg.kilometer      # km
        data.orbit_elevation_angle = 25 * ureg.degree       # deg
        data.downlink_frequency = 137.5 * ureg.megahertz    # Hz
        data.target_energy_noise_ratio = 20.0               # dB
        data.implementation_loss = -1.0                     # dB
        data.transmit_power = 5.0 * ureg.watt               # Watt
        data.transmit_losses = -1.0                         # dB 
        data.transmit_antenna_gain = 4.0                    # dB
        data.transmit_pointing_loss = -3.0                  # dB
        data.polarization_losses = 0.0                      # dB
        data.atmospheric_loss = -0.75                        # dB
        data.receive_antenna_gain = 5.4                     # dB
        data.receiving_pointing_loss = -3.0                 # dB 
        data.system_noise_figure = 5.0                      # dB
        data.noise_bandwidth = 34.0 * ureg.kilohertz        # Hz
        # intermediates
        data.downlink_wavelength = 2.180 * ureg.meter       # m
        data.link_distance = 1700 * ureg.kilometer          # km
        data.required_ebno = 21.0                           # dB
        data.transmit_power_dBm = 37.0                      # dBm
        data.transmit_eirp = 37.0                           # dBm
        data.downlink_path_loss = -140                      # dB
        # outputs
        data.received_power = -100                          # dBm
        data.minimum_detectable_signal = -124               # dBm
        data.energy_noise_ratio = 23                        # dB
        data.link_margin = 2                                # dB
        # add it to the data table
        self._datatable.append(data)

    def __getitem__(self, key):
        data = self._datatable[key]
        # TODO: make this return a LinkBudgetTestCase, which extends a LinkBudget class. 
        return data

    def __len__(self):
        return len(self._datatable)

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        return self.next()

    def next(self):
        result = None
        try:
            result = self[self.__index]
        except IndexError:
            raise StopIteration
        self.__index += 1
        return result

    class _Data:
        def __str__(self):
            return self.name

