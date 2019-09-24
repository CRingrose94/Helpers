import itertools as it


def grouper(inputs, n, filler=None):
    iters = [iter(inputs)] * n
    return it.zip_longest(*iters, fillvalue=filler)


def better_enumerate(option=1):

    letters = ['a', 'b', 'c', 'd', 'e']

    if option == 1:
        tups = []
        for i, let in enumerate(letters):
            tups.append((i, let))
        return tups
    elif option == 2:
        return [(i, let) for i, let in enumerate(letters)]
    else:
        return list(zip(it.count(), letters))

    
def flatten(sequence):
    """
    Given any nested sequences, flatten it to a single sequence
    """

    for item in sequence:
        if hasattr(item, '__iter__'):
            yield from flatten(item)
        else:
            yield item


if __name__ == '__main__':
    print(better_enumerate())
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(grouper(nums, 3)))

    a = flatten([1, [2, 3], [4, [5]]])
    print(list(a))
