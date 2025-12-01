from pathlib import Path
from typing import Sequence

INPUT_PATH: Path = Path(__file__).parent / "input.txt"

LAST_VALUE: int = -1


def load_input_data() -> list[list[int]]:
    response: list[list[int]] = []
    with INPUT_PATH.open("r") as f:
        for line in f.readlines():
            data: list[int] = [int(x) for x in line.split()]
            response.append(data)
    return response


def check_adjacent_levels(data: Sequence[int]) -> bool:
    return all(1 <= abs(earlier - later) <= 3 for earlier, later in zip(data, data[1:]))


def all_decreasing(data: Sequence[int]) -> bool:
    return all(earlier > later for earlier, later in zip(data, data[1:]))


def all_increasing(data: Sequence[int]) -> bool:
    return all(earlier < later for earlier, later in zip(data, data[1:]))


def analyze_reports(data: Sequence[Sequence[int]]) -> int:
    sum = 0
    for report in data:
        if (all_increasing(report) or all_decreasing(report)) and check_adjacent_levels(
            report
        ):
            sum += 1

    return sum


def main() -> None:
    reports: list[list[int]] = load_input_data()
    result: int = analyze_reports(data=reports)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
