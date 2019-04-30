import numpy as np
import matplotlib.pyplot as plt
import sqlite3 as sqlite
from sklearn.cluster import KMeans
import math


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

##40 IS LAT and -105 is long
random_state = 300
conn = sqlite.connect('K_means_data.db')
conn.row_factory = dict_factory
cur = conn.cursor()
all_data = cur.execute("SELECT * FROM Address;").fetchall()
print(all_data[0]) 

hold_array=[]

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d




for i in range(0,96):
	if all_data[i]['Zestimate'] <=1500000:
		CU = [40.003999984, -105.266998932]
	
		
		ex_rent=(all_data[i]['Zestimate'])*0.008
		print(ex_rent)
		
		Lngt=all_data[i]['LAT']
		Lati=all_data[i]['LNG']

		cur_loc= [Lati,Lngt]

		distance_miles = distance([Lati,Lngt],CU)

		hold_array.append([ex_rent,distance_miles])

X=np.array(hold_array)



y_pred = KMeans(n_clusters=5, random_state=random_state).fit_predict(X)
print(y_pred)


plt.scatter(X[:,0], X[:,1], c=y_pred)
plt.title("K_Means Testing")
plt.xlabel("Expected Rent")
plt.ylabel("Distance in miles from CU")

plt.savefig("Antoku_K_Means.png")

##The Antoku scores from K_means Cluster
#[3,0,2,2,3,3,2,0,4,2,3,4,0,0,0,0,0,0,0,0,0,0,0,0,0,3,3,0,4,1,4,4,0,1,1,4,1,1,1,0,2,4,4,2,1,1,0,1,4,0,3,1,3,3,0,4,0,1,1,4,4,4,4,3,1,1,1,3,0,4,3,4,0,0,0,1,1,1,1,0,0,2,0,1,4,4,0,0,0,4,0,1,0]

