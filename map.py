from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
 
# make sure the value of resolution is a lowercase L,
#  for 'low', not a numeral 1
map = Basemap(projection='merc', lat_0=36, lon_0=-119,
    resolution = 'h', area_thresh = 1000.0,
    llcrnrlon=-119.643034, llcrnrlat=31.693901,
    urcrnrlon=-119.633409, urcrnrlat=42.326470)
 
map.drawcoastlines()
map.drawcountries()
map.fillcontinents(color='coral')
map.drawmapboundary()
#map.drawstates()

map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
 
plt.show()
