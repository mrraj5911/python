a=int(input("entr the total students: "))
b={}
for i in range(a):
    name=input("enter the name: ")
    marks=input("enter the marks: ")
    b[name]=marks
print(b)
while True:
    name=input('enter the name of student to fine the marks: ')
    marks=b.get(name,-1)
    if marks==-1:
        print('student of this name is not here')
    else:
        print('the marks of student {} is {}'.format(name,marks))
    option=input('do you want to find the marks of student [y/n]')
    if option=='n':
        break
print('thanks for comming'
      '')