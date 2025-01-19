from collections import defaultdict
from typing import Iterable

from .day import Day
from dataclasses import dataclass

@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def mdist(self, dist: int) -> Iterable["Point"]:
        """
        enumerates all the points of a manhattan distance `dist` from this point
        """
        for dx in range(-dist, dist+1):
            if abs(dx) == dist:
                yield Point(self.x + dx, self.y)
            else:
                dy = dist - abs(dx)
                yield Point(self.x + dx, self.y - dy)
                yield Point(self.x + dx, self.y + dy)


class Day06(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.points = self.parse()

    def get_bounds(self) -> tuple[int, int, int, int, int]:
        """
        :return: span, min_x, max_x, min_y, max_y of the bounding rectangle
        """
        min_x = min((p.x for p in self.points))
        max_x = max((p.x for p in self.points))
        min_y = min((p.y for p in self.points))
        max_y = max((p.y for p in self.points))

        x_span = max_x - min_x + 1
        y_span = max_y - min_y + 1

        return (
            max(x_span, y_span) + 1,
            min_x - x_span - 1,
            max_x + x_span + 1,
            min_y - y_span - 1,
            max_y + y_span + 1,
        )

    def part1(self) -> str:
        span, min_x, max_x, min_y, max_y = self.get_bounds()
        # map it out!
        grid = {}
        infinites = set()
        for s in range(span+1):
            candidates = {}
            for p in self.points:
                for m in p.mdist(s):
                    if m not in grid:
                        if m in candidates:
                            candidates[m] = None
                        else:
                            candidates[m] = p
            grid.update(candidates)
            if s == span:
                infinites.update({v for v in candidates.values() if v is not None})

        # find the areas
        areas = defaultdict(int)
        for k, v in grid.items():
            if v is None:
                continue
            areas[v] += 1

        # for area in sorted(areas.values(), reverse=True):
        #     print(f"{area=}")
        return str(max(area for point, area in areas.items()
                       if point not in infinites))



    def part2(self) -> str:
        return "dayXX 2"

    def parse(self) -> list[Point]:
        ret = []
        for line in self.data_lines():
            x, y = map(int, line.split(', '))
            ret.append(Point(x, y))
        return ret
