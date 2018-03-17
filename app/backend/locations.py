## locations,py
## Handles the locations table in the database.
#
## Needs to add, remove, and modify locations

from backend import sql_query

def add_location(name, description):
    return sql_query.execute_query('INSERT INTO locations (name, description) VALUES (%s, %s);' , (name, description))

def get_location(name):
    return sql_query.execute_query('SELECT * FROM locations WHERE locations.name = %s;', (name,))

def search_location(search, num_results):
    return sql_query.execute_query('SELECT * FROM locations WHERE locations.name LIKE %s LIMIT %s;', (search, num_results))

def search_location_desc(search, num_results):
    return sql_query.execute_query('SELECT * FROM locations where locations.description LIKE %s LIMIT %s', (search, num_results))

def list_locations():
    return sql_query.execute_query('SELECT * FROM locations LIMIT %s;', (100,))
