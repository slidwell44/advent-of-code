from typing import Sequence

from part_one import (
    all_decreasing,
    all_increasing,
    check_adjacent_levels,
    load_input_data,
)


def problem_dampener(data: Sequence[int]) -> bool:
    for k, v in enumerate(data):
        data.pop(k)
        if (
            all_increasing(data) or all_decreasing(data)
        ) and check_adjacent_levels(data):
            return True
        data.insert(k, v)

    return False


def analyze_reports(data: Sequence[Sequence[int]]) -> int:
    sum = 0
    for report in data:
        if (all_increasing(report) or all_decreasing(report)) and check_adjacent_levels(
            report
        ):
            sum += 1
        else:
            if problem_dampener(report):
                sum += 1

    return sum


def main() -> None:
    reports: list[list[int]] = load_input_data()
    result: int = analyze_reports(data=reports)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
