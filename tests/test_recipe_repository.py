from lib.recipe_repository import RecipeRepository
from lib.recipe import Recipe


def test_get_all_recipes(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    recipe = RecipeRepository(db_connection)
    assert recipe.all() == [
        Recipe(1, 'Spagetti Bolognese', 90, 4),
        Recipe(2, 'Packet Ramen', 5, 3),
        Recipe(3, 'Smoked Rat with Rosemary Potatoes', 60, 1),
        Recipe(4, 'Chicken Kebab', 60, 4),
        Recipe(5, 'Chilli con Carne', 120, 5)
    ]

def test_finds_single_recipe(db_connection):
    db_connection.seed("seeds/recipe_directory.sql")
    recipe = RecipeRepository(db_connection)
    assert recipe.find(3) == Recipe(3, 'Smoked Rat with Rosemary Potatoes', 60, 1)

