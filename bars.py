import json
import math
import sys


def collect_data_from_json(json_data):
    with open(json_data, "r") as json_file:
        bars_attributes = json.loads(json_file.read())
    return bars_attributes["features"]


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_biggest_bar(bars):
    return max(bars, key=lambda x: get_seats_count_from_bar(x))


def get_smallest_bar(bars):
    return min(bars, key=lambda x: get_seats_count_from_bar(x))


def count_distance_between_two_bars(longitude, latitude, input_longitude, input_latitude):
    return math.fabs(longitude - input_longitude) + math.fabs(latitude - input_latitude)


def get_closest_bar(bars, longitude, latitude):
    return min(bars, key=lambda x: count_distance_between_two_bars(longitude, latitude, x["geometry"]["coordinates"][0],
                                                           x["geometry"]["coordinates"][1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_data = sys.argv[1]
        print("Самый большой бар: ", get_biggest_bar(collect_data_from_json(json_data)))
        print("Самый маленький бар: ", get_smallest_bar(collect_data_from_json(json_data)))
        print("Самый ближайший бар: ", get_closest_bar(collect_data_from_json(json_data), float(input("Введите долготу: ", )), float(input("Введите широту: ",))))
