def check_prime(n):
    x = 2
    while x * x <= n:
        if n % x == 0:
            return False
        x += 1
    return True

print(check_prime(4))