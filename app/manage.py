import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask_script import Manager, Server, Command
from init import app, db
from flask import Response
from app.models import *
from Markov import *
import copy

manager = Manager(app)

# Turn on debugger by default and reloader
manager.add_command("runserver", Server(
    use_debugger = True,
    use_reloader = True,
    host = '0.0.0.0')
)

#------------ System tools -------------------



def retrieveLocaleDictionary():
    userInput = ""
    localeList = []
    for elem in Locale.objects:
        dict = Dictionary()
        userInput = input("\tEnter number of influences on locale " + elem.locale + ": ")
        dict.key=elem.locale
        dict.value=userInput
        localeList.append(copy.copy(dict))

    return localeList







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
            _localCount = retrieveLocaleDictionary()
            userInput = ""
            print("\n")

            user = User(firstName=_firstName, lastName=_lastName, email=_email, userName=_userName, password=_password, localeCount=_localCount)
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



class MemeInputBatchFile(Command):
    "Loading in batch memes from file"
    def run(self):
        print("\n-----------------------------------------------------\n")
        print("Beginning batch meme input from file")
        print("Prepare to upload many memes to db")
        print("String lists are comma delimited\n")
        path = input("\tPlease enter a path to file: ")
        f = open(path, "r")
        if f.closed:
            print("\tFile error.  Terminating command.")
            return

        content = f.read()
        objects = content.split("~\n")
        lines = []
        for elem in objects:
            lines.append(elem.split("\n"))

        counter = 1
        for elem in lines:
            print(elem)
            _title = elem[0]
            if _title == "":
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _description = elem[1]
            if _description == "":
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _url = elem[2]
            if _url == "":
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _nativeTags = elem[3].split(",")
            if _nativeTags == []:
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _numLikes = int(elem[4])
            if _numLikes < 0:
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _numShares = int(elem[5])
            if _numShares < 0:
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue
            _numDownloads = int(elem[6])
            if _numDownloads < 0:
                print("\tObject " + str(counter) + " failed to load")
                counter = counter+1
                continue

            meme = Meme(title=_title, description=_description, numLikes=_numLikes, url=_url, native_tags=_nativeTags, foreign_tags=[], numShares=_numShares, numDownloads=_numDownloads)
            meme.save()
            print("\tObject " + str(counter) + " saved successfully")
            counter = counter + 1

        print("\nBatch input terminated")
        print("\n-----------------------------------------------------\n")




class test(Command):
    "A quickie testie"
    def run(self):
        m = UserDomain(User.objects(userName="nmoon")[0], Locale, "Locale")





# Add commands to the manager here

manager.add_command('batchimages', ImageInputBatch())
manager.add_command('batchusers', UserInputBatch())
manager.add_command('batchtags', TagInputBatch())
manager.add_command('batchlocales', LocaleInputBatch())
manager.add_command('test', test())
manager.add_command('batchmemesfile', MemeInputBatchFile())




if __name__ == "__main__":
    manager.run()