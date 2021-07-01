cookbook = {
    "sandwich" : (["bread", "ham", "salad"], "lunch", 10),
    "cake" : (["flour", "sugar", "egg"], "dessert", 60),
    "salad" : (["lettuce", "croutons", "tomatoes"], "entree", 6),
}

def get_recipe(name = None):
    if (name is None):
        name = input ("enter name of recipe\n")
    if (name not in cookbook):
        print("Recipe not found")
        return
    print ("ingredients: " + ",".join(['%s']*len(cookbook[name][0])) % tuple(cookbook[name][0]) + "\ntype: %s\nprep time: %d minutes" % tuple(cookbook[name][1:]))

def delete_recipe():
    name = input ("enter name of recipe\n")
    if (name not in cookbook):
        print ("Recipe not found")
        return
    cookbook.__delitem__(name)
    print(cookbook)

def add_recipe():
    recipe_name = input("Enter name of new recipe\n")
    recipe_ingredients = str(input("Enter ingrendients, seperated by a comma\n")).split(', ')
    recipe_type = str(input("Enter meal type\n"))
    recipe_prep = 0
    while (not recipe_prep):
        recipe_prep = int(input("Enter recipe prep time in minutes\n"))
    cookbook[recipe_name] = tuple([recipe_ingredients, recipe_type, recipe_prep])
    

def get_cookbook():
    for recipe in cookbook.keys():
        print ("\n" + recipe + ":")
        get_recipe(recipe)

for key in cookbook.keys():
    print(key)
for value in cookbook.values():
    print(value)
for item in cookbook.items():
    print(item)
print (cookbook.keys())

#get_recipe("cake")
switcher = {
    1 : get_recipe,
    2 : delete_recipe,
    3 : add_recipe,
    4 : get_cookbook,
}
prompt = "1: get recipe\n2: Delete recipe\n3: Add recipe\n4: Get Cookbook\n5: quit\n\nEnter desired action:\n"
user_input = 0
while (user_input != 5):
    user_input = int(input(prompt))
    if user_input not in switcher:
        print ("Invalid Key\n")
    else:
        switcher[user_input]()
    
print ("Goodbye")