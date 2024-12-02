#! /usr/bin/env python3

"""Solution for https://adventofcode.com/2023/day/5"""

import re
from collections import namedtuple
from itertools import chain, count
from sys import argv


class MapList:
    Map = namedtuple("Map", ["destination", "source", "length"])

    def __init__(self, maps=None):
        self.maps: list[MapList.Map] = maps or []

    def add_map(self, map):
        if map is not MapList.Map:
            map = MapList.Map(*map)
        self.maps.append(map)

    def __getitem__(self, item):
        for map in self.maps:
            if 0 <= (offset := item - map.source) < map.length:
                return map.destination + offset
        return item


class ReverseMapList:
    def __init__(self, map_list):
        self.map_list = map_list

    def __getitem__(self, item):
        if self.map_list[item] == item:
            yield item
        for map in self.map_list.maps:
            if 0 <= (offset := item - map.destination) < map.length:
                yield map.source + offset


def make_mappings(lines: list[str]):
    x = y = None
    current_mapping = MapList()
    mappings = {}
    for line in lines:
        if not line.strip():
            continue

        if re_match := re.match(r"(.+)-to-(.+) map:", line):
            if x:
                mappings[x] = (y, current_mapping)
            x, y = re_match[1], re_match[2]
            current_mapping = MapList()
        else:
            current_mapping.add_map([int(n) for n in line.split()])
    mappings[x] = (y, current_mapping)
    return mappings


def get_location(seed, mappings):
    destination, value = "seed", seed
    while destination != "location":
        destination, mapping = mappings[destination]
        value = mapping[value]
    return value


def part1(seed_line, mappings):
    print(min(get_location(s, mappings) for s in seed_line))


def corresponding_seeds(value, destination, rmappings):
    source, rmapping = rmappings[destination]
    if source == "seed":
        yield from rmapping[value]
    else:
        for v in rmapping[value]:
            yield from corresponding_seeds(v, source, rmappings)


def is_in_seed_ranges(seed, seed_ranges):
    for start, length in seed_ranges:
        if 0 <= (seed - start) < length:
            return True
    return False


def get_lowest_location(seed_ranges, rmappings):
    for location in count():
        for seed in corresponding_seeds(location, "location", rmappings):
            if is_in_seed_ranges(seed, seed_ranges):
                return location


def part2(seed_line, mappings):
    # TODO: optimize (currently 34s w/ PyPy, 205s w/ CPython)
    rmappings = {
        destination: (source, ReverseMapList(mapping))
        for source, (destination, mapping) in mappings.items()
    }
    seed_ranges = [
        (seed_line[i], seed_line[i + 1]) for i in range(0, len(seed_line), 2)
    ]
    print(get_lowest_location(seed_ranges, rmappings))


def main():
    fpath = "input" if len(argv) <= 1 else argv[1]
    with open(fpath) as f:
        lines = f.read().splitlines()
    seed_line, *rest = lines
    seed_line = [int(n) for n in re.findall(r"\d+", seed_line)]
    mappings = make_mappings(rest)
    part1(seed_line, mappings)
    part2(seed_line, mappings)


if __name__ == "__main__":
    main()
