import random

number=random.randint(1,100)
n=0
while n!=number:
   n=int(input('enter a n:'))
   if n>number:
     print('Too high')
   elif n<number:
      print('Too low')
   elif n==number:
      print('correct')