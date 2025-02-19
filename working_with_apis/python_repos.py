import requests

# Make the api call and store the request
url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
r = requests.get(url)
print("\nStatus Code :", r.status_code)

# now store the api response
response_dict = r.json()

#  Process results
print(response_dict.keys())
