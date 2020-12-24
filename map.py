import folium
from IPython.display import HTML, display
map_osm = folium.Map(location=[45.5236,-122.6750],tiles='Stamen Toner',zoom_control=13)
map_osm.simple_marker(ocation=[45.5236,-122.6750],popup='Camp Muir')
map_osm.click_for_marker(popup='Waypoint')
display(map_osm)
# mapWidth, mapHeight = (400,500) # width and height of the displayed iFrame, in pixels
# srcdoc = map_osm.HTML.replace('"', '&quot;')
# embed = HTML('<iframe srcdoc="{}" '
#              'style="width: {}px; height: {}px; display:block; width: 50%; margin: 0 auto; '
#              'border: none"></iframe>'.format(srcdoc, mapWidth, mapHeight))
# embed