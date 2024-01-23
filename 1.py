def find_sum_fibonachi():
    a = 3
    b = 4
    result = 0
    while a + b < 30:
        c = a
        a = b
        b = c + b
        if a % 2 == 0:
            result += a
    return result

if __name__ == '__main__':
    print(find_sum_fibonachi())
