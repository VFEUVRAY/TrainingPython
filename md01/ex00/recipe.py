class Recipe:
    _type = ("starter", "lunch", "dessert")
    def __init__(self, name : str, cooking_lvl : int, cooking_time : int, ingredients : list, recipe_type : str, description = None) -> None:
        if cooking_lvl > 5 or cooking_lvl < 1:
            raise ValueError("Invalid cooking lvl")
        if recipe_type not in self._type:
            raise ValueError("Invalid recipe type")
        if cooking_time < 1:
            raise ValueError("Recipe: Cooking cannot be negative")
        self._name = name
        self._cookingLvl = cooking_lvl
        self._cookingTime = cooking_time
        self._ingredients = ingredients
        self._recipeType = recipe_type
        self._description = description
    
    def __str__(self) -> str:
        return (self._name)

