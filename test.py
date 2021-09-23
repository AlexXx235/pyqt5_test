import json
from json import *

filename = "users.txt"

users = {
    "admin": "admin",
    "loki": "koki",
    "vodka": "pivo",
    "pupa": "lupa"
}


def save(users):
    with open(filename, "w") as f:
        json.dump(users, f)


def load():
    with open(filename, "r") as f:
        return json.load(f)


if __name__ == '__main__':
    save(users)