from depr import main

def test(count):
    _sentence = "hello " * count
    results = main(_sentence)
    return (count, results[2])

tests = []

x = 10

for i in range(10):
    count = x + (i * 10)

    tests.append(test(count))

print(tests)