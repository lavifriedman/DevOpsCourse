class Dogs:
    def __init__(self, name, color, race):
        self.name = name
        self.color = color
        self.race = race

    def bark_if_cat(self, animal):
        if type(animal) == Cats:
            print("Hav Hav")


new_dog = Dogs("jack", "black", "")
