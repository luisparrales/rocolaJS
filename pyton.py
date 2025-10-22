import requests

def get_water_pokemon():
    """
    Retrieves a list of all water-type Pokemon from the PokeAPI.

    Returns:
        list: A list of Pokemon names that are water-type.
    """
    url = "https://pokeapi.co/api/v2/type/water"
    response = requests.get(url)
    data = response.json()
    pokemon_list = [pokemon['pokemon']['name'] for pokemon in data['pokemon']]
    return pokemon_list

if __name__ == '__main__':
    water_pokemon = get_water_pokemon()
    print("List of Water-type Pokemon:")
    for pokemon in water_pokemon:
        print(pokemon)