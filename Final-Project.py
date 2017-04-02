def meal_selector():
    x = input("Are you making Breakfast, Lunch, Dinner, or Dessert?").upper()
    if x == "BREAKFAST":
        #Search the web by filtering for only Breakfast recipes
    elif x == "LUNCH":
        #Search the web by filtering for only Lunch recipes
    elif x == "DINNER":
        #Search the web by filtering for only Dinner recipes
    elif x == "DESSERT":
        #Search the web by filtering for only Desser recipes


print("Welcome to Food Generator:")
while True:
    y = input("Please Enter Your Ingredients and Press Enter When Finished: ")
    if y == "":
        break
