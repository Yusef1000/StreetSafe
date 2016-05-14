#Yusef Abdulla
#Final Project
#SAFE STREET

#Import necessary files
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

#Initialize Basemap
m = Basemap(projection="mill",
            llcrnrlat= 40,
            llcrnrlon= -75,
            urcrnrlat= 41,
            urcrnrlon= -73)
m.drawcoastlines()
m.drawcountries(linewidth=2)
m.drawstates(color='b')
m.bluemarble()

#CSV files are incredibly large and takes too long to open. Must manually pull out coordinates

#Coordinates of criminals activity
crimes = [(40.740977, -73.984252),
(40.717367, -74.012178)	,
(40.856673, -73.910127)	,
(40.630276, -73.955545)	,
(40.608648, -74.153563)	,
(40.747639, -73.943676)	,
(40.752846, -73.984133)	,
(40.817828, -73.926862)	,
(40.768731, -73.964915)	,
(40.769939, -73.986469)	,
(40.578349, -73.934465)	,
(40.743951, -73.935154)	,
(40.873442, -73.889361)	,
(40.66624, -73.957349)	,
(40.695507, -73.987882)	,
(40.744988, -73.816444)	,
(40.736316, -73.820035)	,
(40.755343, -73.988846)	,
(40.748151, -73.989723)	,
(40.819548, -73.949518)	,
(40.748724, -73.984205)	,
(40.702821, -73.795776)	]

#Coordinates of public buildings
safeZones = [(40.740976, -73.984252),
(40.717366, -74.012178)	,
(40.856673, -73.910126)	,
(40.630275, -73.955545)	,
(40.755343, -73.988846)	,
(40.748151, -73.989723)	,
(40.819548, -73.949518)	,
(40.748724, -73.984205)	,
(40.702821, -73.795776)]

#Give dots appropriates colors and plot them
for i in crimes:
    NYClat, NYClon = i[0], i[1]
    xpt, ypt = m(NYClon, NYClat)
    m.plot(xpt, ypt, 'ro')

for j in safeZones:
    NYClat1, NYClon1 = j[0], j[1]
    xpt1, ypt1 = m(NYClon1, NYClat1)
    m.plot(xpt1, ypt1, 'bo')



plt.title("Safe Street")
plt.show()

