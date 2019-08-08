'''
This program uses pytest framework for unit testing
'''
from geektrust.src.read_files import VEHICLE_DATA as vehicle_data, JSON_FILES as file

def test_when_checking_number_of_json_files_itshouldbetwo():
    '''
    This test check the number of JSON file in the directory
    '''
    assert len(file) == 2

def test_when_vehicle_file_should_not_have_bus():
    '''
    This test will check for an invalid key
    '''
    assert 'bus' not in vehicle_data.keys()
