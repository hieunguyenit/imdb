class Actor(object):

    def __init__(self, name, birth_date, bio):
        self.id = id
        self.name = name
        self.birth_date = birth_date
        self.bio = bio

    def display(self):
        print self.name + self.birth_date + self.bio


class Movie(object):
    def __init__(self, name, year, description):
        self.name = name
        self.year = year
        self.description = description

    def display(self):
        print self.name + self.year + self.description
