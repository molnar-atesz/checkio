def get_range_tuple(target, length):
    min = 0 if target == 0 else target - 1 
    max = target if target == length else target + 1
    return (min, max+1)

def count_neighbours(grid, row, col):
    count = 0
    row_range = get_range_tuple(row, len(grid)-1)
    col_range = get_range_tuple(col, len(grid[0])-1)
    for row_index in range(row_range[0], row_range[1]):
        for col_index in range(col_range[0], col_range[1]):
            if row_index != row or col_index != col:
                count += grid[row_index][col_index]
    print(count)
    return count

if __name__ == '__main__':
    count_neighbours(((1, 0, 0, 1, 0),
                      (0, 1, 0, 0, 0),
                      (0, 0, 1, 0, 1),
                      (1, 0, 0, 0, 0),
                      (0, 0, 1, 0, 0),), 1, 2)

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"

    assert count_neighbours(((1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),
                             (1, 0, 1, 0, 1),
                             (0, 1, 0, 1, 0),), 5, 4) == 2, "hmm"

    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"
