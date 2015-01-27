'''
Created on Jan 27, 2015

@author: besil
'''

from matcher import StringMatcher

if __name__ == '__main__':
    sm = StringMatcher()
    data = "data.txt"
    name_file = 'names.csv'
    
    for line in open(data, 'r'):
        print line
    
    for names in open( name_file, 'r' ):
        print names
    
    
    s1 = "ciao"
    s2 = "mondo"
    print sm.match( s1, s2 )