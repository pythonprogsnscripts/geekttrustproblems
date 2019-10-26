import sys, os
sys.path.append(os.path.dirname(__file__)+"/../")
# from src.read_files import orbit_data as odata
from src.read_files import ORBIT_DATA as odata

class Orbit():
    '''
    This Orbit class creates Orbit object/instances with attributes of its route name, distance between
    start & end point, and the number of craters in the orbit route. 
    '''

    def __init__(self):
        pass

    def setOrbit(self, route_name, distance, craters, traffic_speed, point_one, point_two):
        '''
        This object function initializes the attributes of an Orbit object
        '''
        self.route_name = route_name
        self.distance = distance
        self.craters = craters
        self.traffic_speed = traffic_speed
        self.point_one = point_one
        self.point_two = point_two
        return

    def defineOrbit(self, route_name, orbit_speed, orbit_datafile):
        '''
        This object function initializes the attributes of an Orbit object. It takes
        in an user input of speed of an orbit and uses the passed on module defined values
        of the name of the Orbit and the datafile location, and creates an orbit object.
        '''
        import json
        for eachOrbit in odata:
            if odata[eachOrbit]['route'] == route_name:
                odata[eachOrbit]['traffic_speed'] = orbit_speed
                with open(orbit_datafile,'w') as temp:
                    json.dump(odata,temp)
                    self.setOrbit(odata[eachOrbit]['route']
                                 , odata[eachOrbit]['distance']
                                 , odata[eachOrbit]['craters']
                                 , odata[eachOrbit]['traffic_speed']
                                 , odata[eachOrbit]['point_one']
                                 , odata[eachOrbit]['point_two']
                                  )
        return self