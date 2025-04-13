#%기호
name = "최지웅"
age = 32
print("제 이름은 %s이고 나이는 %d입니다."%(name,age))

#format매소드
name = "최지웅"
age = 32
print('제 이름은 {}이고 나이는 {}입니다.'.format(name,age))

#fstring
name ="최지웅"
age = 32
print(f'제 이름은 {name}이고 나이는 {age}입니다.')

#별찍기
n = int(input())

for i in range(n):
    print(" "*(n-(i+1)),end="")
    print("*"*(i+1))