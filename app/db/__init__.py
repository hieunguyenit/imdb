from models import *
import os


def load_data(path, name):
    # type: (object, object) -> object
    col_dict = dict()

    for root, dirs, files in os.walk(path + name):
        #
        for file_name in files:
            if file_name.endswith(".data"):
                file_path = os.path.join(root, file_name)
                #
                with open(file_path) as data_file:
                    for line in data_file:
                        tokens = line.split('|')
                        #
                        print tokens
                        if name == 'actor':
                            obj = Actor(tokens[1], tokens[2], tokens[3])
                        elif name == 'movie':
                            obj = Movie(tokens[1], tokens[2], tokens[3])
                        #
                        col_dict[tokens[0]] = obj
    return col_dict


def build_index(file_path):
    actor_index = dict()
    movie_index = dict()

    with open(file_path) as join_file:
        for line in join_file:
            tokens = line.rstrip().split('|')

            actor_index[tokens[0]] = tokens[1:]

            for i in range(1, len(tokens)):
                if tokens[i] in movie_index:
                    movie_index[tokens[i]].append(tokens[0])
                else:
                    movie_index[tokens[i]] = [tokens[0]]

    my_index = dict(actor=actor_index, movie=movie_index)

    return my_index
