# Write a call_times decorator that will take a file_name as a parameter,
# count the number of function calls and write to the file
# in the format f'{func_name} has been called {count} times.\n'


func_call_times = {}
count = 0

def call_times(file_name):

    def wrapper(func):
        def inner(*args, **kwargs):
            global func_call_times
            global count
            func(*args, **kwargs)
            if func.__name__ in func_call_times:
                count += 1
            else:
                count = 1
            func_call_times[func.__name__] = count
            with open(file_name, 'w+') as f:
                func(*args, **kwargs)

                f.write(f'{func.__name__} be called {count} times.\n')
            return f'{file_name} was update'

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


print(boo())
print(boo())
print(boo())
print(doo())
print(doo())
print(doo())
print(doo())
print(doo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())
print(foo())


print(func_call_times)



