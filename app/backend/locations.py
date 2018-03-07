## locations,py
## Handles the locations table in the database.
#
## Needs to add, remove, and modify locations

def add_location(name, description):
    return sql_query('INSERT (#1, #2) into locations;', name, description)

def get_location(name):
    return sql_query('SELECT * FROM locations WHERE locations.name = #0', name)

def search_location(search, num_results):
    return sql_query('SELECT TOP #1 * FROM locations WHERE locations.name LIKE #0', search, num_results)

def search_location_desc(search, num_results):
    search sql_query('SELECT TOP #1 * FROM locations where locations.description LIKE #0', search, num_results)

