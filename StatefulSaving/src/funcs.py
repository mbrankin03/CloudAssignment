from tinydb import TinyDB, Query
import json
import uuid

def insertInDB(db, x):
    if x == "":
        return "No string provided"
    key = str(uuid.uuid4())
    db.insert({'Key': key, 'String': x})
    return key

def getFromDB(db, searchKey):
    Key = Query()
    answer = db.get(Key.Key == searchKey)
    if answer == None:
        return "Key does not exist in our database"
    string = answer['String']
    return string

