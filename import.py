import pymongo
 from pymongo import MongoClient
    mongoClient = MongoClient("mongodb://localhost/pokemon.csv")
     pokemonDB = mongoClient['pokemondb']
     pokemonColl = pokemonDB['pokemon_data']

     pikachuquery = { "name": "Pikachu" }
     pikachu = pokemonColl.find_one(pikachuquery)
    
      print("I found " + str(pokemonColl.count_documents({})) + " pokemon")
