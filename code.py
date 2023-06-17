# -*- coding: utf-8 -*-
"""
Determine optimal number of clusters with dendogram 
Program by Ammar AHmed Siddiqui
#"""

# Importing general libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# importing cluster specific library [dendrogram]
import scipy.cluster.hierarchy as sch

# Load customers Mall Daataset
dataset = pd.read_csv("D:\IMPORTANT\MASTERS\BAHRIA UNIV\Spring2023 Semester\CourseMaterial\Tools in DS\Mall_customers.csv")

# Print dataset top 20 lines only
print(dataset.head())


# Extract 3rd and 4th columns only for analysis
# 3rd Column = Annual Income
# 4th Column = Spending Score

newdata = dataset.iloc[:,[3,4]].values


plt.title('Dendrogram')
plt.xlabel('Customers')



# setting dendogram
# linkage method is used to compute distance d(s,t) between two 
# clusters naing s and t


# finding optimal number of clusters using dendogram


Z1 = sch.linkage(newdata,method='median')
Z2 = sch.linkage(newdata,method='ward')
Z3 = sch.linkage(newdata,method='centroid')
Z4 = sch.linkage(newdata,method='weighted')
Z5 = sch.linkage(newdata,method='average')
Z6 = sch.linkage(newdata,method='complete') # Max
Z7 = sch.linkage(newdata,method='single') # Min

dendrogram1 = sch.dendrogram(Z1)
plt.ylabel('Median Distance')
plt.show()  

dendrogram2 = sch.dendrogram(Z2)
plt.ylabel('Ward Distance')
plt.show()

dendrogram3 = sch.dendrogram(Z3)
plt.ylabel('Centroid Distance')
plt.show()

dendrogram4 = sch.dendrogram(Z4)
plt.ylabel('Weighted')
plt.show()

dendrogram5 = sch.dendrogram(Z5)
plt.ylabel('Average Distance')
plt.show()

dendrogram6 = sch.dendrogram(Z6) # max
plt.ylabel('Max/Complete Distance')
plt.show()

dendrogram7 = sch.dendrogram(Z7) # min
plt.ylabel('Min/Single Distance')
plt.show()







