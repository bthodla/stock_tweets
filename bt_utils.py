def prime(n: int) -> list:
    a, s = 1, []
    while a <= n:
        if is_prime (a):
            s.append(a)
        a += 1
    return s


def is_prime(n: int) -> bool:
    is_prime = True
    b, c = pow(n, 1 / 2), 2
    while c <= b:
        if n % c == 0:
            is_prime = False
            break
        else:
            is_prime = True
        c += 1
    return is_prime


def fibonacci_series(n: int) -> list:
    a, b, s = 0, 1, []
    assert isinstance(n, int)
    while a <= n:
        # print(a, end=' ')
        s.append(a)
        a, b = b, a + b
    return s


def fibonacci (n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n -1) + fibonacci(n - 2)


def is_fib_number (n: int) -> bool:
    if (n in fibonacci_series(n)):
        return True
    else:
        return False


def fib_prime_matches (n: int) -> list:
    return sorted ((set (fibonacci_series (n)) & set (prime (n))))


def factorial (n: int) -> int:
    if (n == 0):
        return 1
    else:
        recurse = factorial(n - 1)
        result = n * recurse
        return result


def find (word: [], letter: str, startpos=0) -> int:
    index = startpos
    while index < len (word):
        if word [index] == letter:
            return index
        else:
            index = index + 1
    return -1


def reverse (s: str) -> str:
    return s [::-1]


def is_palindrome (s: str) -> bool:
    return s.lower() == reverse(s.lower())


def has_letter (s: str, letter: str) -> bool:
    return letter in s


def avoids (s: str, fbw: str) -> bool:
    for i in range (0, len (fbw)):
        if fbw [i] in s:
            return False
    return True
