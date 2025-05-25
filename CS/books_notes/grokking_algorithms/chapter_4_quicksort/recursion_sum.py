from typing import Union

def add(iterable: Union[list, tuple, set]) -> int:
    if len(iterable) == 1:
        return iterable[0]
    else:
        return iterable[0] + add(iterable=iterable[1:])


if __name__ == '__main__':
    numbers: list[int] = [number for number in range(11)]
    total: int = add(iterable=numbers)
    print(f"{total=}")