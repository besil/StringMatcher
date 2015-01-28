'''
Created on Jan 27, 2015

@author: besil
'''

from matcher import StringMatcher
from pprint import pprint

if __name__ == '__main__':
    sm = StringMatcher()
    data = "data.txt"
    name_file = 'names.csv'
    
    names = sm.read_names(name_file)
    pprint(names)
    document = sm.read( data )
    print document
    
    sm.match_document( document )
    
    pprint( sm.correlation_map )
    pprint( sm.presence )
    
    
#                 p1 = chunk[0]
#                 p2 = chunk[1]
#                 diname       = min( di, self.match( self.name(ni), p1 ), self.match(self.name(ni), p2) )
#                 disurname    = min( di, self.match( self.surname(ni), p1 ), self.match(self.surname(ni), p2) )
#                 djname       = min( dj, self.match( self.name(mj), p1 ), self.match(self.name(mj), p2) )
#                 djsurname    = min( dj, self.match( self.surname(mj), p1 ), self.match(self.surname(mj), p2) )
#                 ditot = diname + disurname + 1
#                 djtot = djname + djsurname + 1
#                 di = 0.3*( diname/ditot ) + 0.7 * ( disurname / ditot )
#                 dj = 0.3*( djname/djtot ) + 0.7 * ( djsurname / djtot )
    
    