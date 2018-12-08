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
e= create_engine("sqlite:///new.sqlite")

app = Flask(__name__)
api = Api(app)
# opens home page
@app.route("/")
def home():  
    return render_template('index.html')

class Currency_Meta(Resource):
    def get(self):
        #Connect to databse
        conn = e.connect()
        #Perform query and return JSON data
        query = conn.execute("select distinct month from currency")
        return {'currency': [i[0] for i in query.cursor.fetchall()]}

class Currency_Exchange(Resource):
    def get(self, month):
        conn = e.connect()
        query = conn.execute("select * from new where month='%s'"%month)
        #Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
        return result
        #We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient
 
api.add_resource(Currency_Exchange, '/curr/<string:month>')
api.add_resource(Currency_Meta, '/currency')

if __name__ == "__main__":
    app.run()

