Here's some information about my implementation of the programing questions.

Dependencies
------------

	- exercise 3a 
		* hash_ring
		
	- exercise 3b
		* random
		
	- exercise 3c
		* os
		* json
		* pprint

Usage
-----

	- exercise 3a 
		* python new__memcached.py
		
	- exercise 3b
		* python exercice3b.py
		
	- exercise 3c
		* python exercice3b.py (navigate to exercise3C_Mars folder)



EXERCISE 3A OUTPUT
-------------------

	#######################################################
	-> Here's our 7 servers:
	#######################################################
	# 127.0.0.1:11211 => Node_Ring_Position:197
	# 127.0.0.1:11212 => Node_Ring_Position:609
	# 127.0.0.1:11213 => Node_Ring_Position:379
	# 127.0.0.1:11214 => Node_Ring_Position:357
	# 127.0.0.1:11215 => Node_Ring_Position:683
	# 127.0.0.1:11216 => Node_Ring_Position:127
	# 127.0.0.1:11217 => Node_Ring_Position:293
	#######################################################
	100.0 percent of keys matched
	#######################################################
	Added new server
	#######################################################
	-> Here's our 11 servers:
	#######################################################
	# 127.0.0.1:11211 => Node_Ring_Position:197
	# 127.0.0.1:11212 => Node_Ring_Position:609
	# 127.0.0.1:11213 => Node_Ring_Position:379
	# 127.0.0.1:11214 => Node_Ring_Position:357
	# 127.0.0.1:11215 => Node_Ring_Position:683
	# 127.0.0.1:11216 => Node_Ring_Position:127
	# 127.0.0.1:11217 => Node_Ring_Position:293
	# 127.0.0.1:11218 => Node_Ring_Position:370
	# 127.0.0.1:11219 => Node_Ring_Position:517
	# 127.0.0.1:11220 => Node_Ring_Position:737
	# 127.0.0.1:11221 => Node_Ring_Position:648
	#######################################################
	100.0 percent of keys stil matched
	#######################################################



EXERCISE 3B OUTPUT
------------------

	#############################
	Random number generated: 2
	Function returns: 2
	#############################



EXERCISE 3C OUTPUT
--------------------

	###################################################################################################################
	# TESTING receive() method
	# READING contend of /home/rfjunior/workspace/dubizzle_test/exercise3C_Mars/mars.json file
	###################################################################################################################
	# Contend of /home/rfjunior/workspace/dubizzle_test/exercise3C_Mars/mars.json stored in a python dictionary
	# Here's the contend of the python dict.
	###################################################################################################################
	{u'mars': {u'Atmosphere': {u'composition': [u'Carbon dioxide',
	                                            u'Nitrogen',
	                                            u'Argon',
	                                            u'Oxygen',
	                                            u'Water vapor',
	                                            u'Nitric oxide'],
	                           u'pressure': u'7.5 millibars (average)'},
	           u'Deepest Canyon': u'Valles Marineris',
	           u'Distance from Sun': u'227,936,637 kilometers',
	           u'description': u'Describe Mars planet attributes',
	           u'equatorial_radius': u'3,397 kilometers',
	           u'gravity': u'0.375 that of Earth',
	           u'largest_volcano': u'Olympus Mons',
	           u'length_of_Year': u'687 Earth days',
	           u'length_of_day': u'24 hours, 37 minutes',
	           u'polar_caps': u'Covered with a mixture of carbon dioxide ice and water ice',
	           u'surface_temperature': u'-81 degrees F (-63 degrees C)'}}
	###################################################################################################################
	# TESTING send() method
	# Loading the earth_dict contend from "earth_dict_generator" method
	###################################################################################################################
	{u'earth': {u'Atmosphere': {u'composition': [u'Nitrogen',
	                                             u'Oxygen',
	                                             u'Argon',
	                                             u'Carbon dioxide'],
	                            u'pressure': u'1,013 millibars(at sea level)'},
	            u'Deepest Canyon': u'Grand Canyon',
	            u'Distance from Sun': u'149,597,891 kilometers',
	            u'description': u'Describe Earth planet attributes',
	            u'equatorial_radius': u'6,378 kilometers',
	            u'gravity': u'2.66 times that of Mars',
	            u'largest_volcano': u'Mauna Loa (Hawaii)',
	            u'length_of_Year': u'365 days',
	            u'length_of_day': u'Just slightly under 24 hours',
	            u'polar_caps': u'Permanently covered with water ice',
	            u'surface_temperature': u'57 degrees F (14 degrees C)'}}
	###################################################################################################################
	# Sending earth_dict to a json file on /home/rfjunior/workspace/dubizzle_test/exercise3C_Mars/json_file_created/
	# FILE SAVED AT: /home/rfjunior/workspace/dubizzle_test/exercise3C_Mars/json_file_created/earth.json
	###################################################################################################################
	# END OF TESTS
	###################################################################################################################









