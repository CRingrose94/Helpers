import collections


def log_missing():
    print('Key added')
    return 0


current = {'green': 12, 'blue': 3}

result = collections.defaultdict(log_missing, current)
print('Before: ', dict(result))

increments = [('red', 5), ('blue', 17), ('orange', 9)]
for key, amount in increments:
    result[key] += amount

print('After: ', dict(result))


class CountMissing:
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


counter = CountMissing()
result = collections.defaultdict(counter, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2
