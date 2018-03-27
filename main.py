import bt_utils

if __name__ == '__main__':
    # n, fib_list, prime_list = 0, [], []
    #
    # n = input('Enter a number: ')
    # n = int(n)
    # fib_list = bt_utils.fibonacci_series(100)
    # prime_list = bt_utils.prime(100)
    # print('Fibonacci Numbers: ' + str(len(fib_list)) + ' - ', str(fib_list))
    # print('Prime Numbers: ' + str(len(prime_list)) + ' - ', str(prime_list))
    # print(str(55) + ' is a Fibonacci Number:' + str(bt_utils.is_fib_number(55)))
    # print(bt_utils.fib_prime_matches(100))
    # print('Factorial of ' + str(17) + ':' + str(bt_utils.factorial(17)))
    # print('15th Fibonacci :' + str(bt_utils.fibonacci(15)))
    # print(bt_utils.find('Bhasker Thodla', 'h', 2))
    # print(bt_utils.reverse('malayalam'))
    # print (bt_utils.is_palindrome('Able was I ere I saw Elba'))
    # print(bt_utils.is_palindrome('Malayalam'))
    search_str = 'aeiou'
    fin = open ('words.txt')
    print (fin)
    line_count, e_lines = 0, 0
    for line in fin:
        word = line.strip()
        line_count += 1
        if bt_utils.uses_all (word, search_str):
            print (word)
            e_lines += 1
    print('% of "e" words: ', e_lines / line_count * 100)
    print('No. of e-words:', e_lines)
    print('Total no. of words:', line_count)



