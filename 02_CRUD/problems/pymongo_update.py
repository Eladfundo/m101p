#!/usr/bin/env python
import pymongo

# establish a connection to the database
connection = pymongo.MongoClient("mongodb://localhost")

def using_set():

    print "updating record using set"
    # get a handle to the school database
    db = connection.school
    scores = db.scores


    try:
        # get the doc
        score = scores.find_one({'student_id': 1, 'type': 'homework'})
        print "before: ", score

        # update using set
        scores.update_one({'student_id':1, 'type':'homework'},
                          {'$set': {'examiner': "Jones"}})

        score = scores.find_one({'student_id': 1, 'type': 'homework'})
        print "after: ", score

    except:
        print "Unexpected error:", sys.exc_info()[0]
        raise

using_set()