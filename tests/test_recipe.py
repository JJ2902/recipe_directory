from lib.recipe import *

# When I construct an recipe
# With the fields name, average_cooking_time and rating
# They are reflected in the instance properties

def test_construct_with_fields():
    recipeOne = Recipe(1,'Risotto', 45, 4)
    assert recipeOne.id == 1
    assert recipeOne.name == 'Risotto'
    assert recipeOne.average_cooking_time == 45
    assert recipeOne.rating == 4

