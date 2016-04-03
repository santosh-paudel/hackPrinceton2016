from flask import Flask, render_template, request
from flask.ext.mongoengine import MongoEngine
import os, sys
import datetime
#from Markov import URLEngine

app=Flask(__name__)

app.config["MONGODB_SETTINGS"] = {'DB': "wememe"}
app.config["SECRET_KEY"] = "KeepThisS3cr3t"

db = MongoEngine(app)

class Dictionary(db.EmbeddedDocument):
    key = db.StringField(max_length=30, required=True)
    value = db.IntField(min_value=0)

    def __unicode__(self):
        return self.key


# @app.route('/AboutUs/')
# def AboutUs():
#     return render_template('AboutUs.html')

# @app.errorhandler(404)
# def page_not_found(e):
#     return "<p>Page not found </p>"


# @app.route('/login/')
# def userLogin():
# 	return render_template("pictures.html");


@app.route('/')
@app.route('/', methods=["GET", "POST"])
def index(URLid =None):

    if request.method=="POST":
        print(request.form['name'])


    from app.models import User
    from app.Markov import URLEngine
    userList = User.objects(userName="nmoon")
    user = userList[0]
    Engine = URLEngine(user)
    URLid = Engine.getNextURL()
    print("ID:\t" + str(URLid))
    return render_template('index.html', URLid =URLid)






print('Latest build at ' + str(datetime.datetime.now().time().hour) + ":" 
    + str(datetime.datetime.now().time().minute) + ":" 
    + str(datetime.datetime.now().time().second), file=sys.stderr)

if __name__=="__main__":
    app.run(debug=True)
