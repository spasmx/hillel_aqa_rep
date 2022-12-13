# Write a call_times decorator that will take a file_name as a parameter,
# count the number of function calls and write to the file
# in the format f'{func_name} has been called {count} times.\n'

def call_times(file_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            func(*args, **kwargs)
            file1 = open(file_name, 'a+')
            file2 = open(file_name)
            count = file2.read().count(func.__name__) + 1
            log = f'{func.__name__} called {count} times.\n'

            file1.write(log)

            file2.close()
            file1.close()
        return inner
    return wrapper



