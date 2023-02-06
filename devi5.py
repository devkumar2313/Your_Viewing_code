
Your Question:What does the "yield" keyword do?
Your Answer:-

The "yield" keyword is used in Python to create generators. Generators are a type of iterable, which means that they can be used in for loops. Generators allow you to generate a sequence of values over time, instead of generating the entire sequence at once.

For example, if you wanted to generate the numbers from 0 to 10, you could use a generator like this:

def generate_numbers():
    for i in range(11):
        yield i

for num in generate_numbers():
    print(num)

# Output: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10