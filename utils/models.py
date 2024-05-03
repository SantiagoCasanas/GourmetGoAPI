from typing import List
from pydantic import BaseModel

class Recipe(BaseModel):
    """
    Represents a recipe with its title, introduction, ingredients, and instructions.
    """
    title: str
    intro: str
    ingredients: List[str]
    instructions: List[str]

class Ingredients(BaseModel):
    """
    Represents a list of ingredients.
    """
    ingredients: List[str]