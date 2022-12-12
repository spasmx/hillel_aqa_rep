# Write a function that takes an integer - number.
# The function must return 'yes' if number is a power of 2, otherwise 'no'.
# It is forbidden to use the exponentiation function or operator.

def is_power_if_two(x, _count=1):
    if not isinstance(x, int):
        return f'Invalid argument. {x} must be integer'

    if x == 2:
        return f'Yes\n2 in degree {_count} = {2 ** _count}'
    if x == 1:
        return 'No'

    return is_power_if_two(int(x/2), _count + 1) if x > 0 else 'Argument must be more than 0'


