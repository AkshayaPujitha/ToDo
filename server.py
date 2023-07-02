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
uri =f"mongodb+srv://pujitha:pujitha23@cluster0.xaywh5l.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

#Retrieve
@app.route('/')
def index():
    tasks=client.todo.tasks.find({})
    l=[]
    for task in tasks:
        l.append(task)
    #print(tasks)
    return render_template("index.html",tasks=l)

#Create
@app.route('/add/',methods=["POST"])
def add():
    task=request.form.get('task')
    date=request.form.get('date')
    client.todo.tasks.insert_one({
        'task':task,
        'date':date,
        'is_completed':False
    })
    print("Sucessfully added")
    return Response(task)


if __name__=="__main__":
    app.run(debug=True,port=5001)