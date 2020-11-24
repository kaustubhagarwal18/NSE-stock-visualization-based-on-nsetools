from nsetools import Nse
from pprint import pprint                                
import numpy as np
import time
#import pandas as pd
import matplotlib.pyplot as plt

nse = Nse()                                 # make an object 
q = nse.get_quote('lti')                    # dictionary!
print(q.get('averagePrice'))                # focusing on this key value pair in the dict for now

a = np.zeros(10)                            # to store last 10 values
print(a)
for i in range(10):                         # stupid loop
    a[i] = nse.get_quote('lti').get(('averagePrice'))
    #time.sleep(1)
print(a)                                    # update numpy array    (very inefficient)
plt.plot(a)                                 
plt.show()                                  # line graph

pprint(q)                                   # prints all data
