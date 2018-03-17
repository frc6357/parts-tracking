from flask_restful import Resource

from backend import locations

class LocationResource(Resource):
    def get(self):
        return locations.list_locations()