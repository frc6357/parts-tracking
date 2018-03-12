from flask_restful import Resource

from backend import parts


class PartsResource(Resource):
    def get(self):
        return parts.get_all_parts()