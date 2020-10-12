#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
from fractions import Fraction 

def extract_minutes(s):
    '''
    A helper function to extract total minutes from a string containing any number of minutes mentions
    
    Parameters
    ----------
    string : A string of text.
    
    Returns
    -------
    A floating point number if the string contains minutes and None otherwise.
    '''    
    total_min = 0
    try:
        # find any occurrences of hours
        for i in re.findall('[0-9]* minute',s):        
            i = i.strip('minute').rstrip().lstrip()
            # convert to float and sum accross all occurrences
            i = float(i)
            total_min += i
        return total_min
    except AttributeError:
        return 0

def extract_hours(s):
    '''
    A helper function to extract total hour from a string containing 0-1 hour mentions
    
    Parameters
    ----------
    string : A string of text.
    
    Returns
    -------
    A floating point number if the string contains hour mention and None otherwise.
    '''     
    try:
        # find any occurrences of hours
        x = re.search('[0-9 ]+[ /0-9]+(hour)',s).group(0).strip('hour').rstrip()      
        # convert any instances of fractions and entire number to float
        return float(sum(Fraction(term) for term in x.split()))
    
    except AttributeError:
        return 0