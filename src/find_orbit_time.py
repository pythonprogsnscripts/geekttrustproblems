'''
Separating code for SRP
'''
def get_orbit_time(vehicles, traffic_speed, orbit_distance, craters_count):
    '''
     :param vehicles: Based on Climate, gets the available vehicles
     :param traffic_speed: orbit traffic speed
     :param orbit_distance: orbit distance
     :param craters_count: Number of craters in particular orbit
     :return: [Vehicle Details,minimum Time takes to travel in Minutes, Craters change ]
     '''
    orbit_1_vehicles_time = []

    for i in vehicles[0]:
        if traffic_speed <= i['max_speed']:
            temp_speed = traffic_speed
        else:
            temp_speed = i['max_speed']
        temp = (orbit_distance + (vehicles[1] * craters_count)) \
                * i['cross_crater_time'] + (60 / temp_speed) * orbit_distance
        orbit_1_vehicles_time.append(temp)

    return [vehicles[0][orbit_1_vehicles_time.index(min(orbit_1_vehicles_time))], \
            min(orbit_1_vehicles_time)]
