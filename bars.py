import json
import math
import sys


def collect_data_from_json(path_to_file):
    with open(path_to_file, "r") as json_file:
        bars_data = json.loads(json_file.read())
    return bars_data["features"]


def get_biggest_bar(bars):
    return max(bars, key=lambda x: get_seats_count_from_bar(x))


def get_smallest_bar(bars):
    return min(bars, key=lambda x: get_seats_count_from_bar(x))


def get_closest_bar(bars, input_long, input_lat):
    closest_bar = min(bars, key=lambda bar: count_distance_between_user_and_bar(bar, input_long, input_lat))
    return closest_bar


def get_seats_count_from_bar(bar):
    return int(bar["properties"]["Attributes"]["SeatsCount"])


def print_bar_info(bar, bar_phrase):
    print("Самый " + bar_phrase + " бар: ")
    print(bar["properties"]["Attributes"]["Name"])
    print("Адрес:", bar["properties"]["Attributes"]["Address"])
    print("Число мест:", int(bar["properties"]["Attributes"]["SeatsCount"]))
    print("Тел.:", bar["properties"]["Attributes"]["PublicPhone"][0]["PublicPhone"])


def count_distance_between_user_and_bar(bar, input_long, input_lat):
    long = bar["geometry"]["coordinates"][0]
    lat = bar["geometry"]["coordinates"][1]
    distance = math.sqrt(math.fabs(long - input_long) + math.fabs(lat - input_lat))
    return distance


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bars = collect_data_from_json(sys.argv[1])

        print_bar_info(get_biggest_bar(bars), 'большой')
        print_bar_info(get_smallest_bar(bars), "маленький")

        input_long = float(input("Введите вашу долготу: ", ))
        input_lat = float(input("Введите вашу широту: ", ))

        closest_bar = get_closest_bar(bars, input_long, input_lat)
        print_bar_info(closest_bar, "ближайший")
