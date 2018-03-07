## inventory,py
## Handles the inventory table in the database.
#
## Needs to add, remove, and modify inventory

def new_inventory():
    return

def adjust_inventory():
    return sql_query('UPDATE inventory.count TO number WHERE uid = SELECT uid FROM inventory WHERE ')
    return

def move_inventory():
    ## subtract from A, add to B
    return

def putaway_inventory(part, location, number):
    # increase location
    return sql_query('UPDATE inventory.count TO number WHERE')

def pull_inventory():
    ## subtract
    return