#Name       :Akshit Maurya
#Assignment :Clustering
#Rollnumber :18EC65R13
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

import math

import numpy as np


def e_d(x1, y1, x2, y2):
    return (math.sqrt(((x1-x2)**2)+((y1-y2)**2)))


change = True
temp=0

c0 = []
c1 = []
c2 = []
c3 = []
c4 = []

error = []

euclidian_distance = []

c0_x = 0.0
c0_y = 0.0
e_c0 = 0.0

c1_x = 0.0
c1_y = 0.0
e_c1 = 0.0

c2_x = 0.0
c2_y = 0.0
e_c2 = 0.0

c3_x = 0.0
c3_y = 0.0
e_c3 = 0.0

c4_x = 0.0
c4_y = 0.0
e_c4 = 0.0



df = pd.read_excel("dataset.xlsx", header=None)

for k in range(1, 6):
    c0.clear()
    c0_x = df.loc[0, 0]
    c0_y = df.loc[0, 1]
    e_c0=0.0

    c1.clear()
    c1_x = df.loc[1, 0]
    c1_y = df.loc[1, 1]
    e_c1=0.0

    c2.clear()
    c2_x = df.loc[2, 0]
    c2_y = df.loc[2, 1]
    e_c2=0.0

    c3.clear()
    c3_x = df.loc[3, 0]
    c3_y = df.loc[3, 1]
    e_c3=0.0

    c4.clear()
    c4_x = df.loc[4, 0]
    c4_y = df.loc[4, 1]
    e_c4=0.0

    for i in range(df.shape[0]):
        c0.append(i)

    change = True
    temp = 0

    while(change != False):
        change = False
        temp=temp+1
        for i in range(df.shape[0]):
            euclidian_distance.clear()
            if(k>=1):
                euclidian_distance.append(e_d(c0_x, c0_y, df.loc[i, 0], df.loc[i, 1]))
            if(k>=2):
                euclidian_distance.append(e_d(c1_x, c1_y, df.loc[i, 0], df.loc[i, 1]))
            if(k>=3):
                euclidian_distance.append(e_d(c2_x, c2_y, df.loc[i, 0], df.loc[i, 1]))
            if(k>=4):
                euclidian_distance.append(e_d(c3_x, c3_y, df.loc[i, 0], df.loc[i, 1]))
            if(k>=5):
                euclidian_distance.append(e_d(c4_x, c4_y, df.loc[i, 0], df.loc[i, 1]))
            
            if(0 == euclidian_distance.index(min(euclidian_distance))):
                if i in c1:
                    c1.remove(i)
                    c0.append(i)
                    change = True
                elif i in c2:
                    c2.remove(i)
                    c0.append(i)
                    change = True
                elif i in c3:
                    c3.remove(i)
                    c0.append(i)
                    change = True
                elif i in c4:
                    c4.remove(i)
                    c0.append(i)
                    change = True
                else:
                    pass  

            if(1 == euclidian_distance.index(min(euclidian_distance))):
                if i in c0:
                    c0.remove(i)
                    c1.append(i)
                    change = True
                elif i in c2:
                    c2.remove(i)
                    c1.append(i)
                    change = True
                elif i in c3:
                    c3.remove(i)
                    c1.append(i)
                    change = True
                elif i in c4:
                    c4.remove(i)
                    c1.append(i)
                    change = True
                else:
                    pass  
            if(2 == euclidian_distance.index(min(euclidian_distance))):
                if i in c0:
                    c0.remove(i)
                    c2.append(i)
                    change = True
                elif i in c1:
                    c1.remove(i)
                    c2.append(i)
                    change = True
                elif i in c3:
                    c3.remove(i)
                    c2.append(i)
                    change = True
                elif i in c4:
                    c4.remove(i)
                    c2.append(i)
                    change = True
                else:
                    pass  
            if(3 == euclidian_distance.index(min(euclidian_distance))):
                if i in c0:
                    c0.remove(i)
                    c3.append(i)
                    change = True
                elif i in c1:
                    c1.remove(i)
                    c3.append(i)
                    change = True
                elif i in c2:
                    c2.remove(i)
                    c3.append(i)
                    change = True
                elif i in c4:
                    c4.remove(i)
                    c3.append(i)
                    change = True
                else:
                    pass  
            if(4 == euclidian_distance.index(min(euclidian_distance))):
                if i in c0:
                    c0.remove(i)
                    c4.append(i)
                    change = True
                elif i in c1:
                    c1.remove(i)
                    c4.append(i)
                    change = True
                elif i in c2:
                    c2.remove(i)
                    c4.append(i)
                    change = True
                elif i in c3:
                    c3.remove(i)
                    c4.append(i)
                    change = True
                else:
                    pass  

            euclidian_distance.clear()
        if(len(c0)):
            for i in c0:
                c0_x += df.loc[i, 0]
                c0_y += df.loc[i, 1]
            c0_x /= len(c0)
            c0_y /= len(c0)

        if(len(c1)):
            for i in c1:
                c1_x += df.loc[i, 0]
                c1_y += df.loc[i, 1]
            c1_x /= len(c1)
            c1_y /= len(c1)

        if(len(c2)):
            for i in c2:
                c2_x += df.loc[i, 0]
                c2_y += df.loc[i, 1]
            c2_x /= len(c2)
            c2_y /= len(c2)

        if(len(c3)):
            for i in c3:
                c3_x += df.loc[i, 0]
                c3_y += df.loc[i, 1]
            c3_x /= len(c3)
            c3_y /= len(c3)
        
        if(len(c4)):
            for i in c4:
                c4_x += df.loc[i, 0]
                c4_y += df.loc[i, 1]
            c4_x /= len(c4)
            c4_y /= len(c4)
    
    for i in c0:
        e_c0 += e_d(c0_x, c0_y, df.loc[i, 0], df.loc[i, 1])

    e_c0 /= len(c0)

    if(len(c1)):
        for i in c1:
            e_c1 += e_d(c1_x, c1_y, df.loc[i, 0], df.loc[i, 1])

        e_c1 /= len(c1)
    else:
        e_c1=0

    if(len(c2)):
        for i in c2:
            e_c2 += e_d(c2_x, c2_y, df.loc[i, 0], df.loc[i, 1])

        e_c2 /= len(c2)
    else:
        e_c2=0
        
    if(len(c3)):
        for i in c3:
            e_c3 += e_d(c3_x, c3_y, df.loc[i, 0], df.loc[i, 1])
        e_c3 /= len(c3)
    else:
        e_c3=0

    if(len(c4)):
        for i in c4:
            e_c4 += e_d(c4_x, c4_y, df.loc[i, 0], df.loc[i, 1])
        e_c4 /= len(c4)
    else:
        e_c4=0
    
    error.append((e_c0+e_c1+e_c2+e_c3+e_c4)/k)

    print("------------K={}----------".format(k))
    print("[Iterations={}]".format(temp))
    if(k>=1):
        print("c0_x={}".format(c0_x))
        print("c0_y={}".format(c0_y))
        #print(c0)
        #print(e_c0)
    if(k>=2):
        print("c1_x={}".format(c1_x))
        print("c1_y={}".format(c1_y))
        #print(c1)
        #print(e_c1)
    if(k>=3):
        print("c2_x={}".format(c2_x))
        print("c2_y={}".format(c2_y))
        #print(c2)
        #print(e_c2)
    if(k>=4):
        print("c3_x={}".format(c3_x))
        print("c3_y={}".format(c3_y))
        #print(c3)
        #print(e_c3)
    if(k>=5):
        print("c4_x={}".format(c4_x))
        print("c4_y={}".format(c4_y))
        #print(c4)
        #print(e_c4)
    print("Error={}".format(error[k-1]))

for i in c0:
    plt.plot(df.loc[i, 0], df.loc[i, 1],'ro')

for i in c1:
    plt.plot(df.loc[i, 0], df.loc[i, 1],'bo')

for i in c2:
    plt.plot(df.loc[i, 0], df.loc[i, 1],'go')

for i in c3:
    plt.plot(df.loc[i, 0], df.loc[i, 1],'mo')

for i in c4:
    plt.plot(df.loc[i, 0], df.loc[i, 1],'co')

xaxis=[]
for i in range(len(error)):
    xaxis.append(i+1)

plt.figure()

plt.plot(xaxis,error)
plt.ylabel("Error")
plt.xlabel("Number of Clusters")
plt.show()