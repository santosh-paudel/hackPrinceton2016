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



# Define Command scripts



# Batch input for images, one by one, but batch
class ImageInputBatch(Command):
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
            userInput = input("\tnumShares:  ")
            if userInput == "exit()":
                break
            _numShares = str(userInput)
            userInput = input("\tnumDownloads:  ")
            if userInput == "exit()":
                break
            _numDownloads = str(userInput)
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

            meme = Meme(title=_title, description=_description, numLikes=_numLikes, url=_url, native_tags=_nativeTags, foreign_tags=_foreignTags, numShares=_numShares, numDownloads=_numDownloads)
            meme.save()
            print("\tData entry saved.")
            print("\t-------------------------\n")


        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")

class UserInputBatch(Command):
    "Used to enter batch users"
    def run(self):
        userInput = ""
        print("\n-----------------------------------------------------\n")
        print("Beginning batch user input")
        print("Prepare to upload many users to db")
        print("Enter exit() to stop")
        print("String lists are comma delimited\n")
        while userInput != "exit()":
            userInput = input("\tfirstName:  ")
            if userInput == "exit()":
                break
            _firstName = userInput
            userInput = input("\tLastName:  ")
            if userInput == "exit()":
                break
            _lastName = userInput
            userInput = input("\temail:  ")
            if userInput == "exit()":
                break
            _email = str(userInput)
            userInput = input("\tuserName:  ")
            if userInput == "exit()":
                break
            _userName = userInput
            userInput = input("\tpassword:  ")
            if userInput == "exit()":
                break
            _password = userInput
            userInput = ""
            print("\n")

            user = User(firstName=_firstName, lastName=_lastName, email=_email, userName=_userName, password=_password)
            user.save()
            print("\tData entry saved.")
            print("\t-------------------------\n")


        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")


class TagInputBatch(Command):
    "Used to enter batch tags"
    def run(self):
        userInput = ""
        print("\n-----------------------------------------------------\n")
        print("Beginning batch tag input")
        print("Prepare to upload many tag to db")
        print("Enter exit() to stop")
        print("String lists are comma delimited\n")
        while userInput != "exit()":
            userInput = input("\tTag:  ")
            if userInput == "exit()":
                break
            _tag = userInput
            userInput = input("\tLocale:  ")
            if userInput == "exit()":
                break
            _locale = userInput
            userInput = ""
            print("\n")

            tag = Tag(tag=_tag, locale=_locale)
            tag.save()
            print("\tData entry saved.")
            print("\t-------------------------\n")


        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")


class LocaleInputBatch(Command):
    "Used to enter batch tags"
    def run(self):
        userInput = ""
        print("\n-----------------------------------------------------\n")
        print("Beginning batch locale input")
        print("Prepare to upload many locales to db")
        print("Enter exit() to stop")
        print("String lists are comma delimited\n")
        while userInput != "exit()":
            userInput = input("\tLocale:  ")
            if userInput == "exit()":
                break
            _locale = userInput

            userInput = ""
            print("\n")

            __locale = Locale(locale=_locale)
            __locale.save()
            print("\tData entry saved.")
            print("\t-------------------------\n")


        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")



class test(Command):
    "A quickie testie"
    def run(self):
        print(db.Tag.count())




# Add commands to the manager here

manager.add_command('batchimages', ImageInputBatch())
manager.add_command('batchusers', UserInputBatch())
manager.add_command('batchtags', TagInputBatch())
manager.add_command('batchlocales', LocaleInputBatch())
manager.add_command('test', test())










if __name__ == "__main__":
    manager.run()