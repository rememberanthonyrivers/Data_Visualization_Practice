import json
# import pygal 
from country_codes import get_country_code
from pygal.maps.world import World

#  Load the Json data into a list
filename = 'json_files/population_data.json'
with open(filename) as f:
    pop_data= json.load(f)


# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '1980':
        country = pop_dict['Country Name']
        population = int(float(pop_dict['Population']))
        code = get_country_code(country)

        # append the country code as the key and the population 
        # as the value for that corresponnding country
        if code:
            cc_populations[code] = population

# make the world map object 
wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_populations)

# save the file 
wm.render_to_file('world_populationII.svg')