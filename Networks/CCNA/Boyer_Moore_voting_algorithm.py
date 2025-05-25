# Boyer - Moore Voting Algorithm
# Requires the majority element to be > n / 2
# It is not working if it is <= n / 2

numbers = [1, 2, 3, 1, 4, 1, 1]
result = 0
count = 0
for number in numbers:
    if count == 0:
        result = number
    count += 1 if result == number else -1
    print(f"{number=}  {result=}  {count=}")
print(f"\n\n{result=}")