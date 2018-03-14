from abc import ABCMeta
from abc import abstractmethod


class CredentialFileReader(metaclass=ABCMeta):
    """Parses credential files"""

    @abstractmethod
    def get_credentials(self, config_file_name = None):
        """Parse the provided config file and return username and password as strings"""
        pass
