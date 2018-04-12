# coding: utf-8
"""
To describe a specific position on the surface of the Earth,
  we must rely on the geographic coordinate system. The
  geographic coordinate system is a method used to give every
  possible location on Earth to be specified by a set of numbers
  or letters. A common choice of coordinates is latitude and longitude.
  With this information we can calculate a distance between two
  points along a surface.

For simplicity’s sake, we will suppose that the Earth is a perfect
sphere with a radius of 6,371 kilometers (it gives a mistake no more
than 0.3%). You are given two point coordinates and you must find the
shortest distance between these points on the surface of the Earth,
measured along the surface of the Earth.

Coordinates are given as a string with the latitude and longitude
separated by comma and/or whitespace. Latitude and longitude are
represented in the follow format:

    d°m′s″X

In this example, "d" is degrees, "m" is minutes, "s" is seconds as
integers, while "X" is "N" (north) or "S" (south) for a latitude
and "W" (west) or "E" (east) for a longitude.

The result should be given as a number in kilometers with a
precision of ±0.1 (100 metres).
*********************** ЗАДАНИЕ *******************************
Precondition: Correct Coordinates.

Input: Two arguments. Coordinates as strings (unicode).

Output: The distance as a number (int or float).
"""
from math import sin, cos, radians, pi, acos
import re

# approximate radius of earth in km
R = 6371

PAT = re.compile(r'(\d+)°(\d+)′(\d+)″([EWSN])')


def convert_to_radians(coor):
    if 'W' in coor or 'S' in coor:
        return radians(-(int(coor[0]) * 3600 + int(coor[1]) * 60 + int(coor[2])) / 3600.0)
    return radians((int(coor[0]) * 3600 + int(coor[1]) * 60 + int(coor[2])) / 3600.0)


def distance_my(first, second):
    first = PAT.findall(first)
    second = PAT.findall(second)
    lat1, lon1, lat2, lon2 = map(convert_to_radians, (first + second))
    direct_distance = sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2)
    return round(R * acos(direct_distance), 1) if acos(direct_distance) != 0 else pi * R


def extract_position(position_str):
    items = re.search('(\d+)\D(\d+)\D(\d+)\D(\w)', position_str).groups()
    if 'W' in position_str or 'S' in position_str:
        return radians(-(int(items[0]) * 3600
                         + int(items[1]) * 60 + int(items[2])) / 3600.0)
    return radians((int(items[0]) * 3600 + int(items[1]) * 60 + int(items[2])) / 3600.0)


def distance(first, second):
    if len(first.split()) == 2:
        first = first.split()
    else:
        first = first.split(',')
    if len(second.split()) == 2:
        second = second.split()
    else:
        second = second.split(',')
    first_latitude, first_longitude, second_latitude, second_longitude = \
        map(extract_position, first + second)
    direct_distance = sin(first_latitude) * sin(second_latitude) + \
                      cos(first_latitude) * cos(second_latitude) * cos(first_longitude - second_longitude)

    if acos(direct_distance) == 0:
        return pi * R
    return round(R * acos(direct_distance), 1)


if __name__ == '__main__':
    #  These "asserts" using only for self-checking and not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=1):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision

    assert almost_equal(
        distance(u"51°28′48″N 0°0′0″E", u"46°12′0″N, 6°9′0″E"), 739.2), "From Greenwich to Geneva"
    assert almost_equal(
        distance(u"90°0′0″N 0°0′0″E", u"90°0′0″S, 0°0′0″W"), 20015.1), "From South to North"
    assert almost_equal(
        distance(u"33°51′31″S, 151°12′51″E", u"40°46′22″N 73°59′3″W"), 15990.2), "Opera Night"
