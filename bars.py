import json
from operator import itemgetter
import sys
import math


def get_biggest_bar_name(data_from_file):
    dict_of_bars = {}
    for feature in data_from_file["features"]:
        bar_name = feature["properties"]["Attributes"]["Name"]
        seats_count = feature["properties"]['Attributes']["SeatsCount"]
        dict_of_bars[bar_name] = seats_count
    biggest_bar = [name for name, seats_count in dict_of_bars.items() if seats_count == max(dict_of_bars.values())]
    return " ".join(biggest_bar)


def get_smallest_bar_name(data_from_file):
    dict_of_bars = {}
    for feature in data_from_file["features"]:
        bar_name = feature["properties"]["Attributes"]["Name"]
        seats_count = feature["properties"]['Attributes']["SeatsCount"]
        dict_of_bars[bar_name] = seats_count
    smallest_bar = [name for name, seats_count in dict_of_bars.items() if seats_count == min(dict_of_bars.values())]
    return ", ".join(smallest_bar)


def get_closest_bar_name(data_from_file, longitude, latitude):
    list_of_bars = []
    for bar in data_from_file:
        bar_name = bar["properties"]['Attributes']["Name"]
        bar_coordinates = bar["geometry"]["coordinates"]
        distance_from_bar = [math.fabs(longitude - bar_coordinates[0]) + math.fabs(latitude - bar_coordinates[1])]
        list_of_bars.append((bar_name, distance_from_bar))
    sorted_by_distance_list_of_bars = sorted(list_of_bars, key=itemgetter(1))
    return sorted_by_distance_list_of_bars[0][0]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            read_data_from_input_file = json.loads(f.read())
            print("Самый большой бар – ", get_biggest_bar_name(read_data_from_input_file))
            print("Самый маленький бар – ", get_smallest_bar_name(read_data_from_input_file))
            print("Самый близкий бар – ", get_closest_bar_name(read_data_from_input_file["features"], float(input("Введите долготу: ")), float(input("Введите широту: "))))
