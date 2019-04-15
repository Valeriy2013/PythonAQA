"""
Files library.
"""

import os
import xml.etree.ElementTree as xml
import json


class Person(object):
    """__init__() functions as the class constructor"""

    def __init__(self, first_name, last_name, year, month, day, company, project, role, room, hobby):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.month = month
        self.day = day
        self.company = company
        self.project = project
        self.role = role
        self.room = room
        self.hobby = hobby


def dataFileProcessing(path_to_source_file, path_to_destination_file, data):
    if isFileExist(path_to_source_file):
        print("File exists")
        tree = xml.parse(path_to_source_file)
        root = tree.getroot()

        # changing fields text
        i = 0
        for item in root.findall('PERSON'):
            item.find('FIRST_NAME').text = data[i].first_name
            item.find('LAST_NAME').text = data[i].last_name
            item.find('YEAR_OF_BIRTH').text = data[i].year
            item.find('MONTH_OF_BIRTH').text = data[i].month
            item.find('DAY_OF_BIRTH').text = data[i].day
            item.find('COMPANY').text = data[i].company
            item.find('PROJECT').text = data[i].project
            item.find('ROLE').text = data[i].role
            item.find('ROOM').text = data[i].room
            item.find('HOBBY').text = data[i].hobby
            i += 1

        # write changes back to xml file
        tree.write(path_to_source_file)

        # convert xml to json
        obj = parseXmlToObj((xml.parse(path_to_source_file)).getroot())
        result = {'PERSONS': obj}
        with open(path_to_destination_file, "w") as write_file:
            json.dump(result, write_file, indent=4)
    else:
        print("File doesn't exist.")


def isFileExist(path_to_file):
    full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path_to_file)
    print(full_path)
    print(os.path.exists(full_path))
    return os.path.exists(full_path)


def parseXmlToObj(xml):
    items = []
    for child in list(xml):
        item = {}
        if len(list(child)) > 0:
            for element in list(child):
                item[element.tag] = element.text
        else:
            item[child.tag] = child.text or ''
        items.append(item)
    return items


def main():
    source_path = "samples/xml/test_data.xml"
    destination_path = "samples/json/updated_test_data.json"
    person_list = [Person("First1", "Last1", "2001", "Jan", "1", "company1", "project1", "role1", "room#1", "hobby1"),
                   Person("First2", "Last2", "2002", "Jan", "2", "company2", "project2", "role2", "room#2", "hobby2"),
                   Person("First3", "Last3", "2003", "Jan", "3", "company3", "project3", "role3", "room#3", "hobby3")]
    dataFileProcessing(source_path, destination_path, person_list)


if __name__ == "__main__":
    # calling main function
    main()
