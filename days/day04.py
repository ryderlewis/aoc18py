from .day import Day
from dataclasses import dataclass
from collections import Counter
import re

@dataclass(frozen=True)
class Nap:
    sleep: int
    wake: int

    def duration(self):
        return self.wake - self.sleep

    def minutes(self) -> range:
        return range(self.sleep, self.wake)


@dataclass(frozen=True)
class Shift:
    guard_id: int
    naps: tuple[Nap, ...]


class Day04(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def solver(self):
        shifts = self.parse()
        guard_counts = {}
        for shift in shifts:
            guard_counts.setdefault(shift.guard_id, Counter())
            for nap in shift.naps:
                guard_counts[shift.guard_id].update(nap.minutes())

        most_minutes = max((sum(c.values()) for c in guard_counts.values()))
        sleepiest = next((g for g, c in guard_counts.items() if sum(c.values()) == most_minutes))

        most_common = max((c.most_common(1)[0][1]) for c in guard_counts.values() if len(c) > 0)
        doziest = next((g for g, c in guard_counts.items() if len(c) and c.most_common(1)[0][1] == most_common))

        return sleepiest, doziest, guard_counts

    def part1(self) -> str:
        guard_id, _, counts = self.solver()
        return str(guard_id * counts[guard_id].most_common(1)[0][0])

    def part2(self) -> str:
        _, guard_id, counts = self.solver()
        return str(guard_id * counts[guard_id].most_common(1)[0][0])

    def parse(self) -> list[Shift]:
        ret = []
        pattern = r'^\[\d+-\d+-\d+ \d+:(\d+)\] (?:falls a(sleep)|(wake)s up|Guard #(\d+) begins shift)$'
        guard_id: int|None = None
        sleep_time: int|None = None
        naps = []

        for line in sorted(self.data_lines()):
            m = (re.match(pattern, line))
            assert m is not None
            minute, s, w, g = m.groups()
            if s == 'sleep':
                sleep_time = int(minute)
            elif w == 'wake':
                naps.append(Nap(sleep=sleep_time, wake=int(minute)))
                sleep_time = None
            elif g:
                if guard_id is not None:
                    ret.append(Shift(guard_id=guard_id, naps=tuple(naps)))
                naps = []
                guard_id = int(g)
        if guard_id is not None:
            ret.append(Shift(guard_id=guard_id, naps=tuple(naps)))
        return ret