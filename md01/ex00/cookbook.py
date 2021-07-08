import datetime
from recipe import Recipe

class Cookbook:

    def __init__(self, name : str) -> None:
        self._name = name
        self._recipesList = {}
        self._creationDate = self._lastUpdate = datetime.date.today()
    
    def __str__(self) -> str:
        return(self._name)

    def get_recipe_by_name(self, name : str):
        if name not in self._recipesList:
            print("%s : Recipe %s not found" % (self._name, name))
            return
        print(str(self._recipesList[name]))
        return (self._recipesList[name])
    
    def get_recipes_by_types(self, recipe_type : str):
        if recipe_type not in Recipe._type:
            print ("Cookboook %s Invalid recipe type" % self._name)
            return None
        recipe_list = [str(recipe) for recipe in self._recipesList.values() if recipe._recipeType == recipe_type]
        return recipe_list
    
    def add_recipe(self, recipe : Recipe):
        if not isinstance(recipe, Recipe):
            print ("Cookbook %s add_recipe: invalid object type" % self._name)
            return
        self._recipesList[str(recipe)] = recipe
        self._lastUpdate = datetime.date.today()
