from flask_restful import Api, Resource

from frontend.parts_resource import PartsResource
from frontend.inventory_resource import InventoryResource
from frontend.location_resource import LocationResource

def init_api(api):
    api.add_resource(PartsResource, '/api/v1/parts')
    api.add_resource(InventoryResource, '/api/v1/inventory')
    api.add_resource(LocationResource, '/api/v1/locations')
