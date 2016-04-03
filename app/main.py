from flask import Flask, render_template, request
from Markov import URLEngine
#from Markov import UserDomain
from init import db
from models import *
app = Flask(__name__)


@app.route('/')
@app.route('/<username>')
def index(username=None):
    userList = User.objects(userName=username)

    if not userList:
        print("Invalid username")
        return

    user = userList[0]
    print(username)
    urlID = URLEngine(user)

    return render_template("index.html")#, urlID = urlID)


if __name__ == '__main__':
    app.run()