def function_with_uncommon_error(x):
    if x == 0:
        return 1
    elif x == 1:
        return 0 # Avoid division by zero
    else:
        return x + 1

# Example of error handling
try:
    result = function_with_uncommon_error(1)
    print(f"The result is: {result}")
except ZeroDivisionError as e:
    print(f"Error: {e}") 