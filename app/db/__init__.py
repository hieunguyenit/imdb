from models import *
import os


def load_data(path, name):
    # type: (object, object) -> object
    col_dict = {}

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
