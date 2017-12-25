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


def get_closest_bar(bars, long, lat):
    def distance(bars):
        input_long = bars["geometry"]["coordinates"][0]
        input_lat = bars["geometry"]["coordinates"][1]
        dist_user_and_bar = math.fabs(long - input_long) + math.fabs(lat - input_lat)
        return dist_user_and_bar

    closest_bar = min(bars, key=distance)
    return closest_bar


def get_name_of_the_bar(bar):
    return bar["properties"]['Attributes']["Name"]


def get_address_of_the_bar(bar):
    return bar["properties"]['Attributes']["Address"]


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_phone_number_of_bar(bar):
    return bar["properties"]['Attributes']["PublicPhone"][0]["PublicPhone"]


def print_bar_info(bar):
    print("Количество мест: ", get_seats_count_from_bar(bar))
    print("Адрес: ", get_address_of_the_bar(bar))
    print("Телефон: ", get_phone_number_of_bar(bar))
    return "   "


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
        bars = collect_data_from_json(path_to_file)
        biggest_bar = get_biggest_bar(bars)
        smallest_bar = get_smallest_bar(bars)

        print("Самый большой бар: ", get_name_of_the_bar(biggest_bar))
        print(print_bar_info(biggest_bar))
        print("Самый маленький бар: ", get_name_of_the_bar(smallest_bar))
        print(print_bar_info(smallest_bar))

        longitude = float(input("Введите вашу долготу: ", ))
        latitude = float(input("Введите вашу широту: ", ))
        closest_bar = get_closest_bar(bars, longitude, latitude)

        print("Ближайший бар: ", get_name_of_the_bar(closest_bar))
        print(print_bar_info(closest_bar))
