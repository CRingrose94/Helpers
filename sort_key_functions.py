# Sort a list of mixed types
lst = [1, 3, '2']


def sort_int(a):
    return int(a)


# Using pre-defined function
print(sorted(lst, key=sort_int))
# Using in-place lambda
print(sorted(lst, key=lambda item: int(item)))


# Sorting via class attributes
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f'{self.name}: {self.grade}'


students = [
    Student('jim', 10),
    Student('jack', 9),
    Student('bob', 6),
    Student('Fred', 12)
]

# Sort  alphabetically
print(sorted(students, key=lambda student: getattr(student, 'name')))
# Sort alphabetically; case insensitive
print(sorted(students, key=lambda student: getattr(student, 'name').lower()))
# Sort by grade
print(sorted(students, key=lambda student: getattr(student, 'grade'), reverse=True))
