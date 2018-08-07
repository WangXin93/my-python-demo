from flask import Flask, g
from flask_restful import Resource, Api
from flask_restful import reqparse
import shelve
import markdown
import os

app = Flask(__name__)
api = Api(app)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("devices.db")
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    """"Present some documents"""

    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdownfile:
        content = markdownfile.read()
        return markdown.markdown(content)

class DeviceList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        devices = []

        for key in keys:
            devices.append(shelf[key])

        return {'message': 'Sucess', 'data': devices}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('identifier', required=True)
        parser.add_argument('name', required=True)
        parser.add_argument('device_type', required=True)
        parser.add_argument('controller_gateway', required=True)

        args = parser.parse_args()

        shelf = get_db()
        shelf[args['identifier']] = args

        return {'message': 'Device registered', 'data': args}, 201

class Device(Resource):
    def get(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Device not found', 'data':{}}, 404
        return {'message': 'Device found', 'data':shelf[identifier]}, 200

    def delete(self, identifier):
        shelf = get_db()

        if not (identifier in shelf):
            return {'message': 'Device not found', 'data':{}}, 404

        del shelf[identifier]
        return '', 204

api.add_resource(DeviceList, "/devices")
api.add_resource(Device, "/devices/<string:identifier>")
