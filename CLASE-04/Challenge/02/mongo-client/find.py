import pymongo

client = pymongo.MongoClient("mongodb://m1:27017/")
db = client["m1"]

# Obtén un registro
print("Imprime un registro\n", db.pet.find_one(), "\n")

# Obtén todos los registros
print("Imprime todos los registros")
for pet in db.pet.find():
    print(pet)