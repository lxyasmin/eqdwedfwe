from pymongo import MongoClient


client = MongoClient('mongodb+srv://yasmin:yasmin@cluster0.yrjugsf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db = client.belajarDb5

# Insert One --> Menambahkan satu data ke database
# db.test.insert_one({'nama':'al','group':'grup3'})

# Insert Many --> Menambahkan banyak data ke database
data = [{'nama':'ulil','group':'grup3'},{'nama':'bela','group':'grup3'}]
# db.test.insert_many(data)

#Find All 
datas = list(db.test.find())
# print(datas)

# Find One 
nama = db.test.find_one({"nama":"ulil"})
# print(nama)

#Regex 
search = 'l'
find = db.test.find_one({"nama": {"$regex": search}})
print(find)

#Update
# db.test.update_one(
#     {'nama': 'ulil'},
#     {'$set': {'nama': 'linda'}})

#Alter Key 
# db.test.update_many({},{'$rename':{"grup3":'namagrup'}})

db.test.delete_many({'namagrup': 'grup3'})
