import unittest
from core.slots import Slots


class TestSlots(unittest.TestCase):

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
        expected = '{"1":{"A":"busy","B":"busy"},"2":{"A":"free","B":"free"}}'

        self.assertEqual(matrix, expected)

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
        expected = '{"1":{"A":"busy","B":"busy"},"2":{"A":"free","B":"free"}}'

        self.assertEqual(matrix, expected)

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
        expected = '{"1":{"A":"busy","B":"busy"},"2":{"A":"free","B":"busy"}}'

        self.assertEqual(matrix, expected)

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
        expected = '{"1":{"A":"busy","B":"busy"},"2":{"A":"free","B":"not-found"}}'

        self.assertEqual(matrix, expected)

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
        expected = '{"1":{"A":"busy","B":"not-found","C":"busy"},"2":{"A":"free","B":"not-found","C":"busy"}}'

        self.assertEqual(matrix, expected)

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
        expected = '{"1":{"A":"busy","B":"busy"},"2":{"A":"free","B":"busy"}}'

        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    unittest.main()
