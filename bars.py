import json
import math
import sys


def collect_data_from_json(json_data):
    with open(json_data, "r") as json_file:
        list_of_bar_attributes = json.loads(json_file.read())
    return list_of_bar_attributes["features"]


def get_seats_count_from_bar(bar):
    return int(bar["properties"]['Attributes']["SeatsCount"])


def get_biggest_bar(bars):
    return max(bars, key=lambda x: get_seats_count_from_bar(x))


def get_smallest_bar(bars):
    return min(bars, key=lambda x: get_seats_count_from_bar(x))


def get_closest_from_me_bar(longtitude, latitude, input_longtitude, input_latitude):
    return math.fabs(longtitude - input_longtitude) + math.fabs(latitude - input_latitude)


def get_closest_bar(bars, longtitude, latitude):
    return min(bars, key=lambda x: get_closest_from_me_bar(longtitude, latitude, x["geometry"]["coordinates"][0],
                                                           x["geometry"]["coordinates"][1]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        json_data = sys.argv[1]
