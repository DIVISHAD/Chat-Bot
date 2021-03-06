import pymongo
import random

client = pymongo.MongoClient("mongodb+srv://divishad:221B%40221B@cluster0-gdmit.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.DarwinBot

def botResponse(input, uname):
    res = db.bot_chat.find_one({"user":input})
    if(db.chat_history.find_one( {"username":uname}) == None):
        db.chat_history.insert_one( {"username":uname,"bot":["Hey,"+uname+"!"],"user":[input] } )
    else:
        db.chat_history.update_one( {"username":uname}, {"$push":{"user":input}} )
    if(res == None):
        reply = "Sorry!I can't understand what you are asking about!!"
        db.chat_history.update_one( {"username":uname}, {"$push":{"bot":reply}} )
        return reply
    indx=random.randrange(0, len(res["response"])) 
    db.chat_history.update_one( {"username":uname}, {"$push":{"bot":res["response"][indx]}} )   
    return res["response"][indx] 

def chat_history(username):
    chat = db.chat_history.find_one( {"username":username} )
    if(chat == None):
        return ""
    return chat    