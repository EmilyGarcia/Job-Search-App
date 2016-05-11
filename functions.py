from Tkinter import *
import Tkinter
import requests
import json
from functools import partial
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import googlemaps
from datetime import datetime
##################################################################################################################################
##############################################           FUNCTIONS          ######################################################
##################################################################################################################################


def openDescription( job ):
        
	descWindow = Tkinter.Tk()
	
	jobDesc = job['description']
	
	print (job['location'])
	
	msg = Message(descWindow, text= jobDesc)
	
	msg.config(bg='lightgray', font=('times', 12))
	
	msg.pack()
	
def makeRequest( entry ):
	# Gets city location entered
	city = entry.get()
	
	# Makes request
	payload = {'location': city}
	
	ourRequest = requests.get('http://jobs.github.com/positions.json?', params=payload)
	
	result = ourRequest.json()
	
	return result

def displayJobs( entry, master ):
        
	Result = makeRequest( entry )

        global Result
	
	# Take first five jobs results

        Btn = [0 for x in xrange(5)]
        
        For job in Result:
                
                Desc = partial( openDescription(job), job)
                
                Btn[count] = Button( master, command= desc1, text= job['title'] width= 40 )
                
                Btn[count].grid( row=4, column=0, sticky=W, pady=4 )
                
                count++
                
def getLocation(address)

        gmaps = googlemaps.Client(key='AIzaSyBsk8YYNnUQjmUaD0LgH_wsOtqmMSCnGQE')
        
        geocode_result = gmaps.geocode(address)
        
        location = (geocode_result[0]['geometry']['location']['lng'], geocode_result[0]['geometry']['location']['lat'])
        
        return location
        
def mapThat():
	# make sure the value of resolution is a lowercase L,
	#  for 'low', not a numeral 1
	mapp = Basemap(projection='mill', lat_0=36, lon_0=-119,
	    resolution = 'h', area_thresh = .1,
	    llcrnrlon=-130, llcrnrlat=31,
	    urcrnrlon=-109, urcrnrlat=43)
	 
	mapp.drawcoastlines()
	
	mapp.drawcountries()
	
	mapp.fillcontinents(color='coral')
	
	mapp.drawmapboundary()
	
	mapp.drawstates()

	For job in Result:

                X, Y = getLocation(job['location'])
	
                x, y = mapp( X, Y)
	
                mapp.plot(x, y, 'bo', markersize=10)
	
                labels.append (job['title'])
	
	for label, xpt, ypt in zip(labels, x, y):
                
    		plt.text(xpt+10000, ypt+5000, label)
    		
	plt.show()
