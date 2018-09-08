Brief Information:

Platform:Python 3.6.5 |Anaconda, Inc.|
[GCC 7.2.0] on Ubuntu 18.04

The script uses dataset.xlsx excel file to compute clusters.
Clusters are maintained in list c0,c1,c2,c3,c4.
Respective cluster centers are stored in (c0_x,c0_y),(c1_x,c1_y),(c2_x,c2_y),(c3_x,c3_y),(c4_x,c4_y). 
e_d(x1,y1,x2,y2) is used to compute the distance between points (x1,y1) and (x2,y2)
The script uses a temporary list euclidian_distance to hold euclidian distance from cluster centers
inorder to determine correct clusters.
Apart from these pandas.read_excel() is used to read excel file,
matplotlib.pyplot.scatter and matplotlib.pyplot.plot is used to plot cluster
 
Input parameter:
None. dataset.xlsx neds to be placed in same directory from where python script is excuted.

Output parameter:
Cluster centers for each iteration and Error.
Figure representing clusters,ClusterVsError graph.
