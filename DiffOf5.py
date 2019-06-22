#!/usr/bin/python3

import numpy as np

arr=np.empty([8,2])
no=101
for i in range(8):
 for j in range(2):
  arr[i][j]=no
  no=arr[i][j]+5

print(arr)

