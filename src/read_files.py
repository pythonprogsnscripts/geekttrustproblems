import json
import os
json_files = os.listdir('inputdata')

def read_json_data(json_file):
    with open('inputdata/'+json_file,'r') as file:
        return json.load(file)

# file_name = json_file.strip().split('.')[0]
orbit_data = read_json_data(json_files[0])
vehical_data = read_json_data(json_files[1])