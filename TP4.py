# -*- coding: utf-8 -*-
"""
TP4
"""
def BuildDecisionTree (dataset, minimun):
    A = dataset[0].split(' ')
    B = dataset[1].split(' ')
    C = dataset[2].split(' ')
    for i in range(len(A)):
        A[i]=int(A[i])
        B[i]=int(B[i])
        C[i]=int(C[i])
    tree_out=GINI_min(A,B,C,minimun)
    return tree_out
    

def GINI(c1,c2):
    if c1==0 and c2==0:
        Gini=0
    else:
        Gini=1-(c1/(c1+c2))**2-(c2/(c1+c2))**2
    return Gini

def GINI_min(A,B,C,minimun):
    level=1
    count_positionA=[0,0]
# out store conditionA,conditionB,number of leaf,number of error
    out=[0,0,0,0]
    number_leaf=0
    error_number=0
# Start from A
    value_gini1=[0,0,0]
    value_gini2=[0,0,0]
    value_gini=[1,1,1]
    for i in range(max(A)):
        count_gini = [0, 0, 0, 0]
        for j in range(len(A)):
            if (A[j]<=i):
                if(C[j]==0):
                    count_gini[0] += 1
                else:
                    count_gini[1] += 1
            else:
                if (C[j] == 0):
                    count_gini[2] += 1
                else:
                    count_gini[3] += 1
        value_gini1[i] = GINI(count_gini[0],count_gini[1])
        value_gini2[i] = GINI(count_gini[2], count_gini[3])
        value_gini[i] = (value_gini1[i]*(count_gini[0]+count_gini[1]) + value_gini2[i]*(count_gini[2]+count_gini[3]))/(count_gini[0]+count_gini[1]+count_gini[2]+count_gini[3])
    count_positionA[1] = value_gini.index(min(value_gini))
    count_positionA[0] = min(value_gini)
    out[0]=value_gini.index(min(value_gini))
# print root
    print("Root")
    print("Level %i" %level)
    level+=1
    a=[]
    for i in range(count_positionA[1]+1):
        a.append(i)
    print("Feature A %i %i" %(count_positionA[1]-1,count_positionA[1]))
    print("Gini %s" %count_positionA[0])
    data_position1=[]
    c_number1=0
    data_position2=[]
    c_number2=0
    for j in range(len(A)):
        if (A[j] <= count_positionA[1]):
            data_position1.append(j)
            c_number1+=1
        else:
            data_position2.append(j)
            c_number2+=1
#print leaf
    if c_number1<=minimun:
        print("Leaf")
        number_leaf+=1
        print("Level %i" %level)
        c=0
        c1=0
        c2=0
        for i in range(c_number1):
            if (C[data_position1[i]] == 0):
                c1 += 1
            else:
                c2 += 1
        c=GINI(c1,c2)    
        print("Gini %s" %c)
# intermediate
    else:
        count_positionB=[0,0]
        value_gini1=[0,0,0]
        value_gini2=[0,0,0]
        value_gini=[1,1,1]
        for i in range(max(B)):
            count_gini = [0, 0, 0, 0]
            for j in range(c_number1):
                if (B[data_position1[j]]<=i):
                    if (C[data_position1[j]] == 0):
                        count_gini[0] += 1
                    else:
                        count_gini[1] += 1
                else:
                    if (C[data_position1[j]] == 0):
                        count_gini[2] += 1
                    else:
                        count_gini[3] += 1
            value_gini1[i] = GINI(count_gini[0],count_gini[1])
            value_gini2[i] = GINI(count_gini[2], count_gini[3])
            value_gini[i] = (value_gini1[i]*(count_gini[0]+count_gini[1]) + value_gini2[i]*(count_gini[2]+count_gini[3]))/(count_gini[0]+count_gini[1]+count_gini[2]+count_gini[3])
        count_positionB[1] = value_gini.index(min(value_gini))
        count_positionB[0] = min(value_gini)
        out[1]=value_gini.index(min(value_gini))
        print("Intermediate")
        print("Level %i" %level)
        print("Feature B %i" %(count_positionB[1]))
        print("Gini %s" %count_positionB[0])       
    if c_number2<=minimun:
        print("Leaf")
        number_leaf+=1
        print("Level %i" %level)
        level+=1
        c=0
        c1=0
        c2=0
        for i in range(c_number2):
            if (C[data_position2[i]] == 0):
                c1 += 1
            else:
                c2 += 1
        c=GINI(c1,c2)  
        print("Gini %s" %c)
        if c!=0:
            error_number+=min(c1,c2)
    else:
        count_positionB=[0,0]
        value_gini1=[0,0,0]
        value_gini2=[0,0,0]
        value_gini=[1,1,1]
        for i in range(max(B)):
            count_gini = [0, 0, 0, 0]
            for j in range(c_number2):
                if (B[data_position2[j]]<=i):
                    if (C[data_position2[j]] == 0):
                        count_gini[0] += 1
                    else:
                        count_gini[1] += 1
                else:
                    if (C[data_position2[j]] == 0):
                        count_gini[2] += 1
                    else:
                        count_gini[3] += 1
            value_gini1[i] = GINI(count_gini[0],count_gini[1])
            value_gini2[i] = GINI(count_gini[2], count_gini[3])
            value_gini[i] = (value_gini1[i]*(count_gini[0]+count_gini[1]) + value_gini2[i]*(count_gini[2]+count_gini[3]))/(count_gini[0]+count_gini[1]+count_gini[2]+count_gini[3])
        count_positionB[1] = value_gini.index(min(value_gini))
        count_positionB[0] = min(value_gini)
        print("Intermediate")
        print("level %i" %level)
        level+=1
        print("Feature B <= %i" %(count_positionB[1]))
        print("Gini %s" %count_positionB[0])
# leaf
    count_gini=[0,0,0,0]
    c_2=0
    c_3=0
    for j in range(c_number1):
        if (B[data_position1[j]]<=count_positionB[1]):
            if (C[data_position1[j]] == 0):
                count_gini[0] += 1
            else:
                count_gini[1] += 1
        else:
            if (C[data_position1[j]] == 0):
                count_gini[2] += 1
            else:
                count_gini[3] += 1
    c_2=GINI(count_gini[0],count_gini[1])
# compute the number of train error
    if c_2!=0:
            error_number+=min(count_gini[0],count_gini[1])
    c_3=GINI(count_gini[2],count_gini[3])
    if c_3!=0:
            error_number+=min(count_gini[2],count_gini[3])
    print("Leaf")
    number_leaf+=1
    print("Level %i" %level)
    print("Gini %s" %c_2)
    print("Leaf")
    number_leaf+=1
    print("Level %i" %level)
    print("Gini %s" %c_3)
    out[2]=number_leaf
    out[3]=error_number
    return(out)


def prune_tree(tree, a,minNUM):
    return 0




f=open(r"C:\Users\Administrator\Desktop\Telecom\课件\SD\SD201\TP\TP4\tree.txt") 
dataset = f.read().split('\n',2)
BuildDecisionTree(dataset,3)
