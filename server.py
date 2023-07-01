from flask import Flask,render_template,request,Response
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

#connecting with mongodb
app=Flask(__name__)
load_dotenv('.env')
mongo_db_password = os.environ.get('MONGO_DB_PASSWORD')
uri = f"mongodb+srv://pujitha:{mongo_db_password}@flasktodomongo.xgwvcrn.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


@app.route('/')
def index():
    task={'completed':False,'title':"washing clothes",'due_date':'23-10-2003'}
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)