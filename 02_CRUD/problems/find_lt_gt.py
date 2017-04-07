import pymongo
import sys

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

# get a handle to the school database
db=connection.school
scores = db.scores


def find():

    print "find, reporting for duty"

    query = {'type':'quiz', 'score':{'$gt': 20, '$lt': 90}}

    try:
        iter = scores.find(query)

    except Exception as e:
        print "Unexpected error:", type(e), e

    return iter

it = find()

for i in it:
    print i