from unittest import TestCase
from config_reader.XMLCredentialFileReader import XMLCredentialFileReader
import os


class TestXMLCredentialFileReaderIT(TestCase):
    def setUp(self):
        self.xml_credential_reader = XMLCredentialFileReader()

    def test_get_credentials_none(self):
        credentials = self.xml_credential_reader.get_credentials()
        self.assertEqual(credentials, (None, None))

    def test_get_credentials_valid(self):
        xml_credential_reader = XMLCredentialFileReader("Username", "Password")
        credentials = xml_credential_reader.get_credentials()
        assert ("Username" == credentials[0])
        assert ("Password" == credentials[1])

    def test_get_credentials_bogus_attributes(self):
        with self.assertRaises(TypeError):
            self.xml_credential_reader.read_credentials(object())

    def test_read_credentials(self):
        username = 'comfox'
        password = 'Testiboii'
        current_working_directory = os.getcwd()
        config_file = os.path.join(current_working_directory, 'Config.xml')
        self.xml_credential_reader.read_credentials(config_file)
        credentials = self.xml_credential_reader.get_credentials()
        assert (username == credentials[0])
        assert (password == credentials[1])
