from enum import Enum


class SlotState(Enum):

    BUSY = 'busy'
    NOT_FOUND = 'not-found'
    FREE = 'free'


def initialize_data_matrix(max_position, max_letter):

    code_max_letter = ord(max_letter.upper())
    code_letter_a = ord('A')
    data = {}

    for i in range(code_letter_a, code_max_letter + 1):

        letter = chr(i)
        data[letter] = [SlotState.NOT_FOUND.value] * max_position

    return data


def get_matrix_busy_by_subject(config, samples, subject=None):

    max_position = config['slots']['max_position']
    max_letter = config['slots']['max_letter']
    data = initialize_data_matrix(max_position, max_letter)

    for sample in samples:

        slot = sample['slot']

        if slot != "":

            subject_registered = sample['subject']

            slot_letter = slot[0]
            slot_position_number = int(slot[1:3])

            if subject:
                state = SlotState.BUSY if subject == subject_registered else SlotState.FREE
            else:
                state = SlotState.BUSY if subject_registered != "" else SlotState.FREE

            data[slot_letter][slot_position_number - 1] = state.value

        letters = list(data.keys())
        letters.sort()

    return [data[key] for key in letters]
