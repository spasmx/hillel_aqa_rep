# Write a call_times decorator that will take a file_name as a parameter,
# count the number of function calls and write to the file
# in the format f'{func_name} has been called {count} times.\n'
import shutil
def call_times(file_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            file1 = open('file.txt', 'a+')
            file2 = open('file.txt')
            count = file2.read().count(func.__name__) + 1
            log = f'{func.__name__} called {count} times.\n'
            file1.write(log)
            file2.close()
            file1.close()
            shutil.copyfile('file.txt', file_name)
            file3 = open(file_name, 'w')
            file4 = open(file_name, 'a+')
            file3.write(f'{func.__name__} called {count} times.\n')
            if func.__name__ in file4.read():
                file4.write(f'{func.__name__} called {count} times.\n')


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
print(boo())
print(doo())
print(doo())
print(foo())
print(foo())
print(foo())
print(foo())



