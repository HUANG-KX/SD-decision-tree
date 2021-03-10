# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 15:07:51 2019

@author: Administrator
"""

for j in len(A):
        i=0
        k=0
        if (A[j] <= count_position[0]):
            if (C[j] == 0):
                data_position1[i]= j
                i+=1
            else:
                data_position2[k] = j
                k+=1
# Start from B
    value_gini1=[0,0,0]
    value_gini2=[0,0,0]
    value_gini=[0,0,0]
    for i in range(max(B)):
        count_gini = [0, 0, 0, 0]
        for j in range(len(B)):
            if (B[j]<=i):
                if(C[j]==0):
                    count_gini[0]+=1
                else:
                    count_gini[1]+=1
            else:
                if (C[j] == 0):
                    count_gini[2] += 1
                else:
                    count_gini[3] += 1
        value_gini1[i] = GINI(count_gini[0],count_gini[1])
        value_gini2[i] = GINI(count_gini[2], count_gini[3])
        value_gini[i] = value_gini1[i] + value_gini2[i]
    count_position[3] = value_gini.index(min(value_gini))
    count_position[2] = min(value_gini)