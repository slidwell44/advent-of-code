from dataclasses import dataclass, field
from pathlib import Path

INPUT_PATH: Path = Path(__file__).parent / "input.txt"


@dataclass
class ParserResult:
    left: list[str] = field(default_factory=list)
    right: list[str] = field(default_factory=list)


def parse_input() -> ParserResult:
    result = ParserResult()
    with INPUT_PATH.open("r") as f:
        data: list[str] = f.read().splitlines()

    for line in data:
        x, y = line.split()
        result.left.append(x.strip())
        result.right.append(y.strip())

    return result


def sum_smallest(data: ParserResult) -> int:
    sums: list[int] = []
    while data.left and data.right:
        min_left: str = min(data.left)
        min_right: str = min(data.right)
        distance: int = abs(int(min_left) - int(min_right))
        sums.append(distance)
        data.left.remove(min_left)
        data.right.remove(min_right)
    return sum(sums)


def main() -> None:
    response: ParserResult = parse_input()
    result: int = sum_smallest(data=response)
    print(result)


if __name__ == "__main__":
    main()
