from flask import make_response
from flask import current_app as app
from models import db, items, item_pic, user
from flask_restful import Resource, Api
from flask import jsonify
import requests

api = Api(app)

# index Route 
@app.route('/', methods=['GET'])
def index():
    if (db):
        return """
                <h1>Restful API Server</h1>
        """
    else:
        return 'Something is broken.'

# FetchData From Mysql Database Route Starts Here
class item(Resource):
    def get(self):
        records = [dict({
            "id": dat.id,
            "name": dat.name,
            "description": dat.description,
            "location": dat.location,
            "created_at": dat.created_at,
        }) for dat in items.query.all()]

        return jsonify(records)

class items(Resource):
    def get(self, id):
        dat = items.query.get(int(id))
        if dat:
            record = {
                "id": dat.id,
                "name": dat.state,
                "description": dat.case,
                "location": dat.death,
                "created_at": dat.updated,
            }
            return jsonify(record)
        else:
            record = {
                "message": "Result Not Found"
            }
            return jsonify(record), 404

api.add_resource(item, '/items')
api.add_resource(items, '//<id>')

