import unittest
from core.slots import Slots
from test import test_utils


class TestSlots(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.tests_result = test_utils.get_json_from_file('test/data/slots_test.json')

    def get_test_result(self, test_case):

        expected = self.tests_result[test_case]
        expected = str(expected)
        expected = expected.replace("'", '"')
        expected = expected.replace(" ", "")
        expected = expected.replace("None", "null")

        return expected

    def test_get_matrix_filter_subjects(self):

        subject = 'test'
        samples = [
            {
                "slot": "A01",
                "subject": subject
            },
            {
                "slot": "A02",
                "subject": ""
            },
            {
                "slot": "B01",
                "subject": subject
            },
            {
                "slot": "B02",
                "subject": ""
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "B",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject(subject)

        self.assertEqual(matrix, self.get_test_result('filter_subjects'))

    def test_get_matrix_config_lowercase(self):

        subject = 'test'
        samples = [
            {
                "slot": "A01",
                "subject": subject
            },
            {
                "slot": "A02",
                "subject": ""
            },
            {
                "slot": "B01",
                "subject": subject
            },
            {
                "slot": "B02",
                "subject": ""
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "b",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject(subject)

        self.assertEqual(matrix, self.get_test_result('lowercase'))

    def test_get_matrix_filter_all(self):

        samples = [
            {
                "slot": "A01",
                "subject": "test1"
            },
            {
                "slot": "A02",
                "subject": ""
            },
            {
                "slot": "B01",
                "subject": "test2"
            },
            {
                "slot": "B02",
                "subject": "test3"
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "B",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject()

        self.assertEqual(matrix, self.get_test_result('filter_all'))

    def test_slot_not_found(self):

        samples = [
            {
                "slot": "A01",
                "subject": "test1"
            },
            {
                "slot": "A02",
                "subject": ""
            },
            {
                "slot": "B01",
                "subject": "test2"
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "B",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject()

        self.assertEqual(matrix, self.get_test_result('not_found'))

    def test_slot_not_found_when_letter_not_existing(self):

        samples = [
            {
                "slot": "A01",
                "subject": "test1"
            },
            {
                "slot": "A02",
                "subject": ""
            },
            {
                "slot": "C01",
                "subject": "test2"
            },
            {
                "slot": "C02",
                "subject": "test3"
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "C",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject()

        self.assertEqual(matrix, self.get_test_result("not_found_when_letter_not_existing"))

    def test_get_matrix_unordered(self):

        samples = [
            {
                "slot": "B01",
                "subject": "test2"
            },
            {
                "slot": "B02",
                "subject": "test3"
            },
            {
                "slot": "A01",
                "subject": "test1"
            },
            {
                "slot": "A02",
                "subject": ""
            }
        ]

        config = {
                   "slots": {
                     "max_letter": "B",
                     "max_position": 2
                   }
                 }

        slots = Slots(config, samples)
        matrix = slots.get_matrix_busy_by_subject()

        self.assertEqual(matrix, self.get_test_result('unordered'))


if __name__ == '__main__':
    unittest.main()
