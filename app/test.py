
from db import build_index

my_index = build_index('../data/join.data')

print my_index['movie']

print my_index['actor']
