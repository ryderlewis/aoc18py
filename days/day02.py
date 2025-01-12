from .day import Day
from collections import Counter


class Day02(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        boxes = self.parse()
        two_count = 0
        three_count = 0
        for b in boxes:
            c = Counter(b)
            if 2 in c.values():
                two_count += 1
            if 3 in c.values():
                three_count += 1
        return str(two_count*three_count)

    def part2(self) -> str:
        boxes = self.parse()
        for i, b1 in enumerate(boxes):
            for b2 in boxes[i+1:]:
                diff_count = sum(1 for c1, c2 in zip(b1, b2) if c1 != c2)
                if diff_count == 1:
                    return ''.join(c1 for c1, c2 in zip(b1, b2) if c1 == c2)
        return ""

    def parse(self) -> list[str]:
        return self.data_lines()
