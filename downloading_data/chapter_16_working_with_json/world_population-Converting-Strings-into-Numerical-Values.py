import json 

#  Load the Json data into a list to start working with json file
filename = 'json_files/population_data.json'
with open(filename) as f:
    pop_data= json.load(f)

# Print the 2010 populationn for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Population'])) # numerical value converted from json string to an integer
        print(country_name + " : " + str(population)) # population obj converted to back to a str
