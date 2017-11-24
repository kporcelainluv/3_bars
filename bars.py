import json
from operator import itemgetter
import sys
import math

def collect_data_from_json(bars):
    dict_of_bars = {}
    for feature in bars["features"]:
        bar_name = feature["properties"]["Attributes"]["Name"]
        seats_count = feature["properties"]['Attributes']["SeatsCount"]
        dict_of_bars[bar_name] = seats_count
    return dict_of_bars


def get_biggest_bar(bars):
    dict_of_bars = collect_data_from_json(bars)
    biggest_bar = " ".join(
        [name for name, seats_count in dict_of_bars.items() if seats_count == max(dict_of_bars.values())])
    for feature in bars["features"]:
        if feature["properties"]["Attributes"]["Name"] == biggest_bar:
            print(" ")
            print("Самый большой бар: ", biggest_bar)
            print("адрес: ", feature["properties"]["Attributes"]['Address'])
            print("телефон: ",
                  " ".join(phone['PublicPhone'] for phone in feature["properties"]["Attributes"]['PublicPhone']))
            print("количество мест - ", feature["properties"]["Attributes"]['SeatsCount'])
            print(" ")
            return feature["properties"]["Attributes"]


def get_smallest_bar(bars):
    dict_of_bars = collect_data_from_json(bars)
    smallest_bar = [name for name, seats_count in dict_of_bars.items() if seats_count == min(dict_of_bars.values())][0]
    for feature in bars["features"]:
        if feature["properties"]["Attributes"]["Name"] == smallest_bar:
            print(" ")
            print("Самый маленький бар: ", smallest_bar)
            print("адрес: ", feature["properties"]["Attributes"]['Address'])
            print("телефон: ",
                  " ".join(phone['PublicPhone'] for phone in feature["properties"]["Attributes"]['PublicPhone']))
            print("количество мест - ", feature["properties"]["Attributes"]['SeatsCount'])
            print(" ")
            return feature["properties"]["Attributes"]


def get_closest_bar(bars, longitude, latitude):
    list_of_bars = []
    for bar in bars:
        bar_name = bar["properties"]['Attributes']["Name"]
        bar_coordinates = bar["geometry"]["coordinates"]
        distance_from_bar = [math.fabs(longitude - bar_coordinates[0]) + math.fabs(latitude - bar_coordinates[1])]
        list_of_bars.append((bar_name, distance_from_bar))
        sorted_by_distance_list_of_bars = sorted(list_of_bars, key=itemgetter(1))
    print(" ")
    print("Самый близкий бар – ", sorted_by_distance_list_of_bars[0][0])
    print("адрес: ", bar["properties"]["Attributes"]['Address'])
    print("телефон: ", " ".join(phone['PublicPhone'] for phone in bar["properties"]["Attributes"]['PublicPhone']))
    print("количество мест - ", bar["properties"]["Attributes"]['SeatsCount'])
    print(" ")
    return bar["properties"]["Attributes"]


if __name__ == '__main__':
    if len(sys.argv) > 1:
        with open(sys.argv[1], "r") as f:
            decoding_json = json.loads(f.read())
            print(get_biggest_bar(decoding_json))
            print(get_smallest_bar(decoding_json))
            print(get_closest_bar(decoding_json["features"], float(input("Введите долготу: ")),
                                  float(input("Введите широту: "))))
