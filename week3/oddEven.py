while True:
    n=int(input('enter a number: '))
    if n==0:
        print('program exited')
        break;
    if n%2==0:
        print(str(n)+ ' is even')
    else:
        print(str(n)+ ' is odd')
    