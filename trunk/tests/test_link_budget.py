import unittest
from . import LinkBudgetTestCaseDataset

class TestLinkBudget(unittest.TestCase):

    NUM_TEST_CASES = 1

    def setUp(self):
        self.test_case_dataset = LinkBudgetTestCaseDataset()
        
    def test_iterable(self):
        count = 0
        for item in self.test_case_dataset:
            count += 1
        self.assertEqual(self.NUM_TEST_CASES, count)

    def test_len(self):
        self.assertEqual(self.NUM_TEST_CASES, len(self.test_case_dataset))

    def test_lb1(self):
        self._test_dataset_item(0)

    def _test_dataset_item(self, item_number):
        tc_data = self.test_case_dataset[item_number]
        self.assertIsNotNone(tc_data.name)
        self.assertIsNotNone(tc_data.description)
        self.assertIsNotNone(tc_data.downlink_frequency)
        self.assertIsNotNone(tc_data.target_energy_noise_ratio)
        self.assertIsNotNone(tc_data.implementation_loss)
        self.assertIsNotNone(tc_data.transmit_losses)
        self.assertIsNotNone(tc_data.transmit_antenna_gain)
        self.assertIsNotNone(tc_data.transmit_pointing_loss)
        self.assertIsNotNone(tc_data.link_distance)
        self.assertIsNotNone(tc_data.polarization_losses)
        self.assertIsNotNone(tc_data.atmospheric_loss)
        self.assertIsNotNone(tc_data.receiver_gain)
        self.assertIsNotNone(tc_data.receiving_pointing_loss)
        self.assertIsNotNone(tc_data.system_noise_figure)
        self.assertIsNotNone(tc_data.noise_bandwidth)
