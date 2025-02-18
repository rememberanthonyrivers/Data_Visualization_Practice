import json 
from country_codes import get_country_code

#  Load the Json data into a list to start working with json file
filename = 'json_files/population_data.json'
with open(filename) as f:
    pop_data= json.load(f)

# Print the 2010 population for each country.
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Population']))
        code = get_country_code(country_name)

        if code:
            print(code + ": " + str(population))
        else:
            print("ERROR - " + country_name)