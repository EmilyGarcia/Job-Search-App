from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
###################################################################################################################################
##############################################              MAP              ######################################################
###################################################################################################################################
	
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
 
plt.show()
