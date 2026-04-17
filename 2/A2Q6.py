# Function to search for a country
def find_country(countries, target):
    if target in countries:
        return countries.index(target)
    else:
        return "Not Found in List"

# List of countries
country_list = ["Nepal", "India", "China", "USA", "Japan","Canada"]

# For user to input the name of the country
search = input("\nEnter country name to search: ")
result = find_country(country_list, search)
print(f"Result for '{search}': {result}")