from flask import Flask, render_template
from flask.ext.mongoengine import MongoEngine
import os, sys
import datetime

app=Flask(__name__)

app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "my_tumble_log"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/AboutUs/')
def AboutUs():
    return render_template('AboutUs.html')

@app.errorhandler(404)
def page_not_found(e):
    return "<p>Page not found </p>"


print('Latest build at ' + str(datetime.datetime.now().time().hour) + ":" 
    + str(datetime.datetime.now().time().minute) + ":" 
    + str(datetime.datetime.now().time().second), file=sys.stderr)

if __name__=="__main__":
    app.run(debug=True)
