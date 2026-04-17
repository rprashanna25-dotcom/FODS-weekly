"""
this program creates a dish class to hold dish information
it also includes a cookbook class to handle multiple dishes
the user can input new dishes and view all saved dishes
"""

class Dish:
    """
    class to represent a single dish
    """
    def __init__(self, dish_id, dish_name, ingredients, instructions):
        """
        initialize dish attributes
        """
        self.dish_id = dish_id
        self.dish_name = dish_name
        self.ingredients = ingredients
        self.instructions = instructions
    def display(self):
        """
        display dish details
        """
        print("\ndish details")
        print("-" * 30)
        print(f"dish id: {self.dish_id}")
        print(f"dish name: {self.dish_name}")
        print(f"ingredients: {self.ingredients}")
        print(f"instructions: {self.instructions}")
class Cookbook:
    """
    class to manage collection of dishes
    """
    def __init__(self):
        """
        initialize empty dish list
        """
        self.dishes = []
    def addition_dish(self, dish):
        """
        add a dish to cookbook
        """
        self.dishes.append(dish)
    def display(self):
        """
        display all dishes in cookbook
        """
        if not self.dishes:
            print("no dishes available")
            return
        print("\nall dishes in cookbook")
        print("=" * 40)
        for dish in self.dishes:
            dish.display()
# create cookbook object
cookbook = Cookbook()

# loop to take multiple dishes
while True:
    choice = input("\nadd dish or type exit: ")
    if choice.lower() == "exit":
        break

    # take dish input
    dish_id = input("enter dish id: ")
    dish_name = input("enter dish name: ")
    ingredients = input("enter ingredients: ")
    instructions = input("enter instructions: ")

    # create dish object
    dish = Dish(dish_id, dish_name, ingredients, instructions)

    # add to cookbook
    cookbook.addition_dish(dish)

# display all dishes
cookbook.display()