from part_one import ParserResult, parse_input


def compute_similarity(data: ParserResult) -> int:
    similarity: list[int] = []
    for x in data.left:
        number_of_occurrences: int = data.right.count(x)
        value: int = number_of_occurrences * int(x)
        similarity.append(value)
    return sum(similarity)


def main() -> None:
    response: ParserResult = parse_input()
    result: int = compute_similarity(data=response)
    print(result)


if __name__ == "__main__":
    main()
