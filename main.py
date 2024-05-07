"""
Blackjack
"""


def calculate_score(a: int, b: int, c: int):
    if a + b + c <= 21:
        return a + b + c
    elif a + b + c >= 21 and a or b or c == 11:
        return (a + b + c) - 10
        # if a + b + c >= 21:
    else:
        return "'BUST'"


"""
Even Numbers
"""


def even_positive_numbers(nums: [list]) -> list:
    even_positive_nums = []
    for num in nums:
        if num % 2 == 0 and num >= 0:
            even_positive_nums.append(num)
    return even_positive_nums


if __name__ == '__main__':
    print(calculate_score(a=10, b=9, c=1))
    # print(calculate_score(a=11, b=9, c=2))
    # print(even_positive_numbers([3, -8, 1, 1, 2]))
    # print(even_positive_numbers([3, -8, 1, 4, 2]))
    # print(even_positive_numbers([3, -8, 22, 6, 2]))


