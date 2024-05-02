from typing import List, Dict
import requests as _requests
import bs4 as _bs4


def _generate_intro_recipe_url(ingredients: List[str]) -> str:
    url = "https://www.recetasgratis.net/busqueda?q="
    
    if len(ingredients) == 1:
        url = url+ingredients[0]
    elif len(ingredients) > 1:
        url = url+ingredients.pop(0)
        for ingredient in ingredients:
            url = f"{url}+{ingredient}"
    
    return url


def _get_page(url: str) -> _bs4.BeautifulSoup:
    page = _requests.get(url)
    soup = _bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def get_info_recipes(page: _bs4.BeautifulSoup) -> dict:
    title_page = page.find_all(class_="header-post")[0]
    info_page = page.find_all(class_="intro")[0]

    if isinstance(title_page, _bs4.Tag):
        title = title_page.h1.text.encode('utf-8').decode('utf-8')

    if isinstance(info_page, _bs4.Tag):
        intro = info_page.p.text.encode('utf-8').decode('utf-8')
    
    
    

def get_recipes(ingredients: list) -> List[str]:
    url = _generate_intro_recipe_url(ingredients)
    page = _get_page(url)
    intro_recipes = page.find_all(class_="resultado link")
    recipes = []
    for recipe in intro_recipes[0]:
        if isinstance(recipe, _bs4.Tag):
            if recipe.name == 'a':
                link = recipe.get('href', None)
                title = recipe.text
                page_recipe = _get_page(link)
                get_info_recipes(page_recipe)

                recipes.append({'title': title, 'link': link})
    return recipes

recipes = get_recipes(['papa', 'arroz'])
