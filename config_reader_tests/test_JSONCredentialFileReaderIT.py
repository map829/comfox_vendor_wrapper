from unittest import TestCase
from config_reader.JSONCredentialFileReader import JSONCredentialFileReader
import os


class TestJSONCredentialFileReaderIT(TestCase):
    def setUp(self):
        self.json_credential_reader = JSONCredentialFileReader()

    def test_get_credentials_none(self):
        credentials = self.json_credential_reader.get_credentials()
        self.assertEqual(credentials, (None, None))

    def test_get_credentials_valid(self):
        json_credential_reader = JSONCredentialFileReader("Username", "Password")
        credentials = json_credential_reader.get_credentials()
        assert ("Username" == credentials[0])
        assert ("Password" == credentials[1])

    def test_get_credentials_bogus_attributes(self):
        with self.assertRaises(TypeError):
            self.json_credential_reader.read_credentials(object())

    def test_read_credentials(self):
        username = 'Testname'
        password = 'Testpass'
        current_working_directory = os.getcwd()
        config_file = os.path.join(current_working_directory, 'Config.json')
        self.json_credential_reader.read_credentials(config_file)
        credentials = self.json_credential_reader.get_credentials()
        assert (username == credentials[0])
        assert (password == credentials[1])
