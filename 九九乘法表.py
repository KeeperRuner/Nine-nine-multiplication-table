a = 1
while a <= 9: #当变量j小于等于9时
    i = 1
    while i <= a:
        print(f'{i}*{a}={a*i}',end='\t')
        i += 1 
    print()
    a += 1