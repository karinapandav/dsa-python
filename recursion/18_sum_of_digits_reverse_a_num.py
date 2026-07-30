def sum_of_digits(n):
    last_digit = n % 10
    remaining = n // 10
    if n == 0:
        return 0 
    else:
        return last_digit + sum_of_digits(remaining)
print(sum_of_digits(3042))

def reverse_number(n):

    def helper(n, rev):
        if n == 0:
            return rev

        last_digit = n % 10
        return helper(n // 10, rev * 10 + last_digit)

    return helper(n, 0)


print(reverse_number(3042))