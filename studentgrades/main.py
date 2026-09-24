n=input('enter your name:')
choice=eval(input('''
       press1 for 1 subject
       press2 for 2 subjects
       press3 for 3 subjects
       press4 for 4 subjects
       press5 for 5 subjects
       press6 for 6 subjects
       '''))
if choice in [1,2,3,4,5,6]:
    if choice==1:
        sub1=eval(input('enter first sub marks:'))
    elif choice==2:
        sub1=eval(input('enter 1st sub marks:'))
        sub2=eval(input('enter 2nd sub marks:'))
    elif choice==3:
        sub1=eval(input('enter 1st sub marks:'))
        sub2=eval(input('enter 2nd sub marks:'))
        sub3=eval(input('enter 3rd sub marks:'))
    elif choice==4:
        sub1=eval(input('enter 1st sub marks:'))
        sub2=eval(input('enter 2nd sub marks:'))
        sub3=eval(input('enter 3rd sub marks:'))
        sub4=eval(input('enter 4th sub marks:'))
    elif choice==5:
        sub1=eval(input('enter 1st sub marks:'))
        sub2=eval(input('enter 2nd sub marks:'))
        sub3=eval(input('enter 3rd sub marks:'))
        sub4=eval(input('enter 4th sub marks:'))
        sub5=eval(input('enter 5th sub marks:'))
    elif choice==6:
        sub1=eval(input('enter 1st sub marks:'))
        sub2=eval(input('enter 2nd sub marks:'))
        sub3=eval(input('enter 3rd sub marks:'))
        sub4=eval(input('enter 4th sub marks:'))
        sub5=eval(input('enter 5th sub marks:'))
        sub6=eval(input('enter 6th sub marks:'))

    if choice==1:
            res=sub1
    elif choice==2:
            res=sub1+sub2
    elif choice==3:
            res=sub1+sub2+sub3
    elif choice==4:
            res=sub1+sub2+sub3+sub4
    elif choice==5:
            res=sub1+sub2+sub3+sub4+sub5
    elif choice==6:
            res=sub1+sub2+sub3+sub4+sub5+sub6
    print(res)

total_marks=int(input('enter total_marks:'))
maximum_marks=int(input('enter maximum marks:'))
percentage=total_marks/maximum_marks*100
print('percentage:',percentage)
if percentage>=90:
      print('Grade A')
elif percentage>=80:
      print('Grade B')
elif percentage>=70:
      print('Grade C')
elif percentage>=60:
      print('Grade D')
else:
      print('Fail')