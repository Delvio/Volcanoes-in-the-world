import folium
import pandas


# Reading the data from the txt file using pandas

data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
# status = list(data["STATUS"])

# This Function deterimine the elevation of each volcano

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

# this will create the map using the folium library
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Control Room")

# creating a layer for the volcanoes

fgv = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m",
    fill_color=color_producer(el), fill=True,  color = 'grey', fill_opacity=0.7))

#Creating a layer for the population in each country
fgp = folium.FeatureGroup(name="Population")


# Colors each country based on their pupulation
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))


# Adds the layers fo each section to the map
map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.TileLayer('cartodbdark_matter'))
map.add_child(folium.TileLayer('stamentoner'))
map.add_child(folium.TileLayer('stamenterrain'))
map.add_child(folium.TileLayer('cartodbpositron'))
map.add_child(folium.TileLayer('stamenwatercolor'))
map.add_child(folium.TileLayer('Mapbox Control Room'))
map.add_child(folium.LayerControl())


# output on a HTML file
map.save("Map1.html")



# //TODO: hay que crear la base de datos actualizada para que se vean las lineas de datos del volcano
