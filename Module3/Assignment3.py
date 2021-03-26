# from geopy.distance import geodesic


# origin = (51.5074 , -0.1278 )  # (latitude, longitude) don't confuse
# dist = (48.8566 , 2.3522 )


# print(geodesic(origin, dist).meters)  # 23576.805481751613
# print(geodesic(origin, dist).kilometers)  # 23.576805481751613
# print(geodesic(origin, dist).miles)  # 14.64994773134371


# import mpu

# # Point one
# lat1 = 51.5074
# lon1 = -0.1278

# # Point two
# lat2 = 48.8566 
# lon2 = 2.3522

# # What you were looking for
# dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
# print(dist)  # gives 278.45817507541943.

from haversine import haversine_vector, Unit

lyon = (51.5074,-0.1278 )# (lat, lon)
paris = (48.8566 ,2.3522)


haversine_vector([lyon, paris], Unit.KILOMETERS, comb=True)

