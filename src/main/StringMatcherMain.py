'''
Created on Jan 27, 2015

@author: besil
'''

from matcher import StringMatcher

if __name__ == '__main__':
    sm = StringMatcher()
    data = "data.txt"
    name_file = 'names.csv'
    
    text = sm.read( data )
    print text
    
    s1 = "ciao"
    s2 = "mondo"
    print sm.match( s1, s2 )