# -*- encoding: utf-8 -*-

"""
#-------------------------------------------------------------------------------------------------------------------
# EXERCICE 3b - Returning a random numbem between 1 and 7 
#
# Author: Roberto Ferreira Junior (roberto.junior@keyrus.com.br)
#

b) Given a function that returns a random integer number between 1 and 5, create a
function that creates a random integer between 1 and 7.
Use any language, or write in pseudo code.Â 

#
# History:
# 04/07/2014 - Version 1.0
#-------------------------------------------------------------------------------------------------------------------
"""

import random

def random_range():
    """
    This function returns a randon number between 1 and 7
    """
    rnd = int(random.randrange(1,8))
    print "Random number generated: %s" %(rnd)
    return rnd

def run():
    rnd=random_range()
    print "Function returns: %s" %(rnd)
    
print 29*'*'
for i in range(1,15):
    run()
    print 29*'*'
