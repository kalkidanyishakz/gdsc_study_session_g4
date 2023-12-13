def try_catch_adder():
    num1=0; num2=0
    try:
        num1=int(input('Enter the first number: '))
        num2=int(input('Enter the second number: '))
        print(num1+num2)
        try:
            print(num1/num2)
        except ZeroDivisionError:
            print('division by zero is not allowed')
    except ValueError:
      print('Enter only a number')
    

    
try_catch_adder()