import bt_utils

if __name__ == '__main__':
    # n, fib_list, prime_list = 0, [], []
    #
    # n = input('Enter a number: ')
    # n = int(n)
    # fib_list = fibonacci_series(n)
    # prime_list = prime(n)
    # print('Fibonacci Numbers: ' + str(len(fib_list)) + ' - ', str(fib_list))
    # print('Prime Numbers: ' + str(len(prime_list)) + ' - ', str(prime_list))
    # print(str(n) + ' is a Fibonacci Number:' + str(is_fib_number(n)))
    # print(fib_prime_matches(n))
    # print('Factorial of ' + str(10) + ':' + str(factorial(10)))
    # print('10th Fibonacci :' + str(fibonacci(10)))
    # print(bt_utils.find('Bhasker Thodla', 'h', 2))
    # print(bt_utils.reverse('Bhasker Thodla'))
    # print (bt_utils.is_palindrome('Able was I ere I saw Elba'))
    # print(bt_utils.is_palindrome('Malayalam'))
    fin = open ('words.txt')
    print (fin)
    line_count, e_lines = 0, 0
    for line in fin:
        word = line.strip()
        line_count += 1
        if bt_utils.uses_all (word, 'aeiou'):
            print (word)
            e_lines += 1
    print('% of "e" words: ', e_lines / line_count * 100)



