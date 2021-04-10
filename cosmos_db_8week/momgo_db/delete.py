import pymongo
from decouple import config

url = config('mongodburl')
myclient = pymongo.MongoClient(url)
mydb = myclient["hrdb"]
mycol = mydb["book"]

# Delete

mycol.delete_one(
    {"_id": 1}
)
print("data Delted success full")
# read the data

for book_result in mycol.find():
    print(book_result)
