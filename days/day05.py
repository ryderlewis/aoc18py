from typing import Iterable

from .day import Day


class Day05(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def reacted(polymer: Iterable[str]) -> int:
        new = []
        for c in polymer:
            if len(new) == 0:
                new.append(c)
                continue
            if new[-1].lower() == c.lower() and new[-1] != c:
                new.pop()
            else:
                new.append(c)
        return len(new)

    def part1(self) -> str:
        polymer = self.data_lines()[0]
        return str(self.reacted(polymer))

    def part2(self) -> str:
        polymer = self.data_lines()[0]
        mlen = self.reacted(polymer)
        for o in range(ord('a'), ord('z')+1):
            mlen = min(mlen, self.reacted((p for p in polymer if p.lower() != chr(o))))
        return str(mlen)
