choice=eval(input('''
     press1 for addition
     press2 for subtraction
     press3 for multiplication
     press4 for division
     enter your choice: '''))

if choice in [1,2,3,4]:
    num1=eval(input('enter first num:'))
    num2=eval(input('enter second num:'))

    if choice==1:
        print(num1+num2)
    elif choice==2:
        print(num1-num2)
    elif choice==3:
        print(num1*num2)
    elif choice==4:
        print(num1/num2)
else:
    print('invalid choice')