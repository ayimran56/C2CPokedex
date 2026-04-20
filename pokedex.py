import requests

def get_pokemon(name):
    resp = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name.lower()}")
    
    if resp.status_code == 404:
        print(f"couldn't find {name}")
        return
    
    data = resp.json()
    
    print("Name:", data["name"])
    print("ID:", data["id"])
    print("Types:", [t["type"]["name"] for t in data["types"]])
    print("HP:", data["stats"][0]["base_stat"])
    print("Attack:", data["stats"][1]["base_stat"])
    print("Defense:", data["stats"][2]["base_stat"])
    print("Special Attack:", data["stats"][3]["base_stat"])
    print("Special Defense:", data["stats"][4]["base_stat"])
    print("Speed:", data["stats"][5]["base_stat"])

name = input("Enter a pokemon name: ")
get_pokemon(name)
