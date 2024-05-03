import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from dotenv import load_dotenv
from utils.models import Recipe, Ingredients
from utils.scraper import get_recipes
from typing import List

# Load environment variables from the .env file
load_dotenv()

# Initialize the FastAPI application
app = FastAPI()

# Get allowed origins from environment variables
origins = os.getenv('origins')

# Configure CORS middleware to allow requests from specified origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "hello world"}

# Endpoint to get a list of recipes using the provided ingredients
@app.post("/get-recipes")
def get_recipes_url(ingredients: Ingredients) -> List[Recipe]:
    # Get the recipe using the provided ingredients
    results = get_recipes(ingredients.ingredients)
    return results