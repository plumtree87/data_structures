import random

class SweepStakes():
    def __init__(self):
        self.contestants = [
            {"firstName": "John", "lastName": "Smith", }, {"firstName": "Aaron", "lastName": "Biggs"}, {"firstName": "Tom", "lastName": "Jerry"},
            {"firstName": "Tim", "lastName": "Allen"}, {"firstName": "Bill", "lastName": "Barr"}
        ]

    def pick_Winner(self):
        num = random.randint(0, 4)
        print(self.contestants[num]['firstName'], self.contestants[num]['lastName'])