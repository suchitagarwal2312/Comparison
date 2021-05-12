#This small program proves how Numpy is much much faster than traditional python.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Let us store 10 lac elements indexed from 0 to 9,99,999 in a traditional python list.

my_list = list(range(1000000))


#Now we will store the same 10 lac elements in a Numpy Array and check which one is faster.

my_arr = np.array(range(1000000))

#Time taken by Traditional python list

%time for i in range(10): my_list2 = my_list * 2

#Time taken by Numpy array

%time for i in range(10): my_arr2 = my_arr * 2



#In ML, it is heavily recommended to use Numpy data structures in place of normal python data structures.


















































        
        
        
        
        
        
        
        
        








































