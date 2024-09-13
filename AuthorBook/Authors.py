# Part 1: Modelling Trades
import decimal

class Author():
    def __init__(self, first_name, last_name, bio, book):
        self.first_name = first_name
        self.last_name = last_name
        self.bio = bio
        this.book = book

    #getters
    @property
    def get_first_name(self):
        return self.first_name

    @property
    def get_last_name(self):
        return self.last_name

    @property
    def get_bio(self):
        return self.bio

    def __str__(self):
        return (f"Author  First_name: {self.fisrt_name}, Last_name: {self.last_name}, Bio: {self.bio}")
