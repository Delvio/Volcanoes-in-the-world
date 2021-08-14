import folium
import pandas

# Reading the data from the txt file using pandas

data = pandas.read_csv("volcanoes.txt")
name = list(data["Name"])
lat = list(data["Latitude"])
lon = list(data["Longitude"])
elev = list(data["Elevation"])
volcano_type = list(data["Type"])
last_known_eruption = list(data["Last Known Eruption"])
status = list(data["Status"])
location = list(data["Location"])
country = list(data["Country"])

# This Function deterimine the elevation of each volcano


def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


# this will create the map using the folium library
map = folium.Map(
    location=[38.58, -99.09],
    zoom_start=6,
    tiles="stamenterrain",
    attr="Elvio Severino",
)


# creating a layer for the volcanoes

fgv = folium.FeatureGroup(name="Volcanoes")

for (
    lt,
    ln,
    el,
    name,
    status,
    volcano_type,
    last_known_eruption,
    country,
    location,
) in zip(
    lat,
    lon,
    elev,
    name,
    status,
    volcano_type,
    last_known_eruption,
    country,
    location,
):
    string = f"""Name: {name}
            <br>
            Elevation: {el}m
            <br>
            Type: {volcano_type}
            <br>
            Status: {status}
            <br>
            Last Known Eruption: {last_known_eruption}
            <br>
            Country = {country}
            <br>
            Location: {location} 
            """

    iframe = folium.IFrame(string)
    popup = folium.Popup(iframe, min_width=250, max_width=250)

    fgv.add_child(
        folium.CircleMarker(
            location=[lt, ln],
            radius=6,
            popup=popup,
            fill_color=color_producer(el),
            fill=True,
            color="grey",
            fill_opacity=0.7,
        )
    )

# Adds the layers fo each section to the map
map.add_child(fgv)
map.add_child(folium.TileLayer("stamenterrain"))
map.add_child(folium.TileLayer("cartodbpositron"))
map.add_child(folium.TileLayer("stamenwatercolor"))
map.add_child(folium.LayerControl())


# output on a HTML file
map.save("index.html")
