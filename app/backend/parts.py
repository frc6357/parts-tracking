## parts,py
## Handles the parts table in the database.
#
## Needs to add, remove, and modify parts

from backend import sql_query

def add_part(part_num, desc):
    return sql_query.execute_query('INSERT INTO parts (part_number, description) VALUES (%s,%s);' , (part_num, desc))

def get_all_parts():
    return sql_query.execute_query('SELECT * FROM parts LIMIT %s;', (100,))

def get_part(part_num):
    return sql_query.execute_query('SELECT * FROM parts WHERE parts.partnum = %s;', (part_num,))

def search_part_num(search, num_results):
    return sql_query.execute_query('SELECT * FROM parts WHERE parts.partnum LIKE %s LIMIT %s;', (search, num_results))

def search_part_desc(search, num_results):
    return sql_query.execute_query('SELECT * FROM parts WHERE parts.description LIKE %s LIMIT %s;', (search, num_results))