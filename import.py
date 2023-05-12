from pymongo import MongoClient
mongoClient = MongoClient("mongodb://localhost/pokemon.csv")
pokemonDB = mongoClient["pokemondb"]
pokemonColl = pokemonDB["pokemon_data"]

myquery = {"name" : "Pikachu"}
pikachu = pokemonColl.find(myquery)

for x in pikachu:
    print(x)

