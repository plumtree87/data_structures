
class Places:
    def __init__(self):
        self.places_on_birthday = {"DZ Discovery Zone", "Chuckee Cheese", "Parents house", "Outback Steakhouse", "Olive Garden"}

    def print_birthday_places(self):
        list_of_places = list(self.places_on_birthday)
        for place in list_of_places:
            print(place)