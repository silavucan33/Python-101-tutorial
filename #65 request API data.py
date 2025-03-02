# How to connect to an API using Python

#we're going to connect on the poke API to get some information on a Pokemon of our choosing

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    #this method is going to return a response object

    #our response object does have an attribute of status code to read what the status code is
    #it's something like '404 Not found' error code.
    #200 status code means that the response is okay
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        #our 'response' is a json format. using this method we'll convert it to a python dictionary. it will consist of key value pairs much like a json file
    else:
        print(f"Failed to retrieve data {response.status_code}")

pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)
#remember that your parameters can be named different then your arguments
#when you send data to a function you can rename it to something else temporarily

if pokemon_info: #if our dictionary exists we can use the if keyword. if pokemon_info is true; if it exists this will be true
    #to access the value of a dictionary, we can access it by a key
    print(f"Name: {pokemon_info["name"].capitalize()}") #access the key of 'name'
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

