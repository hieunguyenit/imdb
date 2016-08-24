class Actor(object):
    def __init__(self, actor_id, name, birth_date, bio):
        self.actor_id = actor_id
        self.name = name
        self.birth_date = birth_date
        self.bio = bio

    def display(self):
        print self.name + self.birth_date + self.bio


class Movie(object):
    def __init__(self, movie_id, name, year, description):
        self.movie_id = movie_id
        self.name = name
        self.year = year
        self.description = description

    def display(self):
        print self.name + self.year + self.description
