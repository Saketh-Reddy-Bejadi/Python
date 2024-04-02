
def countPrimeSetBits(left, right):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(left, right + 1):
        binary_str = bin(i)[2:]  
        one_count = binary_str.count('1')
        if is_prime(one_count):
            res.append(1)
        else:
            res.append(0)
    return res
l=6
r=10
print(countPrimeSetBits(l,r))