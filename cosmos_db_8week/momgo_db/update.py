import pymongo
from decouple import config

url = config('mongodburl')
myclient = pymongo.MongoClient(url)
mydb = myclient["hrdb"]
mycol = mydb["book"]

def show():
    try:
        for book_result in mycol.find():
            print(book_result)
    except Exception as e:
        print(e)

# Update
show()
mycol.update_one(
    {"_id": 1},
    {
        "$set": {
            "boo_author": "Ram jadhav"
        }
    }
)
print("data Updated success full")
# read the data
show()