def calculate_average(*args):
    sum=0;
    for i in args:
        sum+=i

    return sum/len(args)

print( 
      calculate_average(1,2,3)
)