from typing import Union

def count(iterable: Union[list, tuple, set]) -> int:
    if len(iterable) == 0:
        return 0
    return 1 + count(iterable=iterable[1:])

if __name__ == '__main__':
    numbers: list[int] = [number for number in range(10)]
    total: int = count(iterable=numbers)
    print(f"{total=}")