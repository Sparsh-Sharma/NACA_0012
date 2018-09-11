# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:38:11 2018

@author: WS1
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:30:51 2018

@author: WS2
"""

#import time                                                
import numpy as np                                         
import numba     
from numba import njit, prange  

@njit(parallel=True)
def two_d_array_reduction_prod(n):
    shp = (13, 17)
    result1 = 2 * np.ones(shp, np.int_)
    tmp = 2 * np.ones_like(result1)
    for i in numba.prange(n):
            result1 *= tmp
    return result1                                       

Z = two_d_array_reduction_prod(10000000000000000)
print (Z)

#SIZE = 2147483648 * 6                                      
#
#a = np.full(SIZE, 1, dtype = np.int32)                     
#
#b = np.full(SIZE, 1, dtype = np.int32)                     
#
#c = np.ndarray(SIZE, dtype = np.int32)                     
#
#@numba.jit(nopython = True, parallel = True, nogil = True) 
#def add(a, b, c):                                          
#    for i in prange(SIZE):                                  
#        c[i] = a[i] + b[i]                                 
#
#start = time.time()                                        
#add(a, b, c)                                               
#end = time.time()                                          
#
#print(end - start) 