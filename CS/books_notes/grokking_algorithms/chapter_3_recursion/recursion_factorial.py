from re import sub

"""
re.sub() is a function from the re (regular expressions) module. 
It replaces occurrences of a pattern in the string with a specified replacement.

The pattern r'(\d{3})' is a regular expression. It matches any sequence of exactly three digits (\d{3}).
The parentheses around \d{3} create a capture group, which means that the matched digits will be remembered for later use.

\\1, is the replacement string. The \\1 refers to the first capture group (the three digits), and the , adds a comma after the digits.
"""

def factorial(number: int) -> int:
    return 1 if number in (0, 1) else number * factorial(number - 1)


if __name__ == '__main__':
    maximum: int = 20
    for number in range(maximum):
        fact: int = factorial(number=number)
        re_fact: str = sub(r'(\d{3})', '\\1,', str(fact)[::-1])[::-1]
        if re_fact[0] == ',':
            re_fact = re_fact[1:]
        print(f"{number}! = {re_fact}")