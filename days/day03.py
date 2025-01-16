from typing import Optional

from .day import Day
from dataclasses import dataclass
import re


@dataclass
class Rug:
    rug_id: int
    l_pos: int
    t_pos: int
    width: int
    height: int

    def overlap(self, other: "Rug") -> Optional["Rug"]:
        l = max(self.l_pos, other.l_pos)
        r = min(self.l_pos+self.width-1, other.l_pos+other.width-1)
        t = max(self.t_pos, other.t_pos)
        b = min(self.t_pos+self.height-1, other.t_pos+other.height-1)
        if l <= r and t <= b:
            return Rug(-1, l, t, r-l+1, b-t+1)
        return None

    def area(self) -> int:
        return self.width * self.height

class Day03(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.rugs = self.parse()

    def part1(self) -> str:
        overlaps = set()
        for i, r1 in enumerate(self.rugs):
            for r2 in self.rugs[i+1:]:
                if o := r1.overlap(r2):
                    for x in range(o.l_pos, o.l_pos+o.width):
                        for y in range(o.t_pos, o.t_pos+o.height):
                            overlaps.add((x, y))
        return str(len(overlaps))

    def part2(self) -> str:
        overlaps = set()
        all_ids = set([r.rug_id for r in self.rugs])
        for i, r1 in enumerate(self.rugs):
            for r2 in self.rugs[i+1:]:
                if r1.overlap(r2):
                    overlaps.add(r1.rug_id)
                    overlaps.add(r2.rug_id)
        return str((all_ids - overlaps).pop())

    def parse(self) -> list[Rug]:
        ret = []
        for line in self.data_lines():
            # #4 @ 835,854: 14x11
            m = re.match(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)$', line)
            assert m is not None
            ret.append(Rug(*map(int, m.groups())))
        return ret
