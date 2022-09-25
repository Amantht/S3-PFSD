import pymongo
_author_ = 'Aman'
uri = "mongodb+srv://aman:devmamata@cluster0.aqmkc3t.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(uri)
database = client['gryffindor']
collection = database['SortingHat']
def record():
        wizards = collection.find({})
        for person in wizards:
            print ("Are you afraid of what you'll hear?\nYour Animagus is a {}, {}".format(person['Animagus'],person['Member']))
record()