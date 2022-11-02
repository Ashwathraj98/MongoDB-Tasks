import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["myTD"]
mycol = mydb["directory"]

#creating collection
mylist = [{"Name": "nishita", "Phone_no": 9216423891, "Place": "jind"},{"Name": "nardeep", "Phone_no": 9896087651, "Place": "punjab"},{"Name": "sachin", "Phone_no": 7988123456, "Place": "kurukshetra"},{"Name": "sunder", "Phone_no": 9817347891, "Place": "jind"},{"Name": "neha", "Phone_no": 9012223491, "place": "uttarpradesh"},{"Name": "raman", "Phone_no": 7988098761, "Place": "kurukshetra"}]
x = mycol.insert_many(mylist)
for x in mycol.find():
   print(x)

#updating values
myquery = { "Name": "nishita" }
newvalues = { "$set": { "gender": "female" } }

x=mycol.update_one(myquery, newvalues)

for x in mycol.find():
    print(x)

#replacing values
myquery = { "Name": "nardeep" }
newvalues = { "$set": { "Place": "xxx" } }

x=mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)

#deleting values
myquery = { "Name": "nardeep" }
x=mycol.delete_one(myquery)
for x in mycol.find():
    print(x)





