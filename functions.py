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
        
    # Opens new Tkinter window
	descWindow = Tkinter.Tk()
	
	# Gets job location
	jobLoc = job['location']
	jobLoc = jobLoc + "\n"
	# Gets job description
	jobDesc = job['description']
	
	print ( job['location'] )
	

	msg = Message( descWindow, text= (jobLoc, jobDesc) )
	msg.config( font=('times', 12), fg='MediumPurple4', bg='light cyan' )
	
	msg.pack()
	
def makeRequest( entry ):

	# Gets city location entered
	city = entry.get()
	
	# Makes request
	payload = { 'location': city }
	
	ourRequest = requests.get( 'http://jobs.github.com/positions.json?', params=payload )
	
	result = ourRequest.json()
	
	return result

def displayJobs( entry, master ):

	# Stores result of request
	global Result
	Result = makeRequest( entry )

	# Button list 
	Btn = [ 0 for x in xrange(5) ]

	# Counter for Btn
	count = 0

	# Row position of each button - will be incremented 
	r = 4
    
    # Take first 5 jobs results and assign to each button  
	for job in Result:

		# Stores function call to openDescription(job)
		Desc = partial( openDescription, job )

		# Assigns the Btn at count a title 
		Btn[count] = Button( master, command= Desc, text= job['title'], width= 40 )
		Btn[count].config( fg='MediumPurple4', bg='DarkOliveGreen3', relief = FLAT )
		Btn[count].grid( row=r, column=0, sticky=W, pady=4 )

		# Increments count and row
		if (count < 6):
			count = count + 1
		r = r + 1
                
def getLocation( address ):

    gmaps = googlemaps.Client( key='AIzaSyBsk8YYNnUQjmUaD0LgH_wsOtqmMSCnGQE' )
    
    geocode_result = gmaps.geocode( address )
    
    location = ( geocode_result[0]['geometry']['location']['lng'], geocode_result[0]['geometry']['location']['lat'] )
    
    return location
        
def mapThat():

	# Draws map
	mapp = Basemap( projection='mill', resolution = 'i', area_thresh = .1)

	"""	, lat_0=36, lon_0=-119,
	    resolution = 'h', area_thresh = .1,
	    llcrnrlon=-130, llcrnrlat=31,
	    urcrnrlon=-109, urcrnrlat=43 )"""

	mapp.drawcoastlines()
	
	mapp.drawcountries()
	
	mapp.fillcontinents( color='coral', lake_color='aqua' )
	
	mapp.drawmapboundary( fill_color='aqua' )
	
	mapp.drawstates()

	# List for job titles
	jobLoc = [ 0 for x in xrange(5) ]

	# List for latitude
	latList = [ 0 for x in xrange(5) ]

	# List for longitude
	lonList = [ 0 for x in xrange(5) ]

	# Counter for x and y lists
	count = 0

	# Plots points
	for job in Result:

		lat, lon = getLocation( job['location'] )

		# Compute native map projection coordinates of lat/lon grid
		x, y = mapp( lat, lon )

		latList.append( x )
		lonList.append( y )

		mapp.plot( latList[count], lonList[count], 'bo', markersize=10 )

		jobLoc.append ( job['location'] )
		count = count + 1
	
	# Labels all points already plotted
	for loc, xpt, ypt in zip( jobLoc, latList, lonList ):

		plt.text( xpt+10000, ypt+5000, loc )
    		
	plt.show()
  