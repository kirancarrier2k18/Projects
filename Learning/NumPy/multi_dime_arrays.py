import numpy as np

x=np.array([[1,2,3,4],[5,6,7,8],[100,101,102,103]])

print(x)
print("No of axes: ",x.ndim) # no of dimensions
print("No of Size: ",x.size) #Total number of elements
print("No of Shape: ",x.shape) # (Rows,Columns)
print("No of Rows: ",x.shape[0]) #Rows
print("No of Rows: ",x.shape[1]) #Columns
print("Item size in bytes: ",x.itemsize)

