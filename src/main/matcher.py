'''
Created on Jan 27, 2015

@author: besil
'''

import Levenshtein as lev  # @UnresolvedImport

class StringMatcher(object):
    '''
    A simple wrapper to Levenshtein module
    '''


    def __init__(self ):
        pass
    
    def match(self, s1, s2):
        return lev.distance(s1, s2)