# Write a call_times decorator that will take a file_name as a parameter,
# count the number of function calls and write to the file
# in the format f'{func_name} has been called {count} times.\n'


func_name = {}
call_func_counter = 0


def call_times(file_name):
    def wrapper(func):
        def inner(*args, **kwargs):
            global func_name
            global call_func_counter
            func(*args, **kwargs)
            if func.__name__ in func_name:
                call_func_counter += 1
            else:
                call_func_counter = 1
            func_name[func.__name__] = [call_func_counter, file_name]
            with open(file_name, 'w') as f:
                func(*args, **kwargs)
                for function, call in func_name.items():
                    if file_name in call:
                        f.write(f'{function} be called {call[0]} times.\n')
            return f'{file_name} was update'
        return inner
    return wrapper




