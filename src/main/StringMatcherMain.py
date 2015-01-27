'''
Created on Jan 27, 2015

@author: besil
'''

from matcher import StringMatcher

if __name__ == '__main__':
    sm = StringMatcher()
    fname = "data.csv"
    
    
    
    s1 = "ciao"
    s2 = "mondo"
    print sm.match( s1, s2 )