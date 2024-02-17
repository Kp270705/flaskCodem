from flask import Flask, render_template, jsonify
import jinja2
from flask_sqlalchemy import SQLAlchemy



app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db=SQLAlchemy(app)

class Item(db.Model):
    id=db.Column(db.Integer(), primary_key=1)
    name=db.Column(db.String(length=30), nullable=0)
    Course=db.Column(db.String(length=30), nullable=0)
    Sid=db.Column(db.Integer(), nullable=0, unique=1)
    marks=db.Column(db.Integer(), nullable=0)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about/<no>')
def about(no):
    return(f"<h1> about page of your number:- {no} </h1>")


@app.route('/loggin/')
def loggin():
    return render_template("loggin.html", item_name="log")

@app.route('/student/')
def student():
    student=[
        {'name':"Kunal", 'course':"BCA", 'id':22581150, 'marks':78},
        {'name':"Aashu", 'course':"BCA", 'id':22581123, 'marks':72},
        {'name':"Mohit", 'course':"BCA", 'id':225811134, 'marks':85},
        {'name':"Sumit", 'course':"BCA", 'id':225811150, 'marks':88},
        {'name':"Zuneirah", 'course':"BCA", 'id':225811169, 'marks':98},
    ]
    
    return render_template('student.html', items=student)



if __name__  ==  "__main__":
    
    app.run(debug=True)
    
    