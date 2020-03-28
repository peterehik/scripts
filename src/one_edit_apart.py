from spiral import prompter_function


def one_edit_apart(word: str, other: str) -> bool:
    if len(word) == len(other):
        return _one_edit_apart_same_length(word, other)
    if len(word) + 1 == len(other):
        return _one_edit_apart_v1(word, other)
    if len(word) - 1 == len(other):
        return _one_edit_apart_v1(other, word)
    return False


def _one_edit_apart_v1(smaller: str, word: str) -> bool:
    diff_count = 0
    j = 0
    for i in range(0, len(word)):
        if j == len(smaller):
            diff_count += 1
        elif smaller[j] == word[i]:
            j += 1
        elif diff_count == 1:
            return False
        else:
            diff_count += 1
    return diff_count == 1


def _one_edit_apart_same_length(word, other):
    diff_count = 0
    for i in range(0, len(word)):
        if word[i] != other[i]:
            if diff_count == 1:
                return False
            diff_count += 1
    return diff_count == 1


def main():
    first = input('Enter first word: ')
    second = input('Enter second word: ')
    if one_edit_apart(first, second):
        print('Yes!')
    else:
        print('Nope')


if __name__ == "__main__":
    prompter_function(main)

