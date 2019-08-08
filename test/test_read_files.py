'''
Unit testing of read_file using PyTest framework
'''
from geektrust.src.read_files import JSON_FILES as file, VEHICLE_DATA as vehicle_data

def test_if_count_of_json_files_is_two():
    '''
    Check if count of JSON files in the input data
    directory is matching
    '''
    assert len(file) == 2

def test_in_vehicle_file_bus_is_not_found():
    '''
    Check if correct keys are available in vehicle data file
    '''
    assert 'bus' not in vehicle_data.keys()
