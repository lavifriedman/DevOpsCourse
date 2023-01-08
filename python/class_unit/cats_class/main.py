class Cats:
    def __init__(self, name, color, food_type):
        self.name = name
        self.color = color
        self.food_type = food_type

    def chane_food_type(self, new_food_type):
        self.food_type = new_food_type

    def return_all_attributes(self):
        return self.name, self.color, self.food_type
