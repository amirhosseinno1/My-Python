def fibs (num):
    result = [0,1]
    for i in range(num):
        result.append(result[-2] + result[-1])
    return result
x = int(input('num:'))
print(fibs(x))