"""
The Euclidean Algorithm is a technique for quickly finding the Greatest Common Divisor (GCD) of two integers.

The Euclidean Algorithm for finding GCD(A,B) is as follows:
    - If A = 0 then GCD(A,B)=B, since the GCD(0,B)=B, and we can stop.  
    - If B = 0 then GCD(A,B)=A, since the GCD(A,0)=A, and we can stop.
    - If both A and B are non zero, then write A in quotient remainder form (A = B⋅Q + R) and find GCD(B,R) using the Euclidean Algorithm since GCD(A,B) = GCD(B,R)
"""

def greater_common_divisor(a: int, b: int) -> int:
    if a == 0 or a == b:
        return b
    if b == 0:
        return a
    if a > b:
        r: int = a % b
        return greater_common_divisor(a=b, b=r)
    if b > a:
        r: int = b % a
        return greater_common_divisor(a=a, b=r)


if __name__ == '__main__':
    a: int = 0
    b: int = 192
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 192
    
    a: int = 270
    b: int = 0
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 270
    
    a: int = 270
    b: int = 192
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 6
    
    a: int = 1_000
    b: int = 11
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 1
    
    a: int = 88
    b: int = 16
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 8
    
    a: int = 32
    b: int = 256
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 32
    
    a: int = 347_595_023
    b: int = 34_729
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 1
    
    a: int = 178_296
    b: int = 268_442
    gcd: int = greater_common_divisor(a=a, b=b)
    print(f"{a=}\t{b=}\t{gcd=}")         # Answer: 2