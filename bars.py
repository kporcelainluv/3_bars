import json
import math
import sys


def collect_data_from_json(path_to_file):
    with open(path_to_file, "r") as json_file:
        bars_data = json.loads(json_file.read())
    return bars_data["features"]


def get_name_of_the_bar(bar):
    return bar["properties"]['Attributes']["Name"]


def get_address_of_the_bar(bar):
    return bar["properties"]['Attributes']["Address"]


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_phone_number_of_bar(bar):
    return bar["properties"]['Attributes']["PublicPhone"][0]["PublicPhone"]


def get_biggest_bar(bars):
    return max(bars, key=lambda x: get_seats_count_from_bar(x))


def get_smallest_bar(bars):
    return min(bars, key=lambda x: get_seats_count_from_bar(x))


def distance_between_user_and_bar(long, lat, input_long, input_lat):
    return math.fabs(long - input_long) + math.fabs(lat - input_lat)


def get_closest_bar(bars, longitude, latitude):
    return min(bars,
               key=lambda x: distance_between_user_and_bar(longitude, latitude,
                                                           x["geometry"]["coordinates"][0],
                                                           x["geometry"]["coordinates"][1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        path_to_file = sys.argv[1]
        bars = collect_data_from_json(path_to_file)
        print()
        print("Самый большой бар: ", get_name_of_the_bar(get_biggest_bar(bars)))
        print("Количество мест: ", get_seats_count_from_bar(get_biggest_bar(bars)))
        print("Адрес: ", get_address_of_the_bar(get_biggest_bar(bars)))
        print("Телефон: ", get_phone_number_of_bar(get_biggest_bar(bars)))
        print()
        print("Самый маленький бар: ", get_name_of_the_bar(get_smallest_bar(bars)))
        print("Количество мест: ", get_seats_count_from_bar(get_smallest_bar(bars)))
        print("Адрес: ", get_address_of_the_bar(get_smallest_bar(bars)))
        print("Телефон: ", get_phone_number_of_bar(get_smallest_bar(bars)))
        print()
        longitude = float(input("Введите вашу долготу: ", ))
        latitude = float(input("Введите вашу широту: ", ))
        print()
        print("Самый ближайший бар: ", get_name_of_the_bar(get_closest_bar(bars, longitude, latitude)))
        print("Количество мест: ", get_seats_count_from_bar(get_closest_bar(bars, longitude, latitude)))
        print("Адрес: ", get_address_of_the_bar(get_closest_bar(bars, longitude, latitude)))
        print("Телефон: ", get_phone_number_of_bar(get_closest_bar(bars, longitude, latitude)))
