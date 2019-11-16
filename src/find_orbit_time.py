'''
Separating code for SRP
'''
class Orbit:
    '''
    This class calculates the orbit time for the inputs given
    '''
    def __str__(self):
        '''
        Introduced to remove the pylint warning:
        Too few public methods (1/2) (too-few-public-methods)
        '''
        return self.__class__.__name__

    @staticmethod
    def get_orbit_time(vehicles, traffic_speed, orbit_distance, craters_count):
        '''
        :param vehicles: Based on Climate, gets the available vehicles
        :param traffic_speed: orbit traffic speed
        :param orbit_distance: orbit distance
        :param craters_count: Number of craters in particular orbit
        :return: [Vehicle Details,minimum Time takes to travel in Minutes, Craters change ]
        '''
        orbit_vehicles_time = []

        for i in vehicles[0]:
            if traffic_speed <= i['max_speed']:
                temp_speed = traffic_speed
            else:
                temp_speed = i['max_speed']
            temp = (orbit_distance + (vehicles[1] * craters_count)) \
                    * i['cross_crater_time'] + (60 / temp_speed) * orbit_distance
            orbit_vehicles_time.append(temp)

        return [vehicles[0][orbit_vehicles_time.index(min(orbit_vehicles_time))], \
                min(orbit_vehicles_time)]
