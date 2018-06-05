from config_reader.CredentialFileReader import CredentialFileReader
import json


class JSONCredentialFileReader(CredentialFileReader):
    # Constructor: This method gets called when an object is created from this class
    def __init__(self, username=None, password=None):
        self.__username = username
        self.__password = password

    # Reads the username and password from a JSON File and stores it in this object
    def read_credentials(self, config_file_name=None):
        with open(config_file_name) as json_file:
            json_data = json.load(json_file)
            self.__username = json_data['username']
            self.__password = json_data['password']

    # Returns the username and password stored in this object
    def get_credentials(self):
        return self.__username, self.__password
