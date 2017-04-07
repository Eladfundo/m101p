import pymongo


# Copyright 2012-2016, 10gen, Inc.
# Author: Andrew Erlichson


# connect to the db on standard port
connection = pymongo.MongoClient("mongodb://localhost")



db = connection.students       # attach to db
collection = db.grades         # specify the collection

it = collection.find({'type':'homework'}).sort([('student_id', pymongo.ASCENDING),('score', pymongo.ASCENDING)]);
prev_student_id = None
for i in it:
    if (prev_student_id <> i['student_id']):
        print 'Remove', i
        collection.delete_one({'_id':i['_id']})
    prev_student_id = i['student_id']

