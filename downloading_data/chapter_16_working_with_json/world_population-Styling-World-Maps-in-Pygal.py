import json
from pygal.style import RotateStyle
from country_codes import get_country_code
from pygal.maps.world import World

#  Load the Json data into a list
filename = "chapter_16_working_with_json/json_files/population_data.json"
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict["Year"] == "1980":
        country = pop_dict["Country Name"]
        population = int(float(pop_dict["Population"]))
        code = get_country_code(country)

        # append the country code as the key and the population
        # as the value for that corresponnding country
        if code:
            cc_populations[code] = population

# Group the countries into 3 population levels. dicts
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:  # if pop is less than 10 million

        cc_pops_1[cc] = pop
    elif pop < 1000000000:  # if pop is more than 10 mill but less that 1 bill

        cc_pops_2[cc] = pop
    else:  # if pop is 1 bill or more

        cc_pops_3[cc] = pop

# See how many countries are in each level. len of dicts
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# make the world map object
wm = World()

wm_style = RotateStyle("#336699")  # sets the color of the map
wm = World(style=wm_style)  # applys the color to the map
wm.title = "World Population in 2010, by Country"
wm.add("0-10m", cc_pops_1)  # label and value
wm.add("10m-1bn", cc_pops_2)  # label and value
wm.add(">1bn", cc_pops_3)  # label and value

# save the file
wm.render_to_file("world_populationIII.svg")
