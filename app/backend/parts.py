## parts,py
## Handles the parts table in the database.
#
## Needs to add, remove, and modify parts

def add_part(part_num, desc):
    return sql_query('INSERT INTO parts (part_number, description) VALUES (%s,%s);' % (part_num, desc))

def get_part(part_num):
    return sql_query('SELECT * FROM parts WHERE parts.partnum = %s;', (part_num))

def search_part_num(search, num_results):
    return sql_query('SELECT * FROM parts WHERE parts.partnum LIKE %s LIMIT %d;', search, num_results)

def search_part_desc(search, num_results):
    return sql_query('SELECT * FROM parts WHERE parts.description LIKE %s LIMIT %d;', search, num_results)