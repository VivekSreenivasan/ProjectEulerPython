def isPrime(n):
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False
    for c in n:
        
    
num = 600851475143
for c in range(1,50000):
    if(num % c and isPrime(c)):
        print c
