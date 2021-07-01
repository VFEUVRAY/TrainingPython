from recipe import Recipe
from cookbook import Cookbook

testRecipe = Recipe("pizza", 5, 23, ["tomato", "dough"], "starter", "italy")
testCook = Cookbook("MyFirstCookBook")

print(str(testCook))

testCook.add_recipe(testRecipe)
testCook.add_recipe(Recipe("salad", 2, 21, ["lettuce"], "starter", "frence"))
testCook.add_recipe(Recipe("cake", 4, 80, ["flour", "eggs", "sugar"], "dessert", "poland"))
testCook.get_recipe_by_name("pizza")
print(testCook.get_recipes_by_types("dessert"))
testCook.add_recipe("error")
print(testCook._recipesList['pizza']._recipeType)