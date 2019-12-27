# https://py.checkio.org/en/mission/sort-array-by-element-frequency/


# def frequency_sort(items):
#     """
#     :param items: iterable
#     :return: returns iterable sorted by the elements frequency
#     """
#     unique = []
#     for item in items:
#         if item not in unique:
#             unique.append(item)
#     counter = [(k, items.count(k)) for k in unique]
#     # counter.sort(key=lambda x: x[1], reverse=True)
#     result = []
#     for x, y in counter:
#         result += y * [x]
#     return result


def frequency_sort(items):
    # interesting solution, explanation below
    return sorted(items,
                  key=lambda x: items.count(x) - items.index(x) / len(items),
                  reverse=True)

    # for i in items:
    #     x = items.count(i)
    #     y = items.index(i)
    #     z = len(items)
    #     print(f'number {i} - items.count(i) {x} - items.index(i) {y} / len(items) {z} --- {x - y / z}')


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")
