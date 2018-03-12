from flask_restful import Resource

from backend import inventory

class InventoryResource(Resource):
    def get(self):
        return inventory.get_all_inventory()