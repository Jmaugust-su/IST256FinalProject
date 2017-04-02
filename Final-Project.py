count = 0
def meal_selector():
    x = input("Are you making Breakfast, Lunch, Dinner, or Dessert? ").upper()
    if x == "BREAKFAST":
        #Search the web by filtering for only Breakfast recipes
        count == count + 1
    elif x == "LUNCH":
        #Search the web by filtering for only Lunch recipes
        count == count - 1
    elif x == "DINNER":
        #Search the web by filtering for only Dinner recipes
        count == count * 1
    elif x == "DESSERT":
        #Search the web by filtering for only Desser recipes
        count == count / 1


print("Welcome to Food Generator:")
meal_selector()
while True:
    y = input("Please Enter Your Ingredients and Press Enter When Finished: ")
    if y == "":
        break
