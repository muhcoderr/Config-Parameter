from flask import Flask , render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

# Open Config.json file with read mode
with open('templates\config.json','r') as c:
    params = json.load(c)["params"]

local_server = True

app = Flask(__name__) #creating the Flask class object   

if(local_server):
    # configure the SQL database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = params['local_uri']

else:
    # configure the SQL database, relative to the app instance folder
    app.config["SQLALCHEMY_DATABASE_URI"] = params['prod_uri']
    
# create the extension
db = SQLAlchemy()

# initialize the app with the extension
db.init_app(app)

class Contact(db.Model):
    # name, email, subject, msg
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, nullable=False)
    subject = db.Column(db.String, nullable=True)
    msg = db.Column(db.String, nullable=False)
    date = db.Column(db.String, nullable=False)


 
@app.route('/', methods = ['POST', 'GET']) #decorator drfines the   
def home():
    if request.method == "POST":
        # Add Entery to the DB (name, email, subject, message)
        # db fields name (name, email, subject, msg)
        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')
        entry = Contact(name=name, email=email, subject=subject, msg=message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('index.html', params=params) 

@app.route('/portfolio-details') #decorator drfines the   
def portfoliodetails():  

    return render_template('portfolio-details.html') 
  
if __name__ =='__main__':  
    app.run(debug = True)  