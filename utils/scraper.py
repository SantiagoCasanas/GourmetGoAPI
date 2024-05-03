from typing import List
import requests
import bs4
import re

from utils.models import Recipe

def _generate_intro_recipe_url(ingredients: List[str]) -> str:
    """
    Generate the URL for searching recipes based on provided ingredients.

    Args:
        ingredients (List[str]): A list of ingredients.

    Returns:
        str: The generated URL.
    """
    url = "https://www.recetasgratis.net/busqueda?q="
    
    if len(ingredients) == 1:
        url += ingredients[0]
    elif len(ingredients) > 1:
        url += ingredients.pop(0)
        for ingredient in ingredients:
            url += f"+{ingredient}"
    
    return url

def _get_page(url: str) -> bs4.BeautifulSoup:
    """
    Get the HTML content of a web page.

    Args:
        url (str): The URL of the web page.

    Returns:
        bs4.BeautifulSoup: The parsed HTML content.
    """
    page = requests.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    return soup

def get_info_recipes(page: bs4.BeautifulSoup) -> Recipe:
    """
    Extract recipe information from a web page.

    Args:
        page (bs4.BeautifulSoup): The parsed HTML content of the web page.

    Returns:
        dict: A dictionary containing recipe information.
    """
    try:
        title_page = page.find_all(class_="header-post")[0]
        info_page = page.find_all(class_="intro")[0]
        info_ingredients = page.find_all(class_="ingrediente")
        info_instructions = page.find_all(class_="apartado")

        if isinstance(title_page, bs4.Tag):
            title_text = title_page.h1.text
            title = re.sub('RecetasGratis.net', 'GoumertGo', title_text)

        if isinstance(info_page, bs4.Tag):
            intro_text = info_page.p.text
            intro = re.sub('RecetasGratis.net', 'GoumertGo', intro_text)
        
        ingredients = []
        for ingredient in info_ingredients:
            if len(ingredient.attrs['class']) == 1:
                ingredient_text = ingredient.text.strip()
                ingredient_text = re.sub(r'\s+', ' ', ingredient_text)
                ingredient_text = re.sub('RecetasGratis.net', 'GoumertGo', ingredient_text)
                ingredients.append(ingredient_text)

        instructions = []
        for instruction in info_instructions:
            if instruction.attrs.get('id', None) is not None:
                instruction_text = instruction.text.strip()
                instruction_text = re.sub(r'\s+', ' ', instruction_text)
                instruction_text = re.sub('RecetasGratis.net', 'GoumertGo', instruction_text)
                instructions.append(instruction_text)

        info_recipe = Recipe(
            title=title,
            intro=intro,
            ingredients=ingredients,
            instructions=instructions
        )

        return info_recipe
    except:
        return None

def get_recipes(ingredients: List[str]) -> List[Recipe]:
    """
    Get a list of recipes using the provided ingredients.

    Args:
        ingredients (List[str]): A list of ingredients.

    Returns:
        List[str]: A list of recipe information dictionaries.
    """
    url = _generate_intro_recipe_url(ingredients)
    page = _get_page(url)
    intro_recipes = page.find_all(class_="resultado link")
    recipes = []
    counter = 0
    for recipe in intro_recipes:
        if counter > 3:
            break
        for content in recipe:
            if isinstance(content, bs4.Tag):
                if content.name == 'a':
                    link = content.get('href', None)
                    page_recipe = _get_page(link)
                    info = get_info_recipes(page_recipe)
                    if info:
                        recipes.append(info)
                        counter += 1
    return recipes