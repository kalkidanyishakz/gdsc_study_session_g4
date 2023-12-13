def odd_even():
    num=int(input("Enter a number: "))
    return "Even" if num%2==0 else "Odd"


def maximu():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    return a if a>b else b


#print((lambda a=int(input("Enter the 1st number: ")), b=int(input("Enter the 2nd number: ")): a if a>b else b)())

def lengthy_numbers():
    num=input('Enter a number ')
    return 'Short' if len(num)<10 else 'Long'


def list_sum(num=1):
    num_input=int(input("Enter \'0\' to quit Enter a number: "))
    sum=num_input+num
    if num_input==0:
        return sum-1
    return list_sum(sum)

print(list_sum())