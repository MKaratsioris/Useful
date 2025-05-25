from typing import Union

def maximum(iterable: Union[list, tuple, set]) -> int:
    if len(iterable) == 2:
        return iterable[0] if iterable[0] > iterable[1] else iterable[1]
    sub_max = maximum(iterable[1:])
    return iterable[0] if iterable[0] > sub_max else sub_max


if __name__ == '__main__':
    numbers: list[int] = [number for number in range(10)]
    maxim: int = maximum(iterable=numbers)
    print(f"{maxim=}")