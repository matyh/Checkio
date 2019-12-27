#!/usr/bin/env checkio --domain=py run flatten-list

# 
# END_DESC


def flat_list(array):
    new = []
    for i in array:
        if isinstance(i, list):
            new.extend(flat_list(i))
        else:
            new.append(i)
    return new


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')

print(flat_list([[[[[[[[[4294967295]]]]]]]]]))
print(flat_list([[[2]], [4, [5, 6, [[[6]]], 6, 6, 6], 7]]))
print(flat_list([-1, [1, [-2, [3], [[5], [10, -11], [1, 100, [-1000, [5000]]], [20, -10, [[[]]]]]]]]))
