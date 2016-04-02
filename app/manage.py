import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server, Command
from init import app, db
from flask import Response
from app.models import *


manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)


class Hello(Command):
    "Prints hello world"
    def run(self):
        print("Hey there")


class InputBatchImages(Command):
    "Used to input batch images"
    def run(self):
        userInput = ""
        print("\n-----------------------------------------------------\n")
        print("Beginning batch image input")
        print("Prepare to upload many images to db")
        print("Enter exit() to stop")
        print("String lists are comma delimited\n")
        while userInput != "exit()":
            nativeTags = []
            foreignTags = []
            userInput = input("\tTitle:  ")
            if userInput == "exit()":
                break
            _title = userInput
            userInput = input("\tDescription:  ")
            if userInput == "exit()":
                break
            _description = userInput
            userInput = input("\tnumLikes:  ")
            if userInput == "exit()":
                break
            _numLikes = str(userInput)
            userInput = input("\turl:  ")
            if userInput == "exit()":
                break
            _url = userInput
            userInput = input("\tNative Tags:  ")
            if userInput == "exit()":
                break
            _nativeTags = userInput.split(", ")
            userInput = input("\tForeign Tags:  ")
            if userInput == "exit()":
                break
            _foreignTags = userInput.split(", ")
            userInput = ""
            print("\n")

            meme = Meme(title=_title, description=_description, numLikes=_numLikes, url=_url, native_tags=_nativeTags, foreign_tags=_foreignTags)
            meme.save()


        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")


manager.add_command('batchimages', InputBatchImages())
manager.add_command('hello', Hello())



if __name__ == "__main__":
    manager.run()