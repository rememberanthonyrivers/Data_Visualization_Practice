import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
# Make the api call and store the request
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("\nStatus Code :", r.status_code)
# now store the api response
response_dict = r.json()  # .json turns the data into a python dict
print("Total repositories:", response_dict["total_count"]) # represents the toal num of repos onn github
# Explore information about the repositories
repo_dicts = response_dict['items'] # list connntaining a number of dictionaries 

# lets now create the visual 
names, stars = [], [] # here we create two list to store the data for our visual 
for repo_dict in repo_dicts:
    names.append(repo_dict['name']) 
    stars.append(repo_dict['stargazers_count'])

# Make visualization.
my_style = LS('#333366', base_style=LCS)

my_style.title_font_size = 24 
my_style.label_font_size = 14 
my_style.major_label_font_size = 18

my_config = pygal.Config() 
my_config.x_label_rotation = 45
my_config.show_legend = False 
my_config.truncate_label = 15 
my_config.show_y_guides = False 
my_config.width = 1000
chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on GitHub' 
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

print("Repositories returned:", len(repo_dicts)) # num of repos 
# Examine the first repository.
# repo_dict = repo_dicts[0] # we pull the first repo and store it in repo_dict 
# print("\nKeys:", len(repo_dict)) # prints the number of keys withinn this repo 
# for key in sorted(repo_dict.keys()): # prints all of the keys 
#     print(key)
# #  Process results
# # print(response_dict.keys())


# now lets analyze our data
# print("\nSelected information about first repository:")
# print('Name:', repo_dict['name'])
# print('Owner:', repo_dict['owner']['login'])
# print('Stars:', repo_dict['stargazers_count'])
# print('Repository:', repo_dict['html_url'])
# print('Created:', repo_dict['created_at']) 
# print('Updated:', repo_dict['updated_at'])
# print('Description:', repo_dict['description'] + "\n")

# print("Selected Information about each Repository\n")
# for repo_dict in repo_dicts:
#     print('\nName:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Description:', repo_dict['description'])
#     print("\n")


