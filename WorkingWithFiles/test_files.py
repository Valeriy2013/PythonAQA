"""
Unit tests for the files library
"""

import WorkingWithFiles.files as f
import pytest
from WorkingWithFiles.files import Person


@pytest.mark.files
class TestWorkingWithFiles:

    # @pytest.mark.parametrize("path", ["samples/xml/test_data.xml", "samples/json/updated_test_data.json"])
    def test_isSourceFileExist(self):
        assert f.isFileExist("samples/xml/test_data.xml")

    def test_checkSourceFileContentAfterUpdate(self):
        person_list = [
            Person("First1", "Last1", "2001", "Jan", "1", "company1", "project1", "role1", "room#1", "hobby1"),
            Person("First2", "Last2", "2002", "Jan", "2", "company2", "project2", "role2", "room#2", "hobby2"),
            Person("First3", "Last3", "2003", "Jan", "3", "company3", "project3", "role3", "room#3", "hobby3")]
        f.dataFileProcessing("samples/xml/test_data.xml", "samples/json/updated_test_data.json", person_list)
        actual = f.readFileContent("samples/xml/test_data.xml")
        expected = f.readFileContent("samples/xml/expected_test_data.xml")
        assert actual == expected

    def test_isDestinationFileExist(self):
        person_list = [
            Person("First1", "Last1", "2001", "Jan", "1", "company1", "project1", "role1", "room#1", "hobby1"),
            Person("First2", "Last2", "2002", "Jan", "2", "company2", "project2", "role2", "room#2", "hobby2"),
            Person("First3", "Last3", "2003", "Jan", "3", "company3", "project3", "role3", "room#3", "hobby3")]
        f.dataFileProcessing("samples/xml/test_data.xml", "samples/json/updated_test_data.json", person_list)
        assert f.isFileExist("samples/json/updated_test_data.json")

    def test_checkDestinationFileContent(self):
        person_list = [
            Person("First1", "Last1", "2001", "Jan", "1", "company1", "project1", "role1", "room#1", "hobby1"),
            Person("First2", "Last2", "2002", "Jan", "2", "company2", "project2", "role2", "room#2", "hobby2"),
            Person("First3", "Last3", "2003", "Jan", "3", "company3", "project3", "role3", "room#3", "hobby3")]
        f.dataFileProcessing("samples/xml/test_data.xml", "samples/json/updated_test_data.json", person_list)
        actual = f.readFileContent("samples/json/updated_test_data.json")
        expected = f.readFileContent("samples/json/expected_updated_test_data.json")
        assert actual == expected
