import pymongo
from cryptography import encrypted_text

client = pymongo.MongoClient("mongodb+srv://divishad:221B%40221B@cluster0-gdmit.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.DarwinBot

def add_user(data):
    res = db.users.find( { "username":data["username"] } ).count()
    if (res >= 1):
        return {"response":"invalid_uname"}
    else :
        data["password"] = encrypted_text(data["password"], data["username"])
        res = db.users.insert_one(data)
        if(res != None):
            return {"response":"signedup"}
