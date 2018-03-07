## parts,py
## Handles the parts table in the database.
#
## Needs to add, remove, and modify parts

def add_part(part_num, desc):
    sql_query('INSERT (#1, #2) INTO parts;', part_num, desc)

def get_part(part_num):
    return sql_query('SELECT * FROM parts WHERE parts.partnum = #0;', part_num)

def search_part_num(search, num_results):
    return sql_query('SELECT TOP #1 * FROM parts WHERE parts.partnum LIKE #0;', search, num_results)

def search_part_desc(search, num_results):
    return sql_query('SELECT TOP #1 * FROM parts WHERE parts.description LIKE #0;', search, num_results)