import datetime


class Actor(object):

    def __init__(self, name, birth_date, bio):
        self.id = id
        self.name = name
        self.birth_date = datetime.datetime.fromtimestamp(float(birth_date)/1000.0).strftime('%m/%d/%Y')
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
