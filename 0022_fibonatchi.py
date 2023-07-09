N = int(input('N : '))
Fib = []
Fib.append(1)
Fib.append(1)
for i in range(2,N+1):
    Fib.append(Fib[i-2]+Fib[i-1])
print(Fib)