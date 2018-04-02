# Create dummy indicators for the presence of search terms in a Python data frame. 

import pandas as pd
import numpy as np

# Set seed
np.random.seed(3141)

# Create random 3x3 matrix.
k = 5
a = np.matrix([np.random.binomial(k,0.5,3),np.random.binomial(k,0.5,3),np.random.binomial(k,0.5,3)] )
print(a)

# Create data frame from matrix. 
a = pd.DataFrame(data = a)
a.columns = ['a', 'b', 'c']

# Create list of integers to search for. 
ls = [1,2,3,4,5]

# Create dummy indicators for presence of list items in column a.
for l in ls:
    a[l] = a['a'].apply(lambda x: 1 if l == x else 0)

print(a)



