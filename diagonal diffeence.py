#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    n = len(arr)
    left_diagonal =0
    right_diagonal =0
    # Write your code here
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                left_diagonal = left_diagonal+ arr[i][j]
    j= n-1
    i =0
    
    while (i<n):
        right_diagonal = right_diagonal + arr[i][j]
        i = i+1
        j = j-1
    
    diagonaldifference=abs(left_diagonal-right_diagonal)
    return diagonaldifference
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
