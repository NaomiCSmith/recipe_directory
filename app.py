from lib.database_connection import DatabaseConnection
from lib.recipe_repository import RecipeRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/recipe_directory.sql")

# Retrieve all artists
recipe_repository = RecipeRepository(connection)
recipes = recipe_repository.all()

# List them out
for recipe in recipes:
    print(recipe)

# Find specific recipe
print(recipe_repository.find(2))