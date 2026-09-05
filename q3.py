# Q3 - primes using for-else

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        # the else of a for loop only runs if the loop finished without a break.
        # so if no divisor was found we get here and the number is prime.
        return True
    return False


print(is_prime(7))
print(is_prime(12))

n = int(input())

primes = []
for num in range(2, n + 1):
    if is_prime(num):
        primes.append(num)

print(*primes)
