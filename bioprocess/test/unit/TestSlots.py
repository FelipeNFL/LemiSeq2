import unittest
from core import slots


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

        matrix = slots.get_matrix_busy_by_subject(config, samples, subject)

        expected = [
            ['busy', 'free'],
            ['busy', 'free'],
        ]

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

        matrix = slots.get_matrix_busy_by_subject(config, samples, subject)

        expected = [
            ['busy', 'free'],
            ['busy', 'free'],
        ]

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

        matrix = slots.get_matrix_busy_by_subject(config, samples)

        expected = [
            ['busy', 'free'],
            ['busy', 'busy'],
        ]

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

        matrix = slots.get_matrix_busy_by_subject(config, samples)

        expected = [
            ['busy', 'free'],
            ['busy', 'not-found'],
        ]

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

        matrix = slots.get_matrix_busy_by_subject(config, samples)

        expected = [
            ['busy', 'free'],
            ['not-found', 'not-found'],
            ['busy', 'busy'],
        ]

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

        matrix = slots.get_matrix_busy_by_subject(config, samples)

        expected = [
            ['busy', 'free'],
            ['busy', 'busy'],
        ]

        self.assertEqual(matrix, expected)


if __name__ == '__main__':
    unittest.main()
