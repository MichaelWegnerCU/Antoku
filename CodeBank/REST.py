from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///AddressToDB.db')
app = Flask(__name__)
api = Api(app)

class Zestimate(Resource):
    def get(self, zillow_id):
        conn = db_connect.connect() # connect to database
        query = conn.execute("select Zestimate from Address where zillow_id=%d " %int(zillow_id))
        result = [dict(r) for r in query]
        return jsonify(result)

class HomeInfo(Resource):
    def get(self, zillow_id):
        conn = db_connect.connect()
        query = conn.execute("select street_address,zipcode,Zestimate,HomeType,NumBath,HomeSize from Address where zillow_id=%d " %int(zillow_id))
        result = [dict(r) for r in query]
        return jsonify(result)

        

api.add_resource(HomeInfo, '/homeinfo/<zillow_id>') # Route_2
api.add_resource(Zestimate, '/Zestimate/<zillow_id>') # Route_1


if __name__ == '__main__':
     app.debug = True
     app.run(port='5002')