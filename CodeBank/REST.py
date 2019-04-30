from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import sqlite3 as sqlite
import sys
import os
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///testtest.db')
app = Flask(__name__)
api = Api(app)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

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

class getJoin(Resource):
    def get(self, zillow_id):
        conn = sqlite.connect('testtest.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        query = "SELECT investmentId,status,antoku_number FROM Address INNER JOIN Investment ON Address.zillow_id = Investment.investmentId WHERE zillow_id=%d" %int(zillow_id)
        all_data = cur.execute(query).fetchall()
        return all_data

class getUser(Resource):
    def get(self,zillow_id):
        conn = sqlite.connect('testtest.db')
        conn.row_factory = dict_factory
        cur = conn.cursor()
        query = "SELECT UserID,CurrentAmount,Returns FROM Address INNER JOIN User ON Address.zillow_id = User.InvestmentId WHERE zillow_id=%d" %int(zillow_id)
        all_data = cur.execute(query).fetchall()
        return all_data 

        

api.add_resource(HomeInfo, '/homeinfo/<zillow_id>') # Route_2
api.add_resource(Zestimate, '/Zestimate/<zillow_id>') # Route_1
api.add_resource(getJoin, '/getJoin/<zillow_id>')
api.add_resource(getUser, '/getUser/<zillow_id>')

if __name__ == '__main__':
     app.debug = True
     app.run(port='5002')