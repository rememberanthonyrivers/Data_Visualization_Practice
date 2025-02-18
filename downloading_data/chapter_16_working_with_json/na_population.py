# Plotting Numerical Data on a World Map
import pygal
from pygal.maps.world import World

# creates a world map object from pygal 
wm = World()

# set the title of the map
wm.title = 'Populations of Countries in North America'

# add the data to the world map object 
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

# creates the svg file of the world map 
wm.render_to_file('na_populations.svg')