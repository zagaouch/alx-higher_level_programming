#!/usr/bin/python3
""" An empty class base"""


import json
import csv

class Base:
    """defines a class base that has a private attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """static method returns the string [] or JSON string """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"

        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dicts)
                jsonfile.write(json_string)

    def from_json_string(json_string):
        """static method returns the string [] or JSON string """
        if json_string is None or len(json_string) < 1:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        new_file = cls.__name__ + ".json"
        try:
            with open(new_file, "r") as f:
                lst = cls.from_json_string(f.read())
                return [cls.create(**d) for d in lst]
        except Exception:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        data = [obj.id, obj.width, obj.height, obj.x, obj.y]
                    elif cls.__name__ == "Square":
                        data = [obj.id, obj.size, obj.x, obj.y]
                    writer.writerow(data)

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        objs = []

        try:
            with open(filename, "r") as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[0]))
                    elif cls.__name__ == "Square":
                        obj = cls(int(row[1]), int(row[2]), int(row[3]), int(row[0]))
                    objs.append(obj)
            return objs
        except FileNotFoundError:
            return []
