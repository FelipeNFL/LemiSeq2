from abc import ABC, abstractmethod


class Authenticator(ABC):

    @abstractmethod
    def validate(self, username, password):
        raise NotImplementedError
