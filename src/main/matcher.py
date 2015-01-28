'''
Created on Jan 27, 2015

@author: besil
'''

import Levenshtein as lev  # @UnresolvedImport
import string
import math

class StringMatcher(object):
    '''
    A simple wrapper to Levenshtein module
    '''
    def __init__(self ):
        self.correlation_map = dict()
        self.presence = dict()
    
    def windower(self, l):
        ''' Returns a list of couple of words in the document l '''
        for i in range(len(l)-1):
            j = i+1
            yield ( l[i], l[j] )
    
    def search_name(self, person, document):
        name  = lambda p : p.split(" ")[0]
        sname = lambda p : p.split(" ")[1]
        
        max_p = 0
        for chunk in self.windower(document):
            cname   = chunk[0]
            csname  = chunk[1]
            
            c_d_name  = self.match( name(person), cname )
            c_d_sname = self.match( sname(person), csname )
            
            pname   = 1 - ( float(c_d_name) / max(len(cname), len(name(person))) )
            psname  = 1 - ( float(c_d_sname) / max(len(csname), len(sname(person))) )
            
            f = lambda x : math.e ** x
            
            p = f( pname * psname )
            
            max_p = p if p > max_p else max_p
            
        return max_p
    
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
        