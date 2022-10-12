import os
import json


def _get_pokedex():
    """Load pokedex into memory."""
    full_path = os.path.dirname(__file__)
    f = open(f'{full_path}/pokedex.json')
    data = json.load(f)
    return data['pokemon']

POKEDEX = _get_pokedex()

def filter_pokedex(**kwargs):
    if len(kwargs) == 0:
        return POKEDEX

    def matches_filters(pokemon):
        for key, value in kwargs.items():
            if str(value).lower() not in str(pokemon[key]).lower():
                    return False
        return True
    
    filtered = list(filter(matches_filters, POKEDEX))
    return filtered