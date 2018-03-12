from flask_restful import Api, Resource

from frontend.parts_resource import PartsResource
from frontend.inventory_resource import InventoryResource

def init_api(api):
    api.add_resource(PartsResource, '/parts')
    api.add_resource(InventoryResource, '/inventory')
