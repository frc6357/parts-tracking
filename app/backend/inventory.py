## inventory,py
## Handles the inventory table in the database.
#
## Needs to add, remove, and modify inventory

from backend import sql_query

def new_inventory():
    return

def adjust_inventory():
    return sql_query.execute_query('UPDATE inventory.count TO number WHERE uid = SELECT uid FROM inventory WHERE ')
    return

def move_inventory():
    ## subtract from A, add to B
    return

def putaway_inventory(part, location, number):
    # increase location
    return sql_query.execute_query('UPDATE inventory.count TO number WHERE')

def pull_inventory():
    ## subtract
    return

def get_inventory(part_num):
    query = 'SELECT parts.part_number, locations.name, inventory.qty ' \
            'FROM parts INNER JOIN inventory ON parts.uid=inventory.part_uid ' \
            'INNER JOIN locations ON inventory.loc_uid=locations.uid ' \
            'WHERE parts.part_number = %s;'
    return sql_query.execute_query(query, (part_num, ))

def get_all_inventory():
    query = 'SELECT parts.part_number, locations.name, inventory.qty ' \
            'FROM parts INNER JOIN inventory ON parts.uid=inventory.part_uid ' \
            'INNER JOIN locations ON inventory.loc_uid=locations.uid ' \
            'LIMIT %s;'
    result= sql_query.execute_query(query, (100,))
    print(result)
    return result