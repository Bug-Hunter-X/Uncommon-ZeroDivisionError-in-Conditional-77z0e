def function_with_uncommon_error_solution(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 5
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

result = function_with_uncommon_error_solution(0)
print(result)

result = function_with_uncommon_error_solution(5)
print(result)