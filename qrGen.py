from flask import Flask, render_template, session, url_for, request, redirect
import pymongo
import pyqrcode
import qrtools
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
QRdb = client["QRGen"] 
students = client.QRGen.students

@app.route('/')
def index(): 
    return render_template('index.html')

@app.route('/reg', methods=['POST'])
def qrgen():
    name = request.form['name']
    college = request.form['college']
    dept = request.form['dept']
    year = request.form['year']
    ph = request.form['no']
    email = request.form['email']
    students.insert({"Name":name, "College":college, "Department":dept,"Year":year,"Phone":ph,"Email":email})
    details = " NAME : " +name+ "\n COLLEGE : " +college+"\n DEPT : "+dept+"\n YEAR : "+year+"\n PHONE NO : "+ph+"\n EMAIL : "+email
    qr = pyqrcode.create(details) 
    qr.png(file="qrimg.png", scale=6) 
    return render_template('success.html')

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)
    