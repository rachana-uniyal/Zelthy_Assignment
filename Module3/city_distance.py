
import mpu

# Function to preprocess coordinates entered by user 
def check(city):
	coordinates = city.split(",")
	lat = coordinates[0]
	if lat[-1]=="N":
		lat = float(lat.split()[0])
	else:
		lat = -1*float(lat.split()[0])

	lon = coordinates[1]

	if lon[-1]=="E":
		lon = float(lon.split()[0])
	else:
		lon = -1* float(lon.split()[0])

	return lat,lon	


class Distance:
	def __init__(self, lat1, lon1, lat2, lon2):
		self.lat1 = lat1
		self.lon1 = lon1
		self.lat2 = lat2
		self.lon2 = lon2


	# Function to calculate distance between two cities
	def findDistance(self):
		dist = mpu.haversine_distance((self.lat1, self.lon1), (self.lat2, self.lon2))
		return dist



# Ask coordinates of City 1 from user
city1 = input("City1 : ")

# Ask coordinates of City 2 from user
city2 = input("City2 : ")


try:
	# preprocess the coordinates given by user using check function
	lat1, lon1 = check(city1)
	lat2, lon2 = check(city2)
	# object of class Distance
	cityDistance = Distance(lat1,lon1,lat2,lon2)
	print("City 1 and City 2 are " + str(round(cityDistance.findDistance(),2)) +" km apart")

except:
	print("Invalid Input")



