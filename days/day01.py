from .day import Day


class Day01(Day):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def part1(self) -> str:
        return str(sum(self.parse()))

    def part2(self) -> str:
        vals = self.parse()
        curr = 0
        seen = {curr}
        while True:
            for v in vals:
                curr += v
                if curr in seen:
                    return str(curr)
                seen.add(curr)

    def parse(self) -> list[int]:
        ret = []
        for line in self.data_lines():
            val = int(line[1:])
            if line.startswith('+'):
                ret.append(val)
            elif line.startswith('-'):
                ret.append(-val)
            else:
                raise ValueError(line)
        return ret
