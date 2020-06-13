# python3


def max_pairwise_product(numbers):
    m1 = max(numbers)

    del numbers[numbers.index(m1)]
    m2 = max(numbers)

    return m1 * m2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
