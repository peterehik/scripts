from typing import List


def print_array(array: List[List]):
    for i in range(0, len(array)):
        print(" ".join([str(num) if num >= 10 else '0%s' % num for num in array[i]]))


def spiral(n: int) -> List[List]:
    if n == 1:
        return [[1]]
    start, end = (0, n)
    array = [[-1 for i in range(0, n)] for j in range(0, n)]
    start_number = 1
    while start_number <= n*n:
        start_number = populate_spiral_array(array, start, end, start_number, n*n)
        start += 1
        end -= 1
    return array


def populate_spiral_array(array: List[List], start: int, end: int, start_number: int, max_num: int) -> int:

    # move forward
    for i in range(start, end):
        if overwrite(array, start, i, start_number):
            start_number += 1

    if start_number > max_num:
        return start_number

    #move down
    for i in range(start, end):
        if overwrite(array, i, end-1, start_number):
            start_number += 1

    if start_number > max_num:
        return start_number

    #move left
    for i in reversed(range(start, end)):
        if overwrite(array, end-1, i, start_number):
            start_number += 1

    if start_number > max_num:
        return start_number

    #move up
    for i in reversed(range(start, end)):
        if overwrite(array, i, start, start_number):
            start_number += 1

    return start_number


def overwrite(array: List[List], row: int, col: int, val: int) -> bool:
    if array[row][col] == -1:
        array[row][col] = val
        return True
    return False


def prompter_function(fn):
    keep_running = 'Y'
    while keep_running == 'Y' or keep_running == 'y':
        fn()
        keep_running = input("continue? Y or N: ")
    return fn


def main():
    keep_running = 'Y'
    while keep_running == 'Y' or keep_running == 'y':
        number = int(input("enter spiral length: "))
        print_array(spiral(number))
        keep_running = input("continue? Y or N: ")


if __name__ == "__main__":
    main()
