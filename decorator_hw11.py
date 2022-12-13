# Write a call_times decorator that will take a file_name as a parameter,
# count the number of function calls and write to the file
# in the format f'{func_name} has been called {count} times.\n'
def call_times(file_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            file1 = open(file_name, 'a+')
            file2 = open(file_name)
            func(*args, **kwargs)
            count = file2.read().count(func.__name__) + 1
            func_counts = {func.__name__: count}
            log = f'{func.__name__} called {func_counts[func.__name__]} times.\n'
            file1.write(log)

        return inner
    return wrapper





@call_times('foo.txt')
def foo():
    pass

@call_times('foo.txt')
def boo():
    pass

@call_times('calls.txt')
def doo():
    pass

print(foo())
print(boo())
print(foo())
print(doo())
print(doo())
print(foo())
print(foo())


