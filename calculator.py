while True:
    print('----------SIMPLE CALCULATOR----------')
    a=float(input('Enter the first number : '))
    b=float(input('Enter the second number : '))
    print('--------------------------------------')
    print('1.Addition (a+b)')
    print('2.Subtraction (a-b)')
    print('3.Multiplication (a*b)')
    print('4.Division (a/b)')
    print('5.Modulo Division (a%b)')
    print('6.Power (a^b)')
    print('7.EXIT')
    print('---------------------------------------')
    ch=int(input('Now enter your choice from the above options (1|2|3|4|5|6|7) : '))
    if ch==1:
        print(f'The sum {a} + {b} = {a+b}')
    elif ch==2:
        print(f'The difference {a} - {b} = {a-b}')
    elif ch==3:
        print(f'The product {a} x {b} = {a*b}')
    elif ch==4:
        print(f'The quotient {a} / {b} = {a/b}')
    elif ch==5:
        print(f'The remainder {a} % {b} = {a%b}')
    elif ch==6:
        print(f'The result for {a} ^ {b} = {a**b}')
    elif ch==7:
        print('Bye Bye.......')
        break
    else:
        print('You are entered an invalid choice...!\nTry again!')
