def prost(n):
    for i in range(2, n-1):
        if n % i == 0:
            return False
    return True


n = 7
print("Число простое?", prost(n))