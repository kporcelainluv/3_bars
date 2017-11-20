import json
import sys
from operator import itemgetter
import gpxpy.geo


def dict_of_names_and_seats_of_bars(file_of_bars):
    list_of_bars = dict()
    for feature in file_of_bars["features"]:
        bar_name = feature["properties"]["Attributes"]["Name"]
        seats_count = feature["properties"]['Attributes']["SeatsCount"]
        list_of_bars[bar_name] = seats_count
    return list_of_bars


def get_biggest_bar(file_of_bars):
    bars = dict_of_names_and_seats_of_bars(file_of_bars)
    biggest_bar = [bar_name for bar_name, seats_count in bars.items() if seats_count == max(bars.values())]
    return biggest_bar


def get_smallest_bar(file_of_bars):
    bars = dict_of_names_and_seats_of_bars(file_of_bars)
    smallest_bar = [bar_name for bar_name, seats_count in bars.items() if seats_count == min(bars.values())]
    return smallest_bar


def get_closest_bar(file_of_bars, longitude, latitude):
    list_of_bars = list()
    for bar in file_of_bars:
        bar_name = bar["properties"]['Attributes']["Name"]
        bar_coordinates = bar["geometry"]["coordinates"]
        distance_from_bar = gpxpy.geo.haversine_distance(longitude, latitude, bar_coordinates[0], bar_coordinates[1])
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
