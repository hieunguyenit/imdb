from models import *
import os


def create_data_object(data_name, line):
    """
    Create data object based on its data name
    :param data_name:
    :param line:
    :return:
    """
    obj = object
    tokens = line.split('|')

    if data_name == 'actor':
        obj = Actor(tokens[0], tokens[1], tokens[2], tokens[3])
    elif data_name == 'movie':
        obj = Movie(tokens[0], tokens[1], tokens[2], tokens[3])

    return tokens[0], obj


def load_data_by_id(data_name, file_path):
    """
    Load data object by its name and path
    :param data_name:
    :param file_path:
    :return:
    """
    with open(file_path) as data_file:
        obj_id, data_obj = create_data_object(data_name, data_file.readline())

    return obj_id, data_obj


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
                obj_id, data_obj = load_data_by_id(name, file_path)
                col_dict[obj_id] = data_obj

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
