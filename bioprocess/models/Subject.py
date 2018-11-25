import os
import shutil


#Testar classe
class Subject:

    def __init__(self, chrompack_id, work_dir, subject_name):
        self._chrompack_id = chrompack_id
        self._work_dir = work_dir
        self._subject_name = subject_name

    def _get_zip_file_path(self):
        return "{subject_path}/{subject_name}.zip".format(subject_path=self.get_subject_dir_path(),
                                                          subject_name=self._subject_name)

    def _get_assembly_dir(self):
        return "{subject_path}/mounted".format(subject_path=self.get_subject_dir_path())

    def get_zip_filename(self):
        return "{subject_name}.zip".format(subject_name=self._subject_name)

    def get_subject_dir_path(self):
        return "{work_dir}/{chrompack}/subjects/{subject}".format(work_dir=self._work_dir,
                                                                  chrompack=self._chrompack_id,
                                                                  subject=self._subject_name)

    #Testar caso com workdir errado
    #Testar caso com chrompack não existente
    #Testar caso com pasta subjects not found
    #Testar caso com subject inexistente
    #Testar caso com pasta mounted inexistente
    def is_built(self):

        assembly_dir = self._get_assembly_dir()

        files_assembly = os.listdir(assembly_dir)

        return bool(files_assembly)

    def has_zip_created(self):

        zip_path = self._get_zip_file_path()

        return os.path.isfile(zip_path)

    def create_zip(self):

        if not self.has_zip_created():

            dir = self._get_assembly_dir()
            dir_output = self.get_subject_dir_path()

            shutil.make_archive(os.path.join(dir_output, self._subject_name), 'zip', dir)

    def get_alignments(self, contig_name):

        ace_file = "{assembly_path}/{subject_name}.fasta.ace".format(assembly_path=self._get_assembly_dir(),
                                                                     subject_name=self._subject_name)

        with open(ace_file, 'r') as fp:
            lines_file = fp.readlines()

        contig_found = False
        inside_sequence_alignment = False
        alignments = []

        for line in lines_file:

            if line == '\n':
                continue

            if line[:2] == 'CO':
                if contig_found:
                    break

                if contig_name in line:
                    contig_found = True

            if contig_found:

                if line[:2] == 'RD':
                    sample_file = line.split(' ')[1]
                    alignments.append({'sample': sample_file, 'sequence': ''})
                    inside_sequence_alignment = True
                    continue

                if inside_sequence_alignment:

                    if line[0].upper() in ['A', 'T', 'C', 'G', 'N']:
                        alignments[-1]['sequence'] += line.strip()
                    else:
                        inside_sequence_alignment = False

        return alignments

    def get_results(self):

        contigs_file = "{assembly_path}/{subject_name}.fasta.contigs".format(assembly_path=self._get_assembly_dir(),
                                                                             subject_name=self._subject_name)

        with open(contigs_file, 'r') as fp:
            lines_file = fp.readlines()

        contigs_result = []
        json_contig = None

        for pos, line in enumerate(lines_file):

            if line[0] == '>':

                if json_contig:
                    contigs_result.append(json_contig)

                contig_name = line.split('.')[-1].replace('\n', '')
                contig_name = contig_name.replace('\n', '')

                json_contig = {'name': contig_name,
                               'sequence': [],
                               'alignments': self.get_alignments(contig_name)}
            else:
                json_contig['sequence'].append(line.replace('\n', ''))

            is_last_line = (pos + 1) == len(lines_file)

            if is_last_line:
                contigs_result.append(json_contig)

        return contigs_result
