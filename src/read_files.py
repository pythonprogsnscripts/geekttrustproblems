'''
This module reads JSON files and acts as a
placeholder for the data
'''

import json
import os

JSON_FILES = os.listdir('inputdata')

def read_json_data(json_file):
    '''
        :param json_file: the input json file
    '''
    with open('inputdata/'+json_file, 'r') as file:
        return json.load(file)

# file_name = json_file.strip().split('.')[0]
ORBIT_DATA = read_json_data(JSON_FILES[0])
VEHICLE_DATA = read_json_data(JSON_FILES[1])
