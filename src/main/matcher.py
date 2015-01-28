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
        self.correlation_map = dict()
    
    def match_name(self, chunk):
        new_name = ' '.join(chunk)
        rev_new_name = ' '.join(chunk[::-1])
    
    def match(self, s1, s2):
        return lev.distance(s1, s2)
    
    def read_names(self, name_file):
        for line in open(name_file):
            split = line.lower().strip().split(",")
            first = split[0]
            second = split[1]
            self.correlation_map[ (first, second) ] = 0
        return self.correlation_map
    
    def read(self, data):
        ''' NON ORA '''
        text = ''.join( [ x.lower() for x in open( data, 'r' ).readlines() ] ).replace("\n", " ")
        return text.translate(string.maketrans("",""), string.punctuation).split(" ")
        