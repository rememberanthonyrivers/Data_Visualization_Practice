import json 

#  Load the Json data into a list
filename = 'json_files/population_data.json'
with open(filename) as f:
    pop_data= json.load(f)

# Print the 2010 populationn for each country
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = pop_dict['Population']
        print(country_name + " : " + population)
