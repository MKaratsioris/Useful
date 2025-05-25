def is_prime(number: int | float) -> bool:
    if isinstance(number, float):
        return False
    if number <= 1:
        return False
    for n in range(2, int(number ** 0.5) + 1):
        if number % n == 0:
            return False
    return True


if __name__ == '__main__':
    max: int = 10
    count: int = 0
    for number in range(max + 1):
        is_true = is_prime(number=number)
        if is_true:
            count += 1
            print(f"{count}. {number}")
    print(f"In range [0, {max}] there are in total {count} prime numbers.")
    
    number: int = 3
    print(f"Is {number} a prime number? {'Yes' if is_prime(number) else 'No'}")