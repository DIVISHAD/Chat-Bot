import pymongo
from cryptography import encrypted_text,decrypted_text

client = pymongo.MongoClient("mongodb+srv://divishad:221B%40221B@cluster0-gdmit.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.DarwinBot

def validate_db(username,password):
    cipher=encrypted_text(password,username)
    res = db.users.find( {"username":username, "password":cipher} ).count()
    if(res >= 1):
        return {"response":"valid"}
    else: 
        return {"response":"invalid"}    