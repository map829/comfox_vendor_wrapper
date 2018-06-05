from abc import ABCMeta
from abc import abstractmethod


class CredentialFileReader(metaclass=ABCMeta):
    @abstractmethod
    def read_credentials(self, config_file_name=None):
        pass

    @abstractmethod
    def get_credentials(self):
        pass
