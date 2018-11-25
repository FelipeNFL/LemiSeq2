from Bio import SeqIO
from collections import defaultdict
import matplotlib.pyplot as plt


class Sample:

    def __init__(self, work_dir, chrompack_id, sample_filename):

        self._chrompack_id = chrompack_id
        self._sample_filename = sample_filename
        self._work_dir = work_dir

    def _get_absolut_filename(self):
        return "{work_dir}/{chrompack}/samples/{sample}".format(work_dir=self._work_dir,
                                                                chrompack=self._chrompack_id,
                                                                sample=self._sample_filename)

    #Testar quando sample não existir
    def get_traces_files(self):

        sample_filepath = self._get_absolut_filename()
        record = SeqIO.read(sample_filepath, 'abi')
        channels = ['DATA9', 'DATA10', 'DATA11', 'DATA12']
        trace = defaultdict(list)
        
        for channel in channels:
            trace[channel] = record.annotations['abif_raw'][channel]

