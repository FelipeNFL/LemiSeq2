from abc import ABC, abstractmethod

class Authenticator(ABC):

    @abstractmethod
    def validade(self, username, password):
        raise NotImplementedError
