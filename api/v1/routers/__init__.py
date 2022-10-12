from fastapi import APIRouter, status, Form, HTTPException, Depends, Path, Request
from api.v1.models import pokedex as pd

router = APIRouter(
    prefix='/v1',
    tags=['v1']
)

@router.get("/pokemon", status_code=status.HTTP_200_OK)
def filter_pokemon(request: Request):
    """
    Filter pokemon by path query. (Query value need not match exactly)
    e.g. ?name=char (Will return Charmander, Charmeleon, and Charizard entries)
    """
    print(request.query_params)
    return pd.filter_pokedex(**request.query_params)

@router.get("/pokemon/{id}", status_code=status.HTTP_200_OK)
def pokemon_by_number(id: int):
    """Return pokedex entry for pokemon whose number matches `id`"""
    try:
       return pd.filter_pokedex(num=str(id).rjust(3, '0'))
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)