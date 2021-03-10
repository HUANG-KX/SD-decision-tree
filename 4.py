# -*- coding: utf-8 -*-
"""
TP4
"""
import math

def BuildDecisionTree (dataset, minimun):
    A = dataset[0].split(' ')
    B = dataset[1].split(' ')
    C = dataset[2].split(' ')
    for i in range(len(A)):
        A[i]=int(A[i])
        B[i]=int(B[i])
        C[i]=int(C[i])
    tree_out=Inforamation_gain_max(A,B,C,minimun)
    print_tree(tree_out)
    return tree_out

def GINI(c1,c2):
    if c1==0 and c2==0:
        Gini=0
    else:
        Gini=1-(c1/(c1+c2))**2-(c2/(c1+c2))**2
    return Gini

def entropy(c1,c2):
    if c1==0 or c2==0:
        entropy1=0
    else:
        p1=c1/(c1+c2)
        p2=c2/(c1+c2)
        entropy1=-(p1)*math.log2(p1)-(p2)*math.log2(p2)
    return entropy1

#calcul the tree depend on max information_gain
def Inforamation_gain_max(A,B,C,minimun):
    A_spilt=Inforamation_gain(A,C,minimun)
    count=A_spilt[2]
    B1=[0 for i in range(count[0]+count[1])]
    C1=[0 for i in range(count[0]+count[1])]
    B2=[0 for i in range(count[2]+count[3])]
    C2=[0 for i in range(count[2]+count[3])]
    j=0
    k=0
    for i in range(len(A)):
        if (A[i] <= A_spilt[1]):
            B1[j]=B[i]
            C1[j]=C[i]
            j+=1
        else:
            B2[k]=B[i]
            C2[k]=C[i]
            k+=1
    B_1spilt=Inforamation_gain(B1,C1,minimun)
    B_2spilt=Inforamation_gain(B2,C2,minimun)
    output=[[0,0,[0,0,0,0]] for i in range(3)]
    output[0]=A_spilt
    output[1]=B_1spilt
    output[2]=B_2spilt
    return output

#calcul max information_gain    
def Inforamation_gain(D,C,minimun):
    for i in range(max(D)):
        count = [[0, 0, 0, 0] for i in range(max(D))]
        Info_gain=[0 for i in range(max(D))]
        a=[0 for i in range(max(D))]
        for i in range(max(D)):
            for j in range(len(D)):
                if (D[j]<=i):
                    if(C[j]==0):
                        count[i][0] += 1
                    else:
                        count[i][1] += 1
                else:
                    if (C[j] == 0):
                        count[i][2] += 1
                    else:
                        count[i][3] += 1
            a[i]=count[i][0]+count[i][1]+count[i][2]+count[i][3]
            Info_gain[i]=entropy(count[i][0]+count[i][2],count[i][1]+count[i][3])-(count[i][0]+count[i][1])*entropy(count[i][0],count[i][1])/a[i]-(count[i][2]+count[i][3])*entropy(count[i][2],count[i][3])/a[i]
    c_position = Info_gain.index(max(Info_gain))
    if count[c_position][0]+count[c_position][1]<minimun or count[c_position][2]+count[c_position][3]<minimun:
        Info_gain[c_position]=0
        count[c_position]=[0,0,0,0]
        c_position = Info_gain.index(max(Info_gain))
        if count[c_position][0]+count[c_position][1]<minimun or count[c_position][2]+count[c_position][3]<minimun:
            Info_gain[c_position]=0
            count[c_position]=[0,0,0,0]
            c_position = Info_gain.index(max(Info_gain))
            if count[c_position][0]+count[c_position][1]<minimun or count[c_position][2]+count[c_position][3]<minimun:
                Info_gain[c_position]=0
                count[c_position]=[0,0,0,0]
                c_position = Info_gain.index(max(Info_gain))
    c_value = max(Info_gain)
    output=[0,0,[0,0,0,0]]
    output[0]=c_value
    output[1]=c_position
    output[2]=count[c_position]
    
    return output

def print_tree(tree_1):
    level=1
    A=tree_1[0]
    B1=tree_1[1]
    B2=tree_1[2]
    print("Root")
    print("Level %i" %level)
    level+=1
    if A[1]==0:
        print("Feature A %i " %A[1])
    elif A[1]==1:
        print("Feature A %i %i " %(A[1]-1,A[1]))
    elif A[1]==2:
        print("Feature A %i %i %i" %(A[1]-2,A[1]-1,A[1]))
    print("Information gain %s" %A[0])
