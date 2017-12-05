import json
import math
import sys


def collect_data_from_json(path_to_file):
    with open(path_to_file, "r") as json_file:
        bars_data = json.loads(json_file.read())
    return bars_data["features"]


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_biggest_bar(bars):
    return max(bars, key=lambda x: get_seats_count_from_bar(x))


def get_smallest_bar(bars):
    return min(bars, key=lambda x: get_seats_count_from_bar(x))


def count_distance_between_user_and_bar(longitude, latitude, input_longitude, input_latitude):
    return math.fabs(longitude - input_longitude) + math.fabs(latitude - input_latitude)


def get_closest_bar(bars, longitude, latitude):
    return min(bars,
               key=lambda x: count_distance_between_user_and_bar(longitude, latitude, x["geometry"]["coordinates"][0],
                                                                 x["geometry"]["coordinates"][1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
        bars = collect_data_from_json(path_to_file)
        print("Самый большой бар: ")
        print(json.dumps(get_biggest_bar(bars), indent=2, sort_keys=True, ensure_ascii=False))
        print("Самый маленький бар: ")
        print(json.dumps(get_smallest_bar(bars), indent=2, sort_keys=True, ensure_ascii=False))
        longitude = float(input("Введите вашу долготу: ", ))
        latitude = float(input("Введите вашу широту: ", ))
        print("Самый ближайший бар: ")
        print(json.dumps(get_closest_bar(bars, longitude, latitude), indent=2, sort_keys=True, ensure_ascii=False))
