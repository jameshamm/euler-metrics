import json
import os
from collections import defaultdict
from config import get_directory, get_extensions


def get_details():
    directory = get_directory()
    extension = get_extensions()
    return directory, extension


def get_json_of_solved_problems():
    directory, extension = get_details()

    solutions = defaultdict(list)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                s = file.split(".")
                solutions[s[1]].append(s[0])
                solutions[s[1]].sort()
    return solutions

if __name__ == "__main__":
    solved = get_json_of_solved_problems()
    with open("solved.json", "w") as f:
        json.dump(solved, f)