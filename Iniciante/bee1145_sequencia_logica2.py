def seq_log(x, y):
    cont = 1
    while cont <= y:
        for i in range(1, x + 1):
            if i == x:
                print(cont)
                cont += 1
            else:
                print(cont, end=' ')
                cont += 1
            


x, y = map(int, input().split(' '))

seq_log(x, y)