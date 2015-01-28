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
        name  = lambda p : p.split(" ")[0]
        sname = lambda p : p.split(" ")[1]
        
        min_d_name = min_d_sname = self.threshold
        min_w_name = min_w_sname = ""
        max_p = 0
        for chunk in self.windower(document):
            cname   = chunk[0]
            csname  = chunk[1]
            
            c_d_name  = self.match( name(person), cname )
            c_d_sname = self.match( sname(person), csname )
            
            pname   = 1 - ( float(c_d_name) / max(len(cname), len(name(person))) )
            psname  = 1 - ( float(c_d_sname) / max(len(csname), len(sname(person))) )
            
            p = 0.1 * pname + 0.9 * psname
            p = pname * psname
            
            if p > max_p:
                if "mazzicone" in person:
                    print "*** {} ***".format(person)
                    print "Name: {} -> {} = {}".format(name(person), cname, pname)
                    print "Surname: {} -> {} = {}".format( sname(person), csname, psname )
                    print "Total prob: {} -> {}".format(max_p, p)
                max_p = p
            
#             if c_d_name < min_d_name and c_d_sname < min_d_sname:
#                 min_d_name = c_d_name
#                 min_d_sname = c_d_sname
#                 min_w_name = cname
#                 min_w_sname = csname
#                 
#                 if "mazzicone" in person:
#                     print "*** {} ***".format(person)
#                     print "Name: {} -> {} = {}".format(name(person), cname, c_d_name)
#                     print "Surname: {} -> {} = {}".format( sname(person), csname, c_d_sname )
                
        
#         pname   = 1 - ( float(min_d_name) / max(len(min_w_name), len(name(person))) )
#         psname  = 1 - ( float(min_d_sname) / max(len(min_w_sname), len(sname(person))) )
#         
#         p = 0.3 * pname + 0.7 * psname
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
        