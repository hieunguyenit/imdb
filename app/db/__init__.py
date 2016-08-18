from models import *
import os


def load_data(path, name):
    """
    Load data based on file path and its table name
    :param path: data directory path
    :param name: table name
    :return: dictionary contains <id, object value>
    """
    # Collection dictionary contains object id and its value
    col_dict = dict()

    for root, dirs, files in os.walk(path + name):
        # Browse all data files
        for file_name in files:
            if file_name.endswith(".data"):
                file_path = os.path.join(root, file_name)
                # Read object data in each file
                with open(file_path) as data_file:
                    for line in data_file:
                        tokens = line.split('|')
                        # Check data table name
                        if name == 'actor':
                            obj = Actor(tokens[1], tokens[2], tokens[3])
                        elif name == 'movie':
                            obj = Movie(tokens[1], tokens[2], tokens[3])
                        # Add object data to collection dictionary
                        col_dict[tokens[0]] = obj
    return col_dict


def build_index(file_path):
    """
    Build index to look up the relationship between actors and movies
    :param file_path: join.data file path
    :return: dictionary of actor index and movie index
    """
    actor_index = dict()
    movie_index = dict()

    with open(file_path) as join_file:
        for line in join_file:
            tokens = line.rstrip().split('|')
            # actor index
            actor_index[tokens[0]] = tokens[1:]
            # movie index
            for i in range(1, len(tokens)):
                if tokens[i] in movie_index:
                    movie_index[tokens[i]].append(tokens[0])
                else:
                    movie_index[tokens[i]] = [tokens[0]]

    my_index = dict(actor=actor_index, movie=movie_index)

    return my_index
