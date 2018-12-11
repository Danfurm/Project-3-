from flask import Flask, jsonify  
from flask import render_template
from flask_restful import Resource, Api
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

# creates a Flask application, named app


#################################################
# Database Setup
#################################################
e= create_engine("sqlite:///currency.sqlite")

app = Flask(__name__)
api = Api(app)
# opens home page
@app.route("/")
def home():  
    return render_template('index.html')

class Eur_Date_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct date from EUR")
        return {'dates': [i[0] for i in query.cursor.fetchall()]}

class Chf_Date_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct date from CHF")
        return {'dates': [i[0] for i in query.cursor.fetchall()]}

class Jpy_Date_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct date from JPY")
        return {'dates': [i[0] for i in query.cursor.fetchall()]}

class Gbp_Date_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct date from GBP")
        return {'dates': [i[0] for i in query.cursor.fetchall()]}

class Rec_Date_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct date from RInd")
        return {'dates': [i[0] for i in query.cursor.fetchall()]}

class Eur_Date_Select(Resource):
    def get(self, date):
        conn = e.connect()
        query = conn.execute("select * from EUR where date='%s'"%date)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Jpy_Date_Select(Resource):
    def get(self, date):
        conn = e.connect()
        query = conn.execute("select * from JPY where date='%s'"%date)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Chf_Date_Select(Resource):
    def get(self, date):
        conn = e.connect()
        query = conn.execute("select * from CHF where date='%s'"%date)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Gbp_Date_Select(Resource):
    def get(self, date):
        conn = e.connect()
        query = conn.execute("select * from Gbp where date='%s'"%date)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Rec_Date_Select(Resource):
    def get(self, date):
        conn = e.connect()
        query = conn.execute("select * from RInd where date='%s'"%date)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient

class Jpy_Dump (Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from JPY")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Eur_Dump (Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from EUR")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Gbp_Dump (Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from GBP")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Chf_Dump (Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from CHF")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

class Rec_Dump (Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select * from RInd")
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result

api.add_resource(Eur_Date_Select, '/EUR/Date/<string:date>')
api.add_resource(Jpy_Date_Select, '/JPY/Date/<string:date>')
api.add_resource(Chf_Date_Select, '/CHF/Date/<string:date>')
api.add_resource(Gbp_Date_Select, '/GBP/Date/<string:date>')
api.add_resource(Rec_Date_Select, '/REC/Date/<string:date>')
api.add_resource(Eur_Date_Meta, '/EUR/Dates')
api.add_resource(Jpy_Date_Meta, '/JPY/Dates')
api.add_resource(Gbp_Date_Meta, '/GBP/Dates')
api.add_resource(Chf_Date_Meta, '/CHF/Dates')
api.add_resource(Rec_Date_Meta, '/REC/Dates')
api.add_resource(Jpy_Dump, '/JPY')
api.add_resource(Eur_Dump, '/EUR')
api.add_resource(Chf_Dump, '/CHF')
api.add_resource(Gbp_Dump, '/GBP')
api.add_resource(Rec_Dump, '/REC')
if __name__ == "__main__":
    app.run()

