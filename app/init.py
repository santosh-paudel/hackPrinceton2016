from flask import Flask, render_template, request
from flask.ext.mongoengine import MongoEngine
from werkzeug.wrappers import Request, Response
from werkzeug.datastructures import ImmutableMultiDict
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
"""
@app.route('/like', methods=["GET", "POST"])
def like():

    if request.method=="POST":
        imd = request.form
        print(imd)
        print(imd.get('Like'))

    return render_template('index.html')
"""
@app.route('/', methods=["POST"])
def like():
    from app.models import User, Meme, Tag, Locale
    from app.Markov import URLEngine

    imd = request.form
    _url = imd.get('Like')
    print("GOT IT")
    print(imd)
    print(imd.get('Like'))

    img = Meme.objects(url=_url)[0]
    tagList = img.native_tags

    print(User.objects(userName="nmoon")[0].localeCount)

    for elem in tagList:
        print(elem)
        User.objects(userName="nmoon")[0].localeCount(key=elem)[0].value[0] = User.objects(userName="nmoon")[0].localeCount(key=elem)[0].value[0] + 1

    return render_template('index.html', URLid =_url)




@app.route('/')
def index(URLid =None):
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
