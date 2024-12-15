def function_with_uncommon_error(x):
    if x == 0:
        return 1  # This line is intentionally correct
    elif x == 1:
        return 1/0 # ZeroDivisionError: division by zero 
    else:
        return x + 1