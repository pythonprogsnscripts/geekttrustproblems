'''
Separating code for SRP
'''
def validate_input_data(input_data):
    '''
    This function validates the climate input.
    If user pass values other the 'Sunny', 'Rainy' or
    'Windy' this function will return False boolean value
        :param climate: Climate
        :return : True or False
    '''
    if input_data not in ['Sunny', 'Rainy', 'Windy']:
        print('Invalid climate input')
        return False
    return True
