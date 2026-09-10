import json


def rw_state(func):
    def wrapper(*args, **kwargs):
        with open('state.json', 'r') as file: data = func(json.load(file), *args, **kwargs)
        with open('state.json', 'w') as file: json.dump(data, file, indent=4)
    return wrapper

def w_state(func):
    def wrapper(*args, **kwargs):
        with open('state.json', 'w') as file: json.dump(func(*args, **kwargs), file, indent=4)
        
    return wrapper

def r_state(func):
    def wrapper():
        with open('state.json', 'r') as file: return func(json.load(file))
    return wrapper