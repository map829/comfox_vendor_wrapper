from config_reader.CredentialFileReader import CredentialFileReader
import os
from xml.etree import ElementTree


class XMLCredentialFileReader(CredentialFileReader):
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    # Reads the username and password from a XML File and stores it in this object
    def read_credentials(self, config_file_name=None):
        credential = ElementTree.parse(xml_config)
        self.__username = credential.find('Username').text
        self.__password = credential.find('Password').text

    # Returns the username and password stored in this object
    def get_credentials(self):
        return self.__username, self.__password


if __name__ == '__main__':
    credential_reader = XMLCredentialFileReader()
    current_working_directory = os.getcwd()
    xml_config = os.path.join(current_working_directory, 'Config.xml')
    credential_reader.read_credentials(xml_config)
    print(str(credential_reader.get_credentials()))