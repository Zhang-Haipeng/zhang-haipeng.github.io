def is_prime(s):
    mm = s-1
    while mm > 1:
        if s%mm == 0:
            return False
        mm -= 1
    return True

s = 0
prime_list = [2, 3, 5, 7, 11]
s = sum(prime_list)
n = 13

while n < 2000:
    if str(n)[-1] in ['1', '3', '7']:
        if is_prime(n):
            prime_list.append(n)
    n += 2
    if n % 1000 == 0:
        print(n)

sum(prime_list)