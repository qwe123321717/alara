def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True
max = 9999
primeList = []
for i in range(2,max):
    if isPrime(i):
        primeList.append(i)
            

a = int(input('input number?'))

for i in range(len(primeList)):
    while a % primeList[i] == 0:
        if a % primeList[i] == 0:
            print(primeList[i],end ='')
            if a / primeList[i] != 1:
                print(end ='*')       
        a //= primeList[i]
