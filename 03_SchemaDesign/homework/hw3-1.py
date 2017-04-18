import pymongo

connection = pymongo.MongoClient()
db = connection.school
collection = db.students

it = collection.find()
for i in it:
    minIndex = None
    for index, score in enumerate(i['scores']):
        if score['type'] != 'homework':
            continue
        if minIndex == None or i['scores'][minIndex]['score'] > score['score']:
            minIndex = index

    del i['scores'][minIndex]

    collection.update_one({"_id": i['_id']}, {"$set":{"scores":i['scores']}})