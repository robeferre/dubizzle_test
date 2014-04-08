# -*- encoding: utf-8 -*-
import os
import json
from pprint import pprint


class Mars(object):

    def __init__(self):
        """
        - Mars constructor
        """
        #Json File Paths
        self.path_to_json_file = os.path.dirname(__file__)+"/mars.json"
        self.path_to_new_json = os.path.dirname(__file__)+"/json_file_created/"

    def send(self, py_dict, file_name):
        """
        - (over)writes a JSON object to a file.
        - Takes in one argument of type dict.
        - Returns 1 on success. Raises a general exception on error.
        """
        if isinstance(py_dict, dict):
            path = self.path_to_new_json + str(file_name)
            with open(path, 'wb') as fp:
                json.dump(py_dict, fp)
            return 1
        else:
            raise Exception("First argument must be a dict type!")

    def receive(self):
        """
       - reads a JSON object from a file. Returns a dict on success.
       - Raises a general exception on error.
        """
        with open(self.path_to_json_file) as data_file:
            json_to_dict = json.load(data_file)

        if isinstance(json_to_dict, dict):
            return json_to_dict
        else:
            raise Exception("Errors found at the json file to import!")

    def earth_dict_generator(self):
        """
        - Returns an earth dict just for testing propose.
        - it is better readable at the json file created
        - some pep8 issues regarding line size
        """
        earth_dict = {u'earth': {u'Atmosphere':
                                 {u'pressure': u'1,013 millibars(at sea level)',
                                  u'composition': [u'Nitrogen',
                                                   u'Oxygen',
                                                   u'Argon',
                                                   u'Carbon dioxide']},
                                 u'Deepest Canyon': u'Grand Canyon',
                                 u'description': u'Describe Earth planet attributes', u'length_of_day':
                                 u'Just slightly under 24 hours',
                                 u'Distance from Sun': u'149,597,891 kilometers',
                                 u'equatorial_radius': u'6,378 kilometers',
                                 u'gravity': u'2.66 times that of Mars',
                                 u'polar_caps': u'Permanently covered with water ice',
                                 u'surface_temperature': u'57 degrees F (14 degrees C)',
                                 u'length_of_Year': u'365 days',
                                 u'largest_volcano': u'Mauna Loa (Hawaii)'}}

        return earth_dict

    def test_method(self):
        """
        - It is a test function.
        """
        # Starting tests
        print 115*'#'
        print "# TESTING receive() method"

        # Calling receive method
        print "# READING contend of %s file" % (self.path_to_json_file)
        print 115*'#'
        received_data_from_json_file = mars_obj.receive()
        print "# Contend of %s stored in a python dictionary" % (self.path_to_json_file)
        print "# Here's the contend of the python dict."
        print 115*'#'
        pprint(received_data_from_json_file)
        print 115*'#'

        # Calling send method
        print "# TESTING send() method"
        print "# Loading the earth_dict contend from \"earth_dict_generator\" method"
        print 115*'#'

        # Creating  earth_dict
        earth_dict = mars_obj.earth_dict_generator()
        
        
        print '# Sending earth_dict to a json file on %s' % (self.path_to_new_json)

        # Sending dict to a json file
        filename = self.path_to_new_json + "earth.json"
        if mars_obj.send(earth_dict, 'earth.json') == 1:
            print '# FILE SAVED AT: %s' % (filename)
            print 115*'#'
            pprint(earth_dict)
            print 115*'#'
        print "# END OF TESTS"
        print 115*'#'


if __name__ == '__main__':
    # Mars obj
    mars_obj = Mars()
    # Running tests
    mars_obj.test_method()
