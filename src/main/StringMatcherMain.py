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
    
    
    