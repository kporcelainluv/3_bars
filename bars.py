import json
import sys
from math import cos, asin, sqrt
from operator import itemgetter


def dict_of_names_and_seats_of_bars(data):
    list_of_bars = dict()
    features = data["features"]
    for feature in features:
        name = feature["properties"]["Attributes"]["Name"]
        seats_count = feature["properties"]['Attributes']["SeatsCount"]
        list_of_bars[name] = seats_count
    return list_of_bars


def get_biggest_bar(data):
    bars = dict_of_names_and_seats_of_bars(data)
    biggest_bar = [bar_name for bar_name, seats_count in bars.items() if seats_count == max(bars.values())]
    return biggest_bar


def get_smallest_bar(data):
    bars = dict_of_names_and_seats_of_bars(data)
    smallest_bar = [bar_name for bar_name, seats_count in bars.items() if seats_count == min(bars.values())]
    return smallest_bar


def count_distance_between_coordinates(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295
    a = 0.5 - cos((lat2 - lat1) * p) / 2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a))


def find_closest_coordinates(data, v):
    return min(data, key=lambda p: count_distance_between_coordinates(v[0], v[1], p[0], p[1]))


def get_closest_bar(bars, longitude, latitude):
    list_of_bars = list()
    for bar in bars:
        bar_name = bar["properties"]['Attributes']["Name"]
        bar_coordinates = bar["geometry"]["coordinates"]
        distance_from_bar = count_distance_between_coordinates(longitude, latitude, bar_coordinates[0],
                                                               bar_coordinates[1])
        list_of_bars.append((bar_name, distance_from_bar))
    sorted_by_distance_list_of_bars = sorted(list_of_bars, key=itemgetter(1))
    return sorted_by_distance_list_of_bars[0][0]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open("file.txt", "r") as f:
            opened_file = json.loads(f.read())
            print("Самый большой бар – ", get_biggest_bar(opened_file))
            print("Самый маленький бар – ", get_smallest_bar(opened_file))
            print("Самый близкий бар – ", get_closest_bar(opened_file["features"],
                                                          float(input("Введите долготу: ")), float(input("Введите широту: "))))
