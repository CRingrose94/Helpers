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
    a = flatten([1, [2, 3], [4, [5]]])

    print(list(a))
