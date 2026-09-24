score=0

print('welcome to Quiz')
print('Quiz started')

# Question 1
print('\n1.what is the capital of India')
print('A.Delhi')
print('B.maharastra')
print('C.andhra')
print('D.jaipur')

ans1=input('enter the choice:')
if ans1.upper()=='A':
    print('correct')
    score+=1
else:
    print('wrong')

# Question 2
print('\n2.How many planets are there')
print('A.2')
print('B.5')
print('C.7')
print('D.9')
ans2=input('enter the choice:')
if ans2.upper()=='D':
    print('correct')
    score+=1
else:
    print('wrong')

# Question 3
print('\n3.what is the capital of Rajasthan')
print('A.Delhi')
print('B.jaisalmer')
print('c.jaipur')
print('D.Qsar')
ans3=input('enter the choice:')
if ans3.upper()=='C':
    print('correct')
    score+=1
else:
    print('wrong')

print('\nQuiz completed!!')
print('your score is: ',score,'/3')