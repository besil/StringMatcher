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
        self.presence = dict()
        self.threshold = 10.0
    
    def windower(self, l):
        ''' Returns a list of couple of words in the document l '''
        for i in range(len(l)-1):
            j = i+1
            yield ( l[i], l[j] )
    
    def search_name(self, person, document):
        di = self.threshold
        for chunk in self.windower(document):
            word = ' '.join(chunk)
            rev_word = ' '.join(chunk[::-1])
            
            di = min( di, self.match( person, word ), self.match( person, rev_word ) )
            
            if di == 0: break
                
        pi = 1 - (di / self.threshold)
        return pi
    
    def match_document(self, document):
        for ni, mj in self.correlation_map.keys():
            pi = self.search_name(ni, document)
            pj = self.search_name(mj, document)
            
            self.presence[ni] = pi
            self.presence[mj] = pj
            
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
        ''' Read a document from file. TODO: read from MongoDB '''
        text = ''.join( [ x.lower() for x in open( data, 'r' ).readlines() ] ).replace("\n", " ")
        return text.translate(string.maketrans("",""), string.punctuation).split(" ")
        