import string
from pandas import DataFrame
from enum import Enum


class SlotState(Enum):

    BUSY = 'busy'
    NOT_FOUND = 'not-found'
    FREE = 'free'


class Slots:

    def __init__(self, config, samples):

        self._samples = samples
        self._df_matrix = self._initialize_matrix(config)

    def _get_letters_list(self, max_letter):

        max_letter = max_letter.upper()
        alphabet = list(string.ascii_uppercase)
        index_last_letter = alphabet.index(max_letter) + 1

        return alphabet[:index_last_letter]

    def _initialize_matrix(self, config):

        max_position = config['slots']['max_position']
        max_letter = config['slots']['max_letter']
        numbers = [str(number).zfill(2) for number in range(1, max_position + 1)]

        df = DataFrame(columns=self._get_letters_list(max_letter), index=numbers)

        return df

    def _add_to_df(self, slot, state, subject):

        slot_letter = slot[0]
        slot_position_number = slot[1:3]
        content = {'state': state.value, 'subject': subject}

        self._df_matrix.at[slot_position_number, slot_letter] = content

    def _get_state_slot(self, subject_registered, subject):

        if not subject and subject_registered != "":
            return SlotState.BUSY

        if subject == subject_registered:
            return SlotState.BUSY

        return SlotState.FREE

    def get_matrix_busy_by_subject(self, subject=None):

        for sample in self._samples:

            slot = sample['slot']

            if slot != "":

                subject_registered = sample['subject']
                state = self._get_state_slot(subject_registered, subject)

                self._add_to_df(slot, state, subject_registered)

        return self._df_matrix.to_json(orient='index')
