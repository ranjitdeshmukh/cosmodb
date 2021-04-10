import pymongo

import pymongo
from decouple import config

url = config('mongodburl')
myclient = pymongo.MongoClient(url)
mydb = myclient["hrdb"]
mycol = mydb["book"]

# insert0

book = {
    '_id' : 1,
    'bookid' : 101,
    'book_name' : "mrutunjay",
    'boo_author' : "Shivaji Savant",
    'book_price' : 420   
}
mycol.insert_one(book)

# read the data

for book_result in mycol.find():
    print(book_result)
