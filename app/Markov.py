
from app.models import *
import copy
import random
import math

#----------------------------------------------------------


class Node:
    def __init__(self, _descriptor, _probability):
        self.descriptor = _descriptor
        self.probability = _probability



#----------------------------------------------------------


class URLEngine:
    def __init__(self, _user):
        self.collection = Locale
        self.nodes = []
        self.user = _user
        self.totalProbability = 0
        self.totalInfluences = 0

        for elem in _user.localeCount:
            self.totalInfluences = self.totalInfluences + elem.value

        for elem in self.user.localeCount:
            if elem.value == 0:
                continue
            d = elem.key
            p = int((elem.value/self.totalInfluences)*100)
            m = Node(d, p)
            self.nodes.append(copy.copy(m))
            self.totalProbability += p


    def getNextURL(self):
        _locale = self.generateLocale()
        tagList = Tag.objects(locale=_locale)
        if not tagList:
            return self.generateRandomURL()
        else:
            return self.generateRandomURLWithTags(tagList)


    def generateLocale(self):
        dartBoard = []
        for i in self.nodes:
            for j in range(0, i.probability):
                dartBoard.append(i.descriptor)
        index = random.randrange(0, len(dartBoard))
        return dartBoard[index]


    def generateRandomURL(self):
        memes = Meme.objects;
        index = random.randrange(0, len(memes))
        return memes[index].url

    def generateRandomURLWithTags(self, tags):
        # Probability of a choice from disjoint domain is always atleast 30%
        disjointProbability = int(math.ceil(len(tags)/3))
        if disjointProbability < 2:
            disjointProbability = 2

        dartBoard = []
        for i in range(0, disjointProbability):
            dartBoard.append("_Disjoint_")

        for elem in tags:
            dartBoard.append(elem.tag)

        index = random.randrange(0, len(dartBoard))

        if dartBoard[index] == "_Disjoint_":
            return self.generateRandomURL()
        else:
            memes = Meme.objects(native_tags=dartBoard[index])
            if len(memes) != 0:
                tmp = random.randrange(0, len(memes))
                return memes[tmp].url
            else:
                return self.generateRandomURL()








#----------------------------------------------------------



