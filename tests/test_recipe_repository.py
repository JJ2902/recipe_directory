from lib.recipe_repository import *
from lib.recipe import *
from lib.database_connection import *

# when I call #all on the recipeRepository
# I get all the recipe back in a list

def test_list_all_recipes(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.all()
    assert result == [
        Recipe(1,'Risotto', 45, 4),
        Recipe(2,'Miso Aubergine', 20, 3),
        Recipe(3,'BBQ Pork', 35, 5),
        Recipe(4,'Tuna Mayo Rice', 15, 3),
        Recipe(5,'Beef Stew', 67, 5),
        Recipe(6,'Omelette', 10, 2)
    ]

"""
when we call #find with an id
we get the record with id
"""

def test_find(db_connection):
    db_connection.seed("seeds/recipes.sql")
    repository = RecipeRepository(db_connection)
    result = repository.find(3)
    assert result == Recipe(3,'BBQ Pork', 35, 5)