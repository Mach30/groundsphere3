from pint import UnitRegistry

class LinkBudgetTestCaseDataset():

    def __init__(self):
        units = UnitRegistry()

        ## populatng data without using the LinkBudget class so that any errors with the class,
        ## or any of its methods, will be uncovered during test execution and not during dataset
        ## initialization
    
        self._datatable = []

        # first test case
        data = self._Data()
        data.name = 'NOAA Weather Satellite'
        data.description = 'A standard NOAA weather satellite, this is a dummy long description ' \
            'that will later be updated to be an accurate description of the test case, instead ' \
            'of this long winded thing that is clearly not meant to be part of real documentation.'
        # inputs
        data.downlink_frequency = 137.5 * units.megahertz
        data.target_energy_noise_ratio = 20.0 # dB
        data.implementation_loss = 1.0 # dB
        data.transmit_power = 5.0 * units.watt
        data.transmit_losses = -1.0 # dB 
        data.transmit_antenna_gain = 4.0 # dB
        data.transmit_pointing_loss = -3.0 # dB
        data.link_distance = 1677.2 * units.kilometers
        data.polarization_losses = 0.0 # dB
        data.atmospheric_loss = -1.1 # dB
        data.receiver_gain = 5.4 # dB
        data.receiving_pointing_loss = -3.0 # dB 
        data.system_noise_figure = 5.0 # dB
        data.noise_bandwidth = 34.0 * units.kilohertz
        # outputs
        data.received_power = -101.4 # dB
        data.minimum_detectable_signal = -123.7 # dB
        data.energy_noise_ratio = 22.3 # dB
        data.link_margin = 1.3 # dB
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

