import os
import subprocess
import logging


class ManagerSubject:

    def __init__(self, work_dir, id_chrompack, subject_name):

        self._work_dir = work_dir
        self._id_chrompack = id_chrompack
        self._subject_name = subject_name

    def get_all_subjects_path(self):
        return '{work_dir}/{chrompack}/subjects'.format(work_dir=self._work_dir,
                                                        chrompack=self._id_chrompack,)

    def get_subject_path(self):
        return '{all_subjects}/{subject}'.format(all_subjects=self.get_all_subjects_path(),
                                                 subject=self._subject_name)

    def get_path_phd_pool(self):
        return '{subject_path}/phd'.format(subject_path=self.get_subject_path())

    def get_path_mounted_dna(self):
        return '{subject_path}/mounted'.format(subject_path=self.get_subject_path())

    def create_all_subject_dir(self):

        all_subjects_path = self.get_all_subjects_path()

        if not os.path.isdir(all_subjects_path):
            os.mkdir(all_subjects_path)

    def create_dirs(self):

        path_subject = self.get_subject_path()
        path_phd = self.get_path_phd_pool()
        path_mounted = self.get_path_mounted_dna()

        self.create_all_subject_dir()

        os.mkdir(path_subject)
        os.mkdir(path_phd)
        os.mkdir(path_mounted)

    def build(self, filenames, phred_bin, phred_parameters, phd2fas_bin, phrap_bin):
        self.create_phd_files(filenames, phred_bin, phred_parameters)
        fasta_filename = self.create_fasta_file(phd2fas_bin)
        self.mount_dna(phrap_bin, fasta_filename)

    def create_phd_files(self, filenames_ab1, phred_bin, phred_parameters):

        phd_dir = self.get_path_phd_pool()

        for file_ab1 in filenames_ab1:
            p = subprocess.Popen([phred_bin, file_ab1, '-pd', phd_dir],
                                 env={'PHRED_PARAMETER_FILE': phred_parameters})
            p.wait()
            logging.info('phd created of file {file}'.format(file=file_ab1))
            
    def create_fasta_file(self, phd2fas_bin):

        mounted_dir = self.get_path_mounted_dna()
        phd_dir = '../phd'
        phd2fas_bin = '../../../../../../{bin}'.format(bin=phd2fas_bin)
        fasta_file = '{subject}.fasta'.format(subject=self._subject_name)

        p = subprocess.Popen([phd2fas_bin, "-id", phd_dir, "-os", fasta_file, "-oq", fasta_file + ".qual"],
                             cwd=mounted_dir,
                             close_fds=True)
        p.wait()
        logging.info('fasta created of subject {subject}'.format(subject=self._subject_name))

        return fasta_file

    def mount_dna(self, phrap_bin, fasta):

        mounted_dir = self.get_path_mounted_dna()
        filename_out = '{mounted_dir}/{subject}.out'.format(mounted_dir=mounted_dir, subject=self._subject_name)

        with open(filename_out, 'w') as fp:
            phrap_bin = '../../../../../../{bin}'.format(bin=phrap_bin)
            p = subprocess.Popen([phrap_bin, '-new_ace', fasta],
                                 cwd=mounted_dir,
                                 stdout=fp,
                                 stderr=fp,
                                 close_fds=True)

            p.wait()
            logging.info('base calling of subject {subject} finished'.format(subject=self._subject_name))


