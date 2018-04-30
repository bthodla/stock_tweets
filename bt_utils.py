import math

def prime(n: int) -> list:
    a, s = 1, []
    while a <= n:
        if is_prime (a):
            s.append(a)
        a += 1
    return s


def is_prime(n: int) -> bool:
    is_prime_no = True
    b, c = pow(n, 1 / 2), 2
    while c <= b:
        if n % c == 0:
            is_prime_no = False
            break
        else:
            is_prime_no = True
        c += 1
    return is_prime_no


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
    if n in fibonacci_series(n):
        return True
    else:
        return False


def fib_prime_matches (n: int) -> list:
    return sorted ((set (fibonacci_series (n)) & set (prime (n))))


# def factorial (n: int) -> int:
#     if n == 0:
#         return 1
#     else:
#        recurse = factorial(n - 1)
#        result = n * recurse
#        return result


def find (word: [], letter: str, startpos=0) -> int:
    index = startpos
    while index < len (word):
        if word [index] == letter:
            return index
        else:
            index = index + 1
    return -1


def reverse (s: str) -> str:
#    return s [::-1]
    result = ''
    for i in range(len(s)):
        i = i + 1
        result = result + s[i * -1]
    return result


def is_palindrome (s: str) -> bool:
    return s.lower() == reverse(s.lower())


def has_letter (s: str, letter: str) -> bool:
    return letter in s


def count (s: str, letter: str) -> int:
    count = 0
    for l in s.upper():
        if l == letter.upper():
            count = count + 1
    return count


def avoids (s: str, fbw: str) -> bool:
    # return ''.join(sorted(fbw)) not in ''.join(sorted(s))
    for i in range (0, len (fbw)):
        if fbw [i] in s:
            return False
    return True


def uses_all (s: str, pw: str) -> bool:
    # return ' '.join(sorted(pw)) in ' '.join(sorted(s))
    # for i in range (0, len (pw)):
    #     if pw [i] not in s:
    #         return False
    for letter in pw:
        if letter not in s:
            return False
    return True


def uses_only (s: str, pw: str) -> bool:
    return sorted(pw) == sorted(s)


def print_lyrics():
    print ("Hey Jude! Don't you be sad! Take a sad song and make it better")
    print ("Remember to get it into your heart! Then you can start to make it better")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

def right_justify(s: str, line_length:int):
    return (line_length - len(s)) * ' ' + s
