from re import template
from flask import Flask, render_template, request,  current_app as app
from flask_cors import CORS
import requests
import sqlite3
import sys
import os






app = Flask(__name__)

 
CORS(app)

@app.route("/")
def index():

    
    return render_template('test.html')

@app.route('/graphs', methods=['GET', 'POST'])
def send_name():
    food = request.form['food']#fetches info from form
    calories = request.form['calories']#fethech info from form
    
    conn = sqlite3.connect('./static/data/food.db')#gave path to connect to DB
    curs = conn.cursor()
    curs.execute("INSERT INTO foodCalories(food, calories) VALUES((?),(?))",(food, calories))#places user info from site to DB
    conn.commit()
    for row in curs.execute('SELECT * FROM foodCalories'):
        r=({'food':row[1],'calories':row[2]})
        r.append(r)
       
        
    
        

    
    return render_template('test.html', r=r,food=food, calories=calories)

@app.route("/display")
def display():

    return render_template('test.html')
    
    

    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

