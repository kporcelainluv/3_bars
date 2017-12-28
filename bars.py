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


def get_closest_bar(bars, distance_between_user_and_bar):
    closest_bar = min(bars, key=distance_between_user_and_bar)
    return closest_bar


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_bar_info(bar):
    print(bar["properties"]['Attributes']["Name"])
    print("Адрес:", bar["properties"]['Attributes']["Address"])
    print("Число мест:", int(bar["properties"]['Attributes']["SeatsCount"]))
    print("Тел.:", bar["properties"]['Attributes']["PublicPhone"][0]["PublicPhone"])
    return ""


if __name__ == '__main__':
    if len(sys.argv) > 1:
        bars = collect_data_from_json(sys.argv[1])

        print("Самый большой бар: ", end="")
        print(get_bar_info(get_biggest_bar(bars)))
        print("Самый маленький бар: ", end="")
        print(get_bar_info(get_smallest_bar(bars)))

        input_long = float(input("Введите вашу долготу: ", ))
        input_lat = float(input("Введите вашу широту: ", ))


        def distance_between_user_and_bar(bars):
            long = bars["geometry"]["coordinates"][0]
            lat = bars["geometry"]["coordinates"][1]
            dist_between_user_and_bar = math.sqrt((long - input_long) + math.fabs(lat - input_lat))
            return dist_between_user_and_bar


        closest_bar = get_closest_bar(bars, distance_between_user_and_bar)
        print("Ближайший бар: ", end="")
        print(get_bar_info(closest_bar))
