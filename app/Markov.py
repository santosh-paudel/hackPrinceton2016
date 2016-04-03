
from init import db
import copy

class MarkovNode:
    def __init__(self, _descriptor, _probability):
        self.descriptor = _descriptor
        self.probability = _probability




#----------------------------------------------------------


class UserDomain:
    def __init__(self, _user, _collection, _collectionString):
        self.collection = _collection
        self.nodes = []
        print(len(collection.objects))

        self.totalInfluences = 0
        for elem in _user.localeCount:
            totalInfluences = totalInfluences + elem.value

        for elem in _user.localeCount:
            if elem.value == 0:
                continue
            d = elem.key
            p = int((elem.value/totalInfluences)*100)
            m = MarkovNode(d, p)
            nodes.append(copy.copy(m))

        for elem in nodes:
            print(elem.descriptor + "\t" + str(elem.probability))


    







#----------------------------------------------------------



