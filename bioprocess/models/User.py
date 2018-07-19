
class User:

    def __init__(self, dbconnection, user):

        self._dbconnection = dbconnection
        self._collection = 'chrompack'
        self._user = user

    def _get_chrompacks(self):

        query = {'user': self._user}

        return self._dbconnection.find(query, self._collection)

    def get_num_chrompacks(self):

        return len(self._get_chrompacks())

    def get_num_samples(self):

        chrompacks = self._get_chrompacks()
        total_samples = 0

        for chrompack in chrompacks:
            samples = chrompack['samples']
            total_samples += len(samples)

        return total_samples

    def get_subjects(self):
        return 0
