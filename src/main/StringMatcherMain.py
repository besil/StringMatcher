'''
Created on Jan 27, 2015

@author: besil
'''

from matcher import StringMatcher
from pprint import pprint

def windower(l):
    for i in range(len(l)-1):
        j = i+1
        yield ( l[i], l[j] )

if __name__ == '__main__':
    sm = StringMatcher()
    data = "data.txt"
    name_file = 'names.csv'
    
    names = sm.read_names(name_file)
    pprint(names)
    document = sm.read( data )
    print document
    
    for chunk in windower(document):
        sm.match_name(chunk)
    
    