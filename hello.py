import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_details(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
        
    else:
        print(f"failed to retrieve information {response.status_code}")
    
    

pokemon_name = "pikachu"
pokemon_info = get_pokemon_details(pokemon_name)




    
 