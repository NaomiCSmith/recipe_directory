from lib.recipe import Recipe

def test_recipe_constructs():
    recipe = Recipe(1, "Choc Cookies", 60, 5)
    assert recipe.id == 1
    assert recipe.title == "Choc Cookies"
    assert recipe.average_cooking_time == 60
    assert recipe.rating == 5

def test_recipe_formats_correctly():
    recipe = Recipe(2, "Ice Cream Float", 5, 4)
    assert recipe.__repr__() == "Recipe(2, Ice Cream Float, 5 minutes, 4 stars)"

def test_recipes_are_equal():
    recipe1 = Recipe(5, "Boiled Snake", 45, 3)
    recipe2 = Recipe(5, "Boiled Snake", 45, 3)
    assert recipe1 == recipe2
