import googlemaps

from datetime import datetime


gmaps = googlemaps.Client(key='AIzaSyBsk8YYNnUQjmUaD0LgH_wsOtqmMSCnGQE')

'''
#Get list of address from query
address_list

#Get the longtitude and latitude from each address
for address in address_list

	geocode = gamps.geocode(adress)

	location = (geocode_result[0]['geometry']['location']['lng'], geocode_result[0]['geometry']['location']['lat'])


'''
#Example on how to print longtitude and latitude
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

 
location = (geocode_result[0]['geometry']['location']['lng'], geocode_result[0]['geometry']['location']['lat'])

print(location)


