
def print_sequence(sequence: list):
    print(''.join(sequence))


def look_and_say(n: int):
    if n == 1:
        print('1')
        return
    n -= 1
    sequence = ['1']
    print('1')
    while n > 0:
        sequence = next_look_and_say_sequence(sequence)
        print_sequence(sequence)
        n -= 1


def next_look_and_say_sequence(sequence: list):
    count = 1
    cur = sequence[0]
    result = []
    cur_spot = 0
    for item in sequence[1:]:
        if item == cur:
            count += 1
        else:
            result.insert(cur_spot, str(count))
            result.insert(cur_spot + 1, cur)
            cur_spot += 2
            count = 1
            cur = item
    result.insert(cur_spot, str(count))
    result.insert(cur_spot + 1, cur)
    return result


def test_next_look_and_say_sequence():
    assert next_look_and_say_sequence(['1']), '11'
    assert next_look_and_say_sequence(['11']), '21'
    assert next_look_and_say_sequence(['21']), '1211'
    assert next_look_and_say_sequence(['1211']), '111221'


def main():
    look_and_say(1)
    print("="*12)
    look_and_say(8)


if __name__ == "__main__":
    main()

