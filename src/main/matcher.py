'''
Created on Jan 27, 2015

@author: besil
'''

import Levenshtein as lev  # @UnresolvedImport
import string

class StringMatcher(object):
    '''
    A simple wrapper to Levenshtein module
    '''


    def __init__(self ):
        pass
    
    def match(self, s1, s2):
        return lev.distance(s1, s2)
    
    def read(self, data):
        text = ''.join( [ x.lower() for x in open( data, 'r' ).readlines() ] ).replace("\n", " ")
        return text.translate(string.maketrans("",""), string.punctuation).split(" ")
        