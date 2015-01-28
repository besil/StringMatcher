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
        self.threshold = 10.0
    
    def windower(self, l):
        ''' Returns a list of couple of words in the document l '''
        for i in range(len(l)-1):
            j = i+1
            yield ( l[i], l[j] )
    
    def match_document(self, document):
        for ni, mj in self.correlation_map.keys():
            di = dj = self.threshold
            
            for chunk in self.windower(document):
                word = ' '.join(chunk)
                
                di = min( di, lev.distance( ni, word ) )
                dj = min( dj, lev.distance( mj, word ) )
                
            pi = 1 - (di / self.threshold)
            pj = 1 - (dj / self.threshold)
            
            self.correlation_map[ (ni, mj) ] = max( self.correlation_map[(ni,mj)], pi * pj )
    
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
        