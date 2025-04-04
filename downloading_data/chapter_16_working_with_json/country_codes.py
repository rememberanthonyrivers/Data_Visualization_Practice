# Obtaining-Two-Digit-Country-Codes
from cc import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # If the country wasn't found, return None.
    return None

# print(get_country_code('Andorra'))
# print(get_country_code('Ethiopia'))
# print(get_country_code('Greenland'))