import pandas as pd
import matplotlib.pyplot as plt
csv = pd.read_csv('via_export_csv.csv')
# print(csv)
centroid = []
width = 0
height = 0
for index, row in csv.iterrows():
	x = row['region_shape_attributes']
	x = x.split(',')
	for i in range(len(x)):
		#print(i)
		if i==2:
			y = x[i].split(':')
			height = int(y[1])/2
		if i ==4:
			y = x[i].split(':')
			y = y[1][:-1]
			width = int(y)/2
	# print(x[0])
		# print(width, height)
	value = [width,height]
	centroid.append(value)
# print(centroid)

from sklearn.cluster import KMeans
import numpy as np

X = np.array(centroid)
kmeans = KMeans(n_clusters=4, random_state=0).fit(X)
print(kmeans.labels_)
print(kmeans.cluster_centers_)



plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, s=50, cmap='viridis_r')

centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
#plt.show()

plt.savefig('kmeans.png', dpi=1200)

