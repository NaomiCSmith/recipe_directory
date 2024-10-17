from lib.recipe import Recipe

class RecipeRepository():
    def __init__(self, _connection):
        self._connection = _connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM recipes')
        recipes_list = []
        for row in rows:
            item = Recipe(row["id"], row["title"], row["average_cooking_time"], row["rating"])
            recipes_list.append(item)
        return recipes_list
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM recipes WHERE id = %s', [id])
        row = rows[0]
        return Recipe(row["id"], row["title"], row["average_cooking_time"], row["rating"])