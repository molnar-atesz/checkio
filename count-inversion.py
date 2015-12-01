def count_inversion(sequence):
    all_inversion = 0
    for index in range(len(sequence)-1):
        current_number = sequence[index]
        next_index = index + 1
        all_inversion += count_inversions_for(current_number, sequence[next_index:])

    return all_inversion


def count_inversions_for(number, sub_sequence):
    num_of_inversions = 0
    for item in sub_sequence:
        if item <= number:
            num_of_inversions += 1
    return num_of_inversions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"