# leaf
    if B1!=[0,0,[0,0,0,0]]:
        print("Intermediate")
        print("Level %i" %level)
        if B1[1]==0:
            print("Feature B %i " %B1[1])
        elif A[1]==1:
            print("Feature B %i %i " %(B1[1]-1,B1[1]))
        elif A[1]==2:
            print("Feature B %i %i %i" %(B1[1]-2,B1[1]-1,B1[1]))
        print("Information gain %s" %B1[0])
    else:
        print("Leaf")
        print("Level %i" %level)
        print("Feature B")
        print("Information gain %s" %0)
    if B2!=[0,0,[0,0,0,0]]:
        print("Intermediate")
        print("Level %i" %level)
        if B2[1]==0:
            print("Feature B %i " %B2[1])
        elif A[1]==1:
            print("Feature B %i %i " %(B2[1]-1,B2[1]))
        elif A[1]==2:
            print("Feature B %i %i %i" %(B2[1]-2,B2[1]-1,B2[1]))
        print("Information gain %s" %B2[0])
    else:
        print("Leaf")
        print("Level %i" %level)
        print("Feature B")
        print("Information gain %s" %0)
    level+=1
    if B1!=[0,0,[0,0,0,0]]:
        print("Leaf")
        print("Level %i" %level)
        print("Information gain %s" %0)
        print("Leaf")
        print("Level %i" %level)
        print("Information gain %s" %0)
    return 0

def generization_error(dataset,tree,alpha):
    A = dataset[0].split(' ')
    B = dataset[1].split(' ')
    C = dataset[2].split(' ')
    A_split=tree[0]
    B1=tree[1]
    B2=tree[2]
    for i in range(len(A)):
        A[i]=int(A[i])
        B[i]=int(B[i])
        C[i]=int(C[i])
    k=0
    number_leaf=0
    for i in range(len(A)):
        count1=B1[2]
        count2=B2[2]
        if A[i]<=A_split[1]:
            if B[i]<B1[1] and B1!=[0,0,[0,0,0,0]]:
                if count1[0]>count1[1]:
                    a=0
                    if C[i]!=a:
                        k+=1
                else:
                    a=1
                    if C[i]!=a:
                        k+=1
            elif B1!=[0,0,[0,0,0,0]]:
                if count1[2]>count1[3]:
                    a=0
                    if C[i]!=a:
                        k+=1
                else:
                    a=1
                    if C[i]!=a:
                        k+=1
            elif B1==[0,0,[0,0,0,0]]:
                if A_split[2][0]>A_split[2][1]:
                    a=0
                    if C[i]!=a:
                        k+=1
                else:
                    a=1
                    if C[i]!=a:
                        k+=1       
        else:
            if B[i]<B2[1] and B2!=[0,0,[0,0,0,0]]:
                if count2[0]>count2[1]:
                    a=0
                    if C[i]!=a:
                        k+=1
                else:
                    a=1
                    if C[i]!=a:
                        k+=1
            elif B2!=[0,0,[0,0,0,0]]:
                if count2[2]>count2[3]:
                    a=0
                    if C[i]!=a:
                        k+=1
                else:
                    a=1
                    if C[i]!=a:
                        k+=1
    if B1==[0,0,[0,0,0,0]]:
        number_leaf+=1
    else:
        number_leaf+=2
    if B2==[0,0,[0,0,0,0]]:
        number_leaf+=1
    else:
        number_leaf+=2
    output=alpha*number_leaf+k
    print(k)
    print("generalization error %s"%output)
    return output
                
def prune(dataset,treein,alpha,minimun):
    g1=generization_error(dataset,treein,0.5)
    A_split=treein[0]
    tree1=treein
    B1=treein[1]
    B2=treein[2]
    if B1!=[0,0,[0,0,0,0]]:
        tree1[1]=[0,0,[0,0,0,0]]
        g2=generization_error(dataset,tree1,0.5)
        if g1>g2:
            treein=tree1
            output=treein
        else:
            output=treein   
    if B2!=[0,0,[0,0,0,0]]:
        tree1[2]=[0,0,[0,0,0,0]]
        g3=generization_error(dataset,tree1,0.5)
        if g2>g3:
            treein=tree1
            output=treein
        else:
            output=treein
    print_tree(treein)
    return output

f=open(r"C:\Users\Administrator\Desktop\Telecom\课件\SD\SD201\TP\TP4\tree.txt") 
dataset = f.read().split('\n',2)
tree=BuildDecisionTree(dataset,2)
print("tree %s" %tree)
generization_error(dataset,tree,0.5)
prune(dataset,tree,0.5,2)